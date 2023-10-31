from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    member_since = models.DateField(auto_now_add=True, blank=False, null=False)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    