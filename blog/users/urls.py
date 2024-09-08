from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginform , name='login')
]