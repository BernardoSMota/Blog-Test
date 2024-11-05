from django.urls import path
from blogUser.views import newUser

app_name = 'blogUser'

urlpatterns = [
    path('user/create/', newUser, name='create'),
    ]