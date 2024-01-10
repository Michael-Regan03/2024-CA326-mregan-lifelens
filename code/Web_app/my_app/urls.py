from django.urls import path, include
from .views import  DailyActivitiesCSVUpload
from rest_framework import routers

app_name = 'my_app'

router = routers.DefaultRouter()

router.register('sensorData', SensorDataViewSet, basename="sensorData" ) 

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/upload-csv/', DailyActivitiesCSVUpload.as_view(), name='api_daily_activity_upload_csv'),
]