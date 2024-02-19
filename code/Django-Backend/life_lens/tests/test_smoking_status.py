from users.models import UserAccount
from life_lens.models import Day, DailyActivity
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class TestSmokingStatus(APITestCase):

    def setUp(self):
        
        #Never Somker
        self.never_smoker = UserAccount.objects.create_user(
            email='neversmoker@gmail.com',
            password='safepassword123',
            name='Never Smoker',
            age=18,
            gender=0
        )

        #Former Smoker
        self.former_smoker = UserAccount.objects.create_user(
            email='formersmoker@gmail.com',
            password='safepassword123',
            name='Former Smoker',
            age=18,
            gender=0
        )

        #Sometimes Smoker
        self.sometimes_smoker = UserAccount.objects.create_user(
            email='sometimessmoker@gmail.com',
            password='safepassword123',
            name='Sometimes smoker',
            age=18,
            gender=0
        )

        #Everyday Smoker
        self.everyday_smoker = UserAccount.objects.create_user(
            email='everydaysmoker@gmail.com',
            password='safepassword123',
            name='Everday Somker',
            age=18,
            gender=0
        )

        self.NStoken = RefreshToken.for_user(self.never_smoker)
        self.FStoken = RefreshToken.for_user(self.former_smoker)
        self.SStoken = RefreshToken.for_user(self.sometimes_smoker)
        self.EStoken = RefreshToken.for_user(self.everyday_smoker)
         
     
        #Most recent day
        self.most_recent_day_NS = Day.objects.create(
            user = self.never_smoker,
            date = '2024-02-23', 
            days = 1
        )

        #Most recent day
        self.most_recent_day_FS = Day.objects.create(
            user = self.former_smoker,
            date = '2024-02-23', 
            days = 2
        )

        #Most recent day
        self.most_recent_day_SS = Day.objects.create(
            user = self.sometimes_smoker,
            date = '2024-02-23', 
            days = 3
        )

        #Most recent day
        self.most_recent_day_ES = Day.objects.create(
            user = self.everyday_smoker,
            date = '2024-02-23', 
            days = 4
        )

        #Most recent day
        self.last_smoke_day_FS = Day.objects.create(
            user = self.former_smoker,
            date = '2024-01-01', 
            days = 5
        )

        self.day_without_smoke_SS = Day.objects.create(
            user = self.sometimes_smoker,
            date = '2024-02-20', 
            days = 6
        )

        #Sometimes smoker seen smoking on last day updated however not seen smoking 3 days before so sometimes smoker
        self.last_smoke_fs = DailyActivity.objects.create(
            day = self.most_recent_day_SS,
            action = 792,  #smoking
            startTime = '2024-02-23 14:00',
            endTime = '2024-02-23 14:29 ',
            duration = '00:29:00'
        )

        #Sveryday smoker seen smoking for everyone of there day objects
        self.last_smoke_day_ES = DailyActivity.objects.create(
            day = self.most_recent_day_ES,
            action = 792,  #smoking
            startTime = '2024-02-23 14:00',
            endTime = '2024-02-23 14:29 ',
            duration = '00:29:00'
        )

        #Former smoker seen smoking in the previous month before there most recent day entry
        self.Last_Smoke_FS = DailyActivity.objects.create(
            day = self.last_smoke_day_FS,
            action = 792,  #smoking
            startTime = '2024-01-01 14:00',
            endTime = '2024-01-01 14:29 ',
            duration = '00:29:00'
        )



    def test_smoking_status_calculations(self):
        endPoint = reverse('life_lens:chronic_illness_parameters_view')

        #Getting Auth credetials for Former Smoker
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.FStoken.access_token}')
        response = self.client.get(endPoint)
        formerSmoker = response.json()['smokingStatus']
        
        #Getting Auth credetials for Everday Smoker Smoker
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.EStoken.access_token}')
        response = self.client.get(endPoint)
        everydaySmoker = response.json()['smokingStatus']

        #Getting Auth credetials for Never Smoker
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.NStoken.access_token}')
        response = self.client.get(endPoint)
        neverSmoker = response.json()['smokingStatus']

        #Getting Auth credetials for Sometimes Smoker
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.SStoken.access_token}')
        response = self.client.get(endPoint)
        sometimesSmoker = response.json()['smokingStatus']


        self.assertEqual(formerSmoker, "Former Smoker", "The former smoker status does not match.")
        self.assertEqual(everydaySmoker, "Everyday Smoker", "The everyday smoker status does not match.")
        self.assertEqual(neverSmoker, "Never Smoker", "The never smoker status does not match.")
        self.assertEqual(sometimesSmoker, "Sometimes Smoker", "The sometimes smoker status does not match.")
