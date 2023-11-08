from django.contrib import admin
from .models import Staff

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'email',
        'role',
        'nationality'
    )


admin.site.register(Staff, StaffAdmin)