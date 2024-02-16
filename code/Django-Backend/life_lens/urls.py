from django.urls import path, include
from .views import  DailyActivitiesCSVUpload, DayView, DailyActivityView, DayViewForSurvey, SurveyPMUpload, SurveyAMUpload, ChronicIllnessParametersView, ChronicIllnessFormatedView
from rest_framework import routers 

app_name = 'life_lens'

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/upload-csv/', DailyActivitiesCSVUpload.as_view(), name='api_daily_activity_upload_csv'), 
    path('daily-activity-data/', DailyActivityView.as_view(), name='daily_activities'),
    path('day/', DayView.as_view(), name='daily_activities'),
    path('day-without-survey/', DayViewForSurvey.as_view(), name='day_without_survey'), 
    path('survey-pm-upload/', SurveyPMUpload.as_view(), name='survey-pm-upload'), 
    path('survey-am-upload/', SurveyAMUpload.as_view(), name='survey-am-upload'),
    path('chronic-illness-parameters-view/', ChronicIllnessParametersView.as_view(), name='chronic-illness-parameters-view'),
    path('chronic-illness-formated-view/', ChronicIllnessFormatedView.as_view(), name='chronic-formated-view'),        
]