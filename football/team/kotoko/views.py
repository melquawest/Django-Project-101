from django.shortcuts import render
from .models import Player
from .forms import AddPlayerInput
from django.http import HttpResponse

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


def add_player(request):
    if (request.method == 'POST'):
        player = AddPlayerInput(request.POST or None)
        if (player.is_valid()):
            first_name = player.cleaned_data['first_name'] # receives data from the form as dict
            last_name = player.cleaned_data['last_name']
            address = player.cleaned_data['address']
            email = player.cleaned_data['email']
            member_since = player.cleaned_data['member_since']
            
            newPlayer = Player.objects.create(
                first_name=first_name,
                last_name=last_name,
                address=address,
                email=email,
                member_since=member_since
            )
            newPlayer.save()
        
    player = AddPlayerInput()
    context = {
        'form': player
    }
    return render(request, 'add_player.html', context)