from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from .views import registration_view, login_view

urlpatterns = [
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('placard')), name='logout'),
]
