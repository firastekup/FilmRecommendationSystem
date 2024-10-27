# movies/models.py

from django.db import models
from django.contrib.auth.models import User

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)  # 'user' ou 'admin'

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title
