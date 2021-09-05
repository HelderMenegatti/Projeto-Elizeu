from django.urls import path
from . import views

urlpatterns = [
    path('singup/', views.sing_up, name="singup"),
]