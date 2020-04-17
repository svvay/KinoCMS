from django.urls import path
from .views import Movie, MoviesDetailViews, ActiveMovies, MoviesViews, CinemaViews, NewsDetail

urlpatterns = [
    path('', MoviesViews.as_view(), name='movies'),
    path('<slug:slug>/', MoviesDetailViews.as_view(), name='movie'),
    path('placard', ActiveMovies.as_view(), name='placard'),
    path('cinema', CinemaViews.as_view(), name='cinema'),
    path('#', NewsDetail.as_view(), name='news'),
]
