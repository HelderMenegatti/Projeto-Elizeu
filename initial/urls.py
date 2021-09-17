from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.sign_up, name="registro"),
    path('rest_auth/', include('rest_auth.urls')),
    path('rest_auth/registration/', include('rest_auth.registration.urls'))
]