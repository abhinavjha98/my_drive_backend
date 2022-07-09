from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url 
from account.views import UserAuthView, UserAuthenticateView

urlpatterns = [
    path('user/profession/', UserAuthView.as_view({'get': 'get_profession'})),
    path('login/',UserAuthView.as_view({'post': 'login'})),
    path('signup/',UserAuthView.as_view({'post': 'signup'})),
    
    path('user/update/',UserAuthenticateView.as_view({'post':'update_profile'})),
    path('user/update/profile/',UserAuthenticateView.as_view({'post':'update_profile_image'})),
    path('user/myprofile/',UserAuthenticateView.as_view({'get':'get_user_profile'})),
]
