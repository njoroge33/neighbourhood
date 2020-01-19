from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.signup, name='signup'),
    re_path(r'login/', LoginView.as_view(), name='login'),
    re_path(r'^profile/', views.profile, name='profile'),
    re_path(r'^updateprofile/', views.update_profile, name='update_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

