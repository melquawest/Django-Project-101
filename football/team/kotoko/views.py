from django.shortcuts import render
from .models import Player

# Create your views here.
def welcome_section(request):
    return render(request, 'index.html')


def list_players(request):
    player = Player.objects.values()
    context = {
        'object': player
    }
    return render(request, 'players.html', context)


def about_player(request, id):
    player = Player.objects.get(id=id)
    context = {
        'object': player
    }
    return render(request, 'about.html', context)
