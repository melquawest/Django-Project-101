from django.contrib import admin
from .models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'email', 'member_since')

admin.site.register(Player, PlayerAdmin)
