from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  CurrentUserView 

app_name = 'users'

router = DefaultRouter()

urlpatterns = [
    path('current_user/', CurrentUserView.as_view(), name='current_user'),
    path('', include(router.urls)),
]