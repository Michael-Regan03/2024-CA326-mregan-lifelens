from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  CurrentUserView 

app_name = 'users'

router = DefaultRouter()
router.register(r'current_user', CurrentUserView, basename='current_user')

urlpatterns = [
    path('', include(router.urls)),
]