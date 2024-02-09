from django.urls import path, include
from .views import  DailyActivitiesCSVUpload, DailyActivitiesView, DayView
from rest_framework import routers 

app_name = 'life_lens'

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/upload-csv/', DailyActivitiesCSVUpload.as_view(), name='api_daily_activity_upload_csv'), 
    path('daily-activity-data/', DailyActivitiesView.as_view(), name='daily_activities'),
    path('day/', DayView.as_view(), name='daily_activities'),    
]