from django.urls import path,include
from . import views



urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.sign_up, name="registration"),
    path('signup/password', views.sign_up_password, name='uppassword'),
    path('login', views.user_login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),


    path('rest_auth/', include('rest_auth.urls')),
    path('rest_auth/registration/', include('rest_auth.registration.urls'))   
]