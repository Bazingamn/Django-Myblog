from django.urls import path

from . import views

app_name = 'mymovie'
urlpatterns = [
    path('', views.ShowScrapeData, name='scrapedata'),
    path('showmovie/', views.show, name='show'),
    path('showweather/', views.ShowWeather, name='weathershow'),
    path('showphone/', views.ShowPhone, name='phoneshow'),
]