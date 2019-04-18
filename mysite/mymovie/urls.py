from django.urls import path

from . import views

app_name = 'mymovie'
urlpatterns = [
    path('', views.Homepage, name='homepage'),
    path('showmovie/', views.show, name='show'),
    path('showweather/', views.ShowWeather, name='weathershow'),
]