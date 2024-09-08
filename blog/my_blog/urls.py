from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='home'),
    path('blog/<pk>/',views.blog ,name='blog'),
    path('creat/',views.creat ,name='creat'),
    path('admin/',views.admin ,name='admin'),
    path('delete/<pk>/',views.delet,name='delete'),
    path('update/<pk>/',views.updata,name='updata'),
]