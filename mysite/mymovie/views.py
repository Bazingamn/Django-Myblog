from django.shortcuts import render
from django.http import HttpResponse
from mymovie import models
from django.core.paginator import Paginator
from django.views import generic


def Homepage(request):
    return render(request, 'mymovie/index.html')


def show(request):
    mylist = models.Movies.objects.all()
    paginator = Paginator(mylist, 25)

    page = request.GET.get('page')
    p_movie = paginator.get_page(page)
    return render(request, 'mymovie/showlist.html', {'p_movie': p_movie})


def ShowWeather(request):
    weatherList = models.Weathers.objects.all()
    return render(request, 'mymovie/weathershow.html', {'weatherlist': weatherList})