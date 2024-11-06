from django.urls import path
from blogUser.views import newUser, userInfo

app_name = 'blogUser'

urlpatterns = [
    path('user/', userInfo, name='info'),
    path('user/create/', newUser, name='create'),
    ]