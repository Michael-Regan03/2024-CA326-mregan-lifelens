from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CSVUploadSerializer, DailyActivitySerializer, DaySerializer
from .models import DailyActivities, Day
from life_lens.lifelogDataMapping import mealAmountMapping, transportMapping
from django.db.models import Max
import pandas as pd
import numpy as np


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
            
            
            df.loc[df['actionSubOption'] == 'meal_amount', 'actionSub'] = df.loc[df['actionSubOption'] == 'meal_amount', 'actionSub'].map(mealAmountMapping)
            df.loc[df['actionSubOption'] == 'move_method', 'actionSub'] = df.loc[df['actionSubOption'] == 'move_method', 'actionSub'].map(transportMapping)
            
            #resolving NaN error for nullable attributes
            df['conditionSub1Option'] = df['conditionSub1Option'].replace({np.nan: None})
            df['conditionSub2Option'] = df['conditionSub2Option'].replace({np.nan: None})

            #calulate next day
            last_day = Day.objects.filter(user=request.user).aggregate(max_day=Max('days'))['max_day'] or 0
            day_num = last_day + 1
            days = Day.objects.create(user=request.user,
                                       days = day_num )

            # interate through dataframe
            for index, row in df.iterrows():
                DailyActivities.objects.create(
                    day=days,
                    ts=float(row['ts']),
                    action=row['action'],
                    actionOption=int(row['actionOption']),
                    actionSub=row.iloc[3] if row['actionSub'] else None,
                    actionSubOption=float(row['actionSubOption']) if row['actionSubOption'] else None,
                    condition=row['condition'],
                    conditionSub1Option=float(row['conditionSub1Option']) if row['conditionSub1Option'] else None,
                    conditionSub2Option=float(row['conditionSub2Option']) if row['conditionSub2Option'] else None,
                    place=row['place'],
                    emotionPositive=int(row['emotionPositive']),
                    emotionTension=int(row['emotionTension']),
                    activity=int(row['activity']),
                ) 

            return Response({"message": "CSV file processed successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DailyActivitiesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    
    def post(self, request, *args, **kwargs):
        days = request.data.get('days')

        try:
            days = int(days)  
        except ValueError:
            return Response({'error': 'Invalid days'}, status=400)

        day = Day.objects.filter(user=request.user, days=days)
        activities = DailyActivities.objects.filter(day__in=day)


        serializer = DailyActivitySerializer(activities, many=True)

        return Response(serializer.data)
    
class DayView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    
    def get(self, request, *args, **kwargs):
        day = Day.objects.filter(user=request.user)
        serializer = DaySerializer(day, many=True)
        return Response(serializer.data)
    
