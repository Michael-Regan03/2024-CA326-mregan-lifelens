from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CSVUploadSerializer, DaySerializer, DailyActivitySerializer, SubOptionSerialiser, EmotionPositiveSerialiser, ConditionSub1OptionSerialiser, EmotionTensionSerialiser, IllnessSerialiser
from .models import Day, DailyActivity, SubOption, Condition, ConditionSub1Option, ConditionSub2Option, Place, EmotionPositive, EmotionTension, Activity, SurveyAM, SurveyPM, Illness
from life_lens.lifelogDataMapping import mealAmountMapping, transportMapping, alcoholPerecent
from django.db.models import Max
import pandas as pd
import numpy as np
from datetime import time, datetime, timedelta
from .converts import sleepConverter, smokeConverter, activeConverter, ageConverter, alcoholConverter

actions = ['actionSubOption', 'condition' , 'conditionSub1Option', 'conditionSub2Option', 'place',
            'emotionPositive', 'emotionTension','activity']
                
models = [SubOption, Condition, ConditionSub1Option, ConditionSub2Option, Place,
            EmotionPositive, EmotionTension, Activity ]


class DailyActivitiesCSVUpload(APIView):
    #User authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request, format=None):
        serializer = CSVUploadSerializer(data=request.data)

        if serializer.is_valid():
            csv_file = serializer.validated_data['file']
            data_set = csv_file.read().decode('UTF-8')
        
            #coverting into data frame for mapping using pandas
            df = pd.read_csv(pd.io.common.StringIO(data_set))
            
            df.loc[df['actionSub'] == 'meal_amount', 'actionSubOption'] = df.loc[df['actionSub'] == 'meal_amount', 'actionSubOption'].map(mealAmountMapping)
            df.loc[df['actionSub'] == 'move_method', 'actionSubOption'] = df.loc[df['actionSub'] == 'move_method', 'actionSubOption'].map(transportMapping)
            
            #resolving NaN error for nullable attributes
            df['conditionSub1Option'] = df['conditionSub1Option'].replace({np.nan: None})
            df['conditionSub2Option'] = df['conditionSub2Option'].replace({np.nan: None})

            #Converting unix time to date time
            #Coordinated Universal Time = True //instead of local time
            df['datetime'] = pd.to_datetime(df['ts'], unit='s', utc=True)

            #Dataset used is from korea
            df['datetime'] = df['datetime'].dt.tz_convert('Asia/Seoul')

            #accessing a single object to get the days date
            first_row = df.iloc[0]
            date = first_row["datetime"].strftime('%Y-%m-%d')
            
            #Figuring out where the actions stop
            df['activity_change'] = df['actionOption'] != df['actionOption'].shift(1)
            #conferting where the bolleans lie into unique numbered groups
            df['group_id'] = df['activity_change'].cumsum()

            dailyActivities = df.groupby(['actionOption', 'group_id']).agg(
                start_time=pd.NamedAgg(column='datetime', aggfunc='min'),
                end_time=pd.NamedAgg(column='datetime', aggfunc='max')

            ).reset_index()

            #calulate next day
            last_day = Day.objects.filter(user=request.user).aggregate(max_day=Max('days'))['max_day'] or 0
            day_num = last_day + 1
            days = Day.objects.create(user=request.user,
                                       days = day_num,
                                       date = date )

            #calculating duration of activity
            dailyActivities['duration'] = dailyActivities['end_time'] - dailyActivities['start_time']

            #sort activities in order
            dailyActivities = dailyActivities.sort_values(by='group_id')


            # interate through dataframe
            for index, row in dailyActivities.iterrows():

                duration_seconds = int(row['duration'].total_seconds())
                hours, remainder = divmod(duration_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                duration = time(hour=hours, minute=minutes, second=seconds)

                da = DailyActivity.objects.create(day=days,
                                            action = row['actionOption'],     
                                            startTime = row['start_time'],
                                            endTime = row['end_time'],                      
                                            duration = duration
                )
                
                
        
                for i in range(len(actions)):
                    
                    ##all entries per action
                    action_df = df[(df['group_id'] == row['group_id'])]
                    
                    #Group first before start/end time calc
                    action_df = action_df.groupby([actions[i]])

            
                    #create seperate df of durations of attributes within each activity
                    action_df = action_df.agg(
                                start_time=pd.NamedAgg(column='datetime', aggfunc='min'),
                                end_time=pd.NamedAgg(column='datetime', aggfunc='max')
                        ).reset_index()

                    action_df['duration'] = action_df['end_time'] - action_df['start_time']

                    for index2, row2 in action_df.iterrows():  
                        
                            duration_seconds = int(row['duration'].total_seconds())
                            hours, remainder = divmod(duration_seconds, 3600)
                            minutes, seconds = divmod(remainder, 60)
                            duration = time(hour=hours, minute=minutes, second=seconds)
                  
                            #as actions[i] cannot be declared in objects.create() directly
                            kwargs = {
                                'dailyActivity': da,
                                actions[i]: row2[actions[i]], 
                                'startTime': row2['start_time'],
                                'endTime': row2['end_time'],
                                'duration': duration
                            }
                        
                            models[i].objects.create(**kwargs)


            return Response({"message": "CSV file processed successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class DayView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    
    def get(self, request, *args, **kwargs):
        day = Day.objects.filter(user=request.user).order_by('date')
        serializer = DaySerializer(day, many=True)
        return Response(serializer.data)
    

class DailyActivityView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    
    def post(self, request, *args, **kwargs):
        date = request.data.get('date')

        action = request.data.get('action')

        date = str(date)
        
        #determining if date is year, year-month, year-month-day
        dateF=''
        if len(date) == 4:  # Year only
            dateF = '%Y'
        elif len(date) == 7 or len(date) == 6:  # Year and month
            dateF = '%Y-%m'
        elif len(date) == 10 or len(date) == 9 or len(date) == 8:  # Year, month, and day
            dateF = '%Y-%m-%d'
        

        ##Format date correctly
        startDate = datetime.strptime(date, dateF).date()
        
        ##Determine ranges
        if dateF == '%Y':
            endDate = datetime(startDate.year, 12, 31).date()
        elif dateF == '%Y-%m':
            if startDate.month == 12:
                endDate = datetime(startDate.year, 12, 31).date()
            else:
                endDate = datetime(startDate.year, startDate.month + 1, 1) - timedelta(days=1)
        else:  
            # Specific day
            endDate = startDate

        day = Day.objects.filter(user=request.user, date__range=(startDate, endDate))
        activities = DailyActivity.objects.filter(day__in=day).order_by('startTime')
    
        if(action == "action"):
            serializer = DailyActivitySerializer(activities, many=True)
            return Response(serializer.data)
        elif(action == "emotionTension"):
            emtionalTensionData = EmotionTension.objects.filter(dailyActivity__in=activities).order_by('startTime')
            serializer = EmotionTensionSerialiser(emtionalTensionData, many=True)
            return Response(serializer.data)
        elif(action == "emotionPositive"):
            emtionalPositiveData = EmotionPositive.objects.filter(dailyActivity__in=activities).order_by('startTime')
            serializer = EmotionPositiveSerialiser(emtionalPositiveData, many=True)
            return Response(serializer.data)
        elif(action == "travel"):
            SubOptionData = SubOption.objects.filter(dailyActivity__in=activities)
            serializer = SubOptionSerialiser(SubOptionData, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class DayViewForSurvey(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        day = Day.objects.filter(user=request.user).order_by('date')
        
        meridiemIndicator = request.data.get('meridiemIndicator')

        if(meridiemIndicator == "am"):
            # Filter days that have one associated SurveyAM
            days_with_am_survey = SurveyAM.objects.filter(day__in=day).values_list('day', flat=True)
            days_without_am_survey = day.exclude(pk__in=days_with_am_survey)
            serializer = DaySerializer(days_without_am_survey, many=True)
            return Response(serializer.data)
        elif(meridiemIndicator == "pm"):
            #Filter days that have one associated SurveyPM
            days_with_pm_survey = SurveyPM.objects.filter(day__in=day).values_list('day', flat=True)
            days_without_pm_survey = day.exclude(pk__in=days_with_pm_survey)
            serializer = DaySerializer(days_without_pm_survey, many=True)
            return Response(serializer.data)
        
        return Response({"error": "Invalid meridiemIndicator provided."}, status=400)

    
class SurveyPMUpload(APIView):
    #User authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        try:
            date = request.data.get('date')
            emotion = request.data.get('emotion')
            stress = request.data.get('stress')
            fatigue = request.data.get('fatigue')
            caffeine = request.data.get('caffeine')
            cAmount = request.data.get('cAmount')
            alcohol = request.data.get('alcohol')
            aAmount = request.data.get('aAmount')

            day = Day.objects.get(user=request.user, date=date)
        
        
            SurveyPM.objects.create(day=day,
                                    emotion = emotion,     
                                    stress = stress,
                                    fatigue = fatigue,                      
                                    caffeine = caffeine,
                                    cAmount = cAmount,
                                    alcohol = alcohol,                      
                                    aAmount = aAmount,
                )
            
            return Response({"message": "Survey successfully posted"}, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SurveyAMUpload(APIView):
    #User authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        try:
            date = request.data.get('date')
            sleep = request.data.get('sleep')
            sleepProblem = request.data.get('sleepProblem')
            dream = request.data.get('dream')
            condition = request.data.get('condition')
            emotion = request.data.get('emotion')

            day = Day.objects.get(user=request.user, date=date)
        
        
            SurveyAM.objects.create(day=day,
                                    sleep = sleep,     
                                    sleepProblem = sleepProblem,                      
                                    dream = dream,
                                    condition = condition,                      
                                    emotion = emotion,
                )
            
            return Response({"message": "Survey successfully posted"}, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


#Calulate hours in a duration
def timeConverterHours(timeObj):
    return timeObj.hour + timeObj.minute / 60 + timeObj.second / 3600

#Calulate minutes in a duration
def timeConverterMinutes(timeObj):
    return timeObj.hour * 60 + timeObj.minute + timeObj.second / 60
    
class ChronicIllnessParametersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def get(self, request, *args, **kwargs):
        try:
            days = Day.objects.filter(user=request.user).order_by('date')
            #default
            sleepTime = 0
            alcoholConsumedAprox = 0
            activeTime = 0
            smokingStatus = 'Never Smoker'
            age = request.user.age
            if(len(days) == 0):
                return Response({"age": age, "sleepAverage": sleepTime, "alcoholAverageAprox" : alcoholConsumedAprox, "activeTimeAverage" : activeTime , "smokingStatus" : smokingStatus})
            for day in days:
                #activities within a day
                activities = DailyActivity.objects.filter(day=day)
                # Sleeps within a day
                sleeps = DailyActivity.objects.filter(day=day,action=111).order_by('startTime')
                for sleep in sleeps:
                    #calulate the time spent sleeping in that day
                    sleepTime += timeConverterHours(sleep.duration)
                #get Active satus in that day
                activeStatuses  = Activity.objects.filter(dailyActivity__in=activities).order_by('startTime')
                for activityStatus in  activeStatuses:
                    actives = [1, 2, 7, 8]
                    for active in actives:
                        if(activityStatus.activity == active):
                            #Calulate time spent bing active in that day
                            activeTime += timeConverterMinutes(activityStatus.duration)
                try:
                    #In try as a surveyPM object may not exist however we use get as there is only one surveyPm object per day
                    drinks = SurveyPM.objects.get(day=day)
                    #If object exists
                    if drinks:
                        if drinks.alcohol != "":
                            percent = alcoholPerecent[drinks.alcohol]
                            alcoholConsumedAprox += drinks.aAmount * percent
                except:
                        #keeps status                
                        alcoholConsumedAprox += 0
            #average sleep time per day
            sleepAverage = sleepTime / len(days)
            #aproximate the alchol consumption per day
            alcoholAverageAprox = alcoholConsumedAprox  / len(days)
            #average time spent being active per day
            activeTimeAverage = activeTime / len(days)
            ##Get last entry
            lastDay = Day.objects.filter(user=request.user).order_by('date').last()
            #arbitrary time span
            thirtyDaysAgo = lastDay.date - timedelta(days=30)
            ##Get all days within the time frame from last entry
            lastThirtyDays = Day.objects.filter(user=request.user, date__range=(thirtyDaysAgo, lastDay.date))
            ##get all smokes within the time frame
            smokes = DailyActivity.objects.filter(day__in=lastThirtyDays,action=792).order_by('startTime')
            if smokes:
                ## Days where a smoke occured within time span
                distinct_smoking_days = smokes.values('startTime').distinct().count()
                if distinct_smoking_days ==len(lastThirtyDays):
                    #if smokes occured everyday with the last 30 days
                    smokingStatus = "Everyday Smoker"
                else:
                    #if smokes occured but not everyday with the last 30 days
                    smokingStatus = "Sometimes Smoker"
            else:
                #check all instances of smoking
                smokes = DailyActivity.objects.filter(day__in=days ,action=792).order_by('startTime')
                if smokes:
                    #If smoking has occured previously but not past 30 days
                    smokingStatus = "Former Smoker"
                else:
                    #if smoking has never occured
                    smokingStatus = "Never Smoker"
            return Response({"age": age, "sleepAverage": sleepAverage, "alcoholAverageAprox" : alcoholAverageAprox, "activeTimeAverage" : activeTimeAverage , "smokingStatus" : smokingStatus})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class ChronicIllnessFormatedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        try:
            sleepAverage = request.data.get('sleepAverage')
            alcoholAverageAprox = request.data.get('alcoholAverageAprox')
            activeTimeAverage = request.data.get('activeTimeAverage')
            smokingStatus = request.data.get('smokingStatus')
        

            ageFormated = ageConverter(request.user.age)
            sleepFormated = sleepConverter(sleepAverage)
            alcoholFormated = alcoholConverter(alcoholAverageAprox, request.user.gender)
            activeFormatted = activeConverter(activeTimeAverage)
            smokingFormatted = smokeConverter(smokingStatus)
        
            output = ageFormated + sleepFormated + alcoholFormated + activeFormatted + smokingFormatted
            return Response({"output": output})
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class IllnessDescriptionView(APIView):
    #User authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        try:
            shortCode = request.data.get('shortCode')
            
            ilness = Illness.objects.get(shortCode=shortCode)

            serializer = IllnessSerialiser(ilness)

            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
