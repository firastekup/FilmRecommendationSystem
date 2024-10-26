# backend/movies/models.py

from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    video_url = models.URLField()  # URL vers la vidéo

    def __str__(self):
        return self.title

# Ajoutez un modèle pour stocker les rôles
class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)  # Par exemple, 'admin' ou 'user'
