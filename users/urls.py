from django.urls import path
from .views import UserList, RegisterUser

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('register/', RegisterUser.as_view(), name='user-register'),
]
