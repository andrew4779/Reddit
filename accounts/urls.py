from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('', views.loginview, name='login'),
    path('', views.logoutview, name='logout'),
]
