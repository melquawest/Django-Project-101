from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.hearts_home, name='home'),
    path('add/', views.add_staff, name='add-staff' ),
    path('list/', views.list_staff, name='staff-list')
]
