from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    born_date = models.DateTimeField()
    born_location = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.full_name
