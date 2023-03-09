from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('send_mail', views.sendmail, name='mail')
]