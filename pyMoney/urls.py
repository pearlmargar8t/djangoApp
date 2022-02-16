from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/send_money', views.send_money)
]
