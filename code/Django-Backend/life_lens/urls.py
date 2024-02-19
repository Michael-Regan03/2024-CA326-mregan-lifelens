from django.urls import path, include
from .views import  DailyActivitiesCSVUpload, DayView, DailyActivityView, DayViewForSurvey, SurveyPMUpload, SurveyAMUpload, ChronicIllnessParametersView, ChronicIllnessFormatedView, IllnessDescriptionView
from rest_framework import routers 

app_name = 'life_lens'

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/upload-csv/', DailyActivitiesCSVUpload.as_view(), name='upload_csv'), 
    path('daily-activity-view/', DailyActivityView.as_view(), name='daily_activity_view'),
    path('day/', DayView.as_view(), name='day'),
    path('day-without-survey/', DayViewForSurvey.as_view(), name='day_without_survey'), 
    path('survey-pm-upload/', SurveyPMUpload.as_view(), name='survey_pm_upload'), 
    path('survey-am-upload/', SurveyAMUpload.as_view(), name='survey_am_upload'),
    path('chronic-illness-parameters-view/', ChronicIllnessParametersView.as_view(), name='chronic_illness_parameters_view'),
    path('chronic-illness-formated-view/', ChronicIllnessFormatedView.as_view(), name='chronic_formated_view'), 
    path('illness-description-view/', IllnessDescriptionView.as_view(), name='illness_description_view'), 
    
]