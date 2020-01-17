from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('', views.signup, name='signup'),
]
