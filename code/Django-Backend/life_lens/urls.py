from django.urls import path, include
from .views import  DailyActivitiesCSVUpload
""" from rest_framework import routers
from . import views """

app_name = 'life_lens'

""" router = routers.DefaultRouter()
 """
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/upload-csv/', DailyActivitiesCSVUpload.as_view(), name='api_daily_activity_upload_csv'),
]