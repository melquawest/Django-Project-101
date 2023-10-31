from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.welcome_section, name='home'),
    path('players/', views.list_players, name='players'),
    path('home/', views.welcome_section, name='master'),
    path('about/<int:id>', views.about_player, name='about')
]
