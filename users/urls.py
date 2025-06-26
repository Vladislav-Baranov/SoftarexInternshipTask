from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.UsersLogin.as_view(), name='login'),
    path('logout/', views.UsersLogout.as_view(), name='logout'),
    path('register/', views.UsersRegister.as_view(), name='register'),
    path('profile/', views.UsersProfile.as_view(), name='profile'),
    path('password-change', views.UsersPasswordChange.as_view(), name='password-change'),
    path('password-change/done/', views.UsersPasswordChangeDone.as_view(), name='password-change-done')
]
