from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, MoviShots, Cinema, News


class MoviesViews(ListView):
    """ Вывод всех фильмов """
    model = Movie
    queryset = Movie.objects.all()
    template_name = 'movie/movies.html'


class ActiveMovies(View):
    """Вывод фильмов в прокате"""

    def get(self, request):
        placard = Movie.objects.filter(is_active=True)
        return render(request, 'movie/active_movies.html', {'placard_list': placard})


class MoviesDetailViews(DetailView):
    """ Описание фильма"""
    model = Movie
    slug_field = 'url'
    template_name = 'movie/movie_detail.html'


class CinemaViews(View):
    """Вывод кинотеатров"""

    def get(self, request):
        cinemas = Cinema.objects.all()
        return render(request, 'cinema/cinema.html', {'cinemas_list': cinemas})


class NewsDetail(View):
    """ Вывод новостей в кинотеатре"""

    def get(self, request, pk):
        news = Cinema.objects.get(id=pk)
        return render(request, 'cinema/news.html', {'news_list': news})
