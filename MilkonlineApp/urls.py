from django.urls import path, include
from . import views

app_name='MilkonlineApp'
urlpatterns=[
    path('', views.index, name='index'),

]
