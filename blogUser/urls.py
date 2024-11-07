from django.urls import path
from blogUser.views import newUser, userInfo, editUser, editUserPassword

app_name = 'blogUser'

urlpatterns = [
    path('user/', userInfo, name='info'),
    path('user/create/', newUser, name='create'),
    path('user/edit/', editUser, name='edit'),
    path('user/edit/password', editUserPassword, name='editPassword'),
    ]