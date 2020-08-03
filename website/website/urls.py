"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from webapp import views
import requests

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),

    #this loads views.py
    path('', views.home, name='home'),
    path('emailchecker/', views.pwned, name='pwned'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secinfohome/',views.info, name='info'),
    path('secinfohome/passwordpage', views.passwordpage, name='passwordpage'),
    path('secinfohome/wfhpage', views.wfhpage, name='wfhpage'),
    path('secinfohome/attackpage', views.attackpage, name='attackpage'),
    path('secinfohome/preventionpage', views.preventionpage, name='preventionpage'),
    path('secinfohome/securitypage', views.securitypage, name='securitypage'),
    path('secinfohome/detectionpage', views.detectionpage, name='detectionpage'),
    path('secinfohome/netsecuritypage', views.netsecuritypage, name='netsecuritypage'),
    path('secinfohome/policypage', views.policypage, name='policypage'),
    path('secinfohome/aboutuspage', views.aboutuspage, name='aboutuspage'),
    path('game/', views.game, name='game'),

]
