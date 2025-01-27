from django.db import models
from django.utils import timezone

# Create your models here.

# id (primary key)
# first_name (string), last_name (string), phone (string), email (email)
# created_date (date), description (text), category (foreign key), 
# show (boolean), owner (foreign key), picture (imagem)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    desciption = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
        
    