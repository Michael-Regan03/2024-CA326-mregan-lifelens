from users.models import UserAccount
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

class TestUrls(APITestCase):

    def setUp(self):
        
        #Creating user for testing
        self.twentys = UserAccount.objects.create_user(
            email='twentys@gmail.com',
            password='safepassword123',
            name='Twentys',
            age=25,
            gender=0
        )

        self.thirties = UserAccount.objects.create_user(
            email='thirties@gmail.com',
            password='safepassword123',
            name='Thirties',
            age=35,
            gender=0
        )

        self.forties = UserAccount.objects.create_user(
            email='forties@gmail.com',
            password='safepassword123',
            name='Forties',
            age=45,
            gender=0
        )

        self.fifties = UserAccount.objects.create_user(
            email='fifties@gmail.com',
            password='safepassword123',
            name='Fifties',
            age=55,
            gender=0
        )

        self.sixties = UserAccount.objects.create_user(
            email='sixties@gmail.com',
            password='safepassword123',
            name='Sixties',
            age=65,
            gender=0
        )

        self.seventies = UserAccount.objects.create_user(
            email='seventies@gmail.com',
            password='safepassword123',
            name='Seventies',
            age=75,
            gender=0
        )

        self.eighty_plus = UserAccount.objects.create_user(
            email='eighty_plus@gmail.com',
            password='safepassword123',
            name='Eighty Plus',
            age=95,
            gender=0
        )

        

        self.twentys_token = RefreshToken.for_user(self.twentys)
        self.thirties_token = RefreshToken.for_user(self.thirties)
        self.forties_token = RefreshToken.for_user(self.forties)
        self.fifties_token = RefreshToken.for_user(self.fifties)
        self.sixties_token = RefreshToken.for_user(self.sixties)
        self.seventies_token = RefreshToken.for_user(self.seventies)
        self.eighty_plus_token = RefreshToken.for_user(self.eighty_plus)

         

    def test_daily_activity_view(self):
        endPoint = reverse('life_lens:chronic_formated_view')
       
        #Creating json object

        expectedResult =   [[1,0,0,0,0,0,0] + [1,0,0,0] + [1] + [1] + [1,0,0,0],
                            [0,1,0,0,0,0,0] + [1,0,0,0] + [1] + [1] + [1,0,0,0], 
                            [0,0,1,0,0,0,0] + [0,1,0,0] + [1] + [1] + [0,1,0,0] ,
                            [0,0,0,1,0,0,0] + [0,1,0,0] + [1] + [1] + [0,1,0,0],
                            [0,0,0,0,1,0,0] + [0,0,1,0] + [0] + [0] + [0,0,1,0],
                            [0,0,0,0,0,1,0] + [0,0,1,0] + [0] + [0] + [0,0,1,0],
                            [0,0,0,0,0,0,1] + [0,0,0,1] + [0] + [0] + [0,0,0,1] ]


        sleepAverages = ["2", "2", "6", "6", "9", "9", "13"]
        alcoholConsumption = ["100", "100", "100", "100", "0", "0", "0"]
        smokingStatuses = ["Everyday Smoker", "Everyday Smoker", "Sometimes Smoker", "Sometimes Smoker", "Former Smoker","Former Smoker","Never Smoker"]

        tokens = [self.twentys_token.access_token, self.thirties_token.access_token, self.forties_token.access_token, self.fifties_token.access_token, self.sixties_token.access_token,
                    self.seventies_token.access_token, self.eighty_plus_token.access_token]


        for i in range(7):
            payLoad = {
                "sleepAverage": sleepAverages[i],
                "alcoholAverageAprox" : alcoholConsumption[i],
                "activeTimeAverage":  alcoholConsumption[i],
                "smokingStatus" : smokingStatuses[i],
            } 
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens[i]}')
            response = self.client.post(endPoint, payLoad, format='json')
            result = response.json()['output']
            self.assertEqual(result, expectedResult[i], "Error in Conversion") 

