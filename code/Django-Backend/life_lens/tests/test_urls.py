from users.models import UserAccount
from life_lens.models import Day, DailyActivity, SubOption, Condition,ConditionSub1Option, ConditionSub2Option, Place, EmotionPositive, EmotionTension, Activity
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.conf import settings

class TestUrls(APITestCase):

    def setUp(self):
        
        
        #Testing Creating Objects

        #Creating user for testing
        self.test_user = UserAccount.objects.create_user(
            email='test@gmail.com',
            password='safepassword',
            name='Test User',
            age=18,
            gender=0
        )

        self.token = RefreshToken.for_user(self.test_user)
         
        #Creating Day for testing
        self.test_day = Day.objects.create(
            user = self.test_user,
            date = '2020-09-01', 
            days = 1
        ) 
        
        
        #Creating Activity for testing
        self.test_activity = DailyActivity.objects.create(
            day = self.test_day,
            action = 86,  #Travel related to participation and volunteering
            startTime = '2020-09-01 14:00',
            endTime = '2020-09-01 14:29 ',
            duration = '00:29:00'
        )
 
        self.test_sub_option = SubOption.objects.create(
            dailyActivity = self.test_activity,
            actionSubOption = 'driving',  
            startTime = '2020-09-01 14:00',
            endTime = '2020-09-01 14:29 ',
            duration = '00:29:00'
        )

        self.test_condition = Condition.objects.create(
            dailyActivity = self.test_activity,
            condition = 'WITH_ONE',  
            startTime = '2020-09-01 14:00',
            endTime = '2020-09-01 14:29 ',
            duration = '00:29:00'
        )

        self.test_condition_sub_1_option = ConditionSub1Option.objects.create(
            dailyActivity = self.test_activity,
            conditionSub1Option =  1,   #with-families
            startTime = '2020-09-01 14:00',
            endTime = '2020-09-01 14:29 ',
            duration = '00:29:00'
        )

        self.test_condition_sub_2_option = ConditionSub2Option.objects.create(
            dailyActivity = self.test_activity,
            conditionSub2Option =  2, #moderate participation in conversation 
            startTime = '2020-09-01 14:00',
            endTime = '2020-09-01 14:10 ',
            duration = '00:10:00'
        )

        self.test_place = Place.objects.create(
            dailyActivity = self.test_activity,
            place =  'outdoor', 
            startTime = '2020-09-01 14:00',
            endTime = '2020-09-01 14:29 ',
            duration = '00:29:00'
        )


        self.test_emotion_positive = EmotionPositive.objects.create(
            dailyActivity = self.test_activity,
            emotionPositive  =  2, 
            startTime = '2020-09-01 14:00',
            endTime = '2020-09-01 14:01 ',
            duration = '00:01:00'
        )

        self.test_emotion_tension = EmotionTension.objects.create(
            dailyActivity = self.test_activity,
            emotionTension  =  3, 
            startTime = '2020-09-01 14:00',
            endTime = '2020-09-01 14:05 ',
            duration = '00:05:00'
        )

        self.test_activity = Activity.objects.create(
            dailyActivity = self.test_activity,
            activity  =  0, # IN_VEHICLE
            startTime = '2020-09-01 14:00',
            endTime = '2020-09-01 14:29 ',
            duration = '00:29:00'
        )



    def test_csv_upload(self):
        #Getting Auth credetials for API
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        #Getting file path
        csvFilePath = os.path.join(settings.BASE_DIR, 'life_lens', 'tests', 'test.csv')
        with open(csvFilePath, 'rb') as csv_file:
            file_data = csv_file.read()
        testFile = SimpleUploadedFile("test.csv", file_data, content_type="text/csv")
        payload = {'file': testFile }
        endPoint = reverse('life_lens:upload_csv')
        response = self.client.post(endPoint, payload)
        self.assertEqual(response.status_code, 201) #Object creation successful



    def test_day(self):
        #Getting Auth credetials for API
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        endPoint = reverse('life_lens:day')
        response = self.client.get(endPoint)
        date = response.json()[0]['date']
        self.assertEqual(response.status_code, 200) #200 access granted
        self.assertEqual(date,'2020-09-01' , "Getting dates") #Getting all dates


    def test_current_user(self):
        #Getting Auth credetials for API 
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}') 
        endPoint = reverse('users:current_user')
        response = self.client.get(endPoint)
        id = response.json()['id']
        name = response.json()['name']
        email = response.json()['email']
        self.assertEqual(response.status_code, 200)#200 access granted
        self.assertEqual(id, 1, "Error with user ID")
        self.assertEqual(name, 'Test User', 'Error with user Name')
        self.assertEqual(email, 'test@gmail.com', 'Error with email address')


    def test_daily_activity_view(self):
        #Getting Auth credetials for API 
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        #Creating json object
        payLoad = {
            "date": "2020-09-01",
            "action" : "action"
        }
        endPoint = reverse('life_lens:daily_activity_view')
        response = self.client.post(endPoint, payLoad, format='json')
        self.assertEqual(response.status_code, 200) #access granted


    def test_survey_am_upload(self):
        #Getting Auth credetials for API 
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        #Creating json object    
        payLoad = {
            "date": "2020-09-01" ,
            "sleep" : "1" , #Not at all
            "sleepProblem" : "1", #It took more than 30 minutes to fall asleep.
            "dream" : "1" , #Nightmare
            "condition": "1", #Not at all
            "emotion" : "1"  #Very unpleasant
        }
        endPoint = reverse('life_lens:survey_am_upload')
        response = self.client.post(endPoint, payLoad, format='json')
        self.assertEqual(response.status_code, 201)


    def test_survey_pm_upload(self):
        #Getting Auth credetials for API 
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        #Creating json object        
        payLoad = {
            "date": "2020-09-01" ,
            "emotion" : "1" , #Very plesant,
            "stress" : "1", # Very plesant
            "fatigue" : "1" , #Very much
            "caffeine": "red-bull",
            "cAmount" : "100" ,
            "alcohol": "1",
            "aAmount" : "100",
        }
        endPoint = reverse('life_lens:survey_pm_upload')
        response = self.client.post(endPoint, payLoad, format='json')
        self.assertEqual(response.status_code, 201)



