from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('send_money/', views.send_money),
    path('login/', views.login_user, name="login"),

]
