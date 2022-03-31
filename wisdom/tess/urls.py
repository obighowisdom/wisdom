from django.urls import path
from . import views
app_name = 'tessurl'

urlpatterns = [
    path('', views.hello, name = 'index'),
    path('mission/', views.work, name = 'mission'),
    path('getinvolved/', views.join, name = 'getinvolved'),
    path('gallery/', views.myblog, name = 'gallery'),
    path('donate/', views.don, name = 'donate'),
    path('home/', views.myhome, name = 'home'),
    path('media/', views.mymedia, name = 'media'),
]