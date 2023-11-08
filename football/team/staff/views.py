from django.shortcuts import render
from .forms import StaffForm
from .models import Staff



# Create your views here.
def hearts_home(request):
    return render(request, 'base.html')


def add_staff(request):
    form = StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StaffForm()
    
    context = {
        'form': form
    }
    return render(request, 'add-staff.html', context)


def list_staff(request):
    staff = Staff.objects.values()
    context = {
        'staff': staff
    }
    return render(request, 'staff.html', context)