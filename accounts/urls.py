from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('send_login_email', views.send_login_email, name='send_login_email'),
]