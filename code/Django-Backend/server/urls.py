"""sensor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings  
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('life_lens.urls', namespace='life_lens')),
    path('', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('auth/', include('djoser.urls')), 
    path('auth/', include('djoser.urls.jwt')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



#Proceseses urls not matched by other patterns
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]