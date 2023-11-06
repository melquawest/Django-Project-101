from django.shortcuts import render



def hearts_home(request):
    return render(request, 'base.html')
# Create your views here.
