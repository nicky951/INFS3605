from django.urls import path

from . import views

urlpatterns = [
    path('nextpage', views.index, name='index'),
    path('', views.testhtml, name='testhtml')
]