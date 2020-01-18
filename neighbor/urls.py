from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.signup, name='signup'),
    re_path(r'login/', LoginView.as_view(), name='login'),
]
