from django.db import models
from django.contrib.auth.models import User

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)  # 'user' ou 'admin'

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Category(models.Model):
    name = models.CharField(max_length=100)  # Nom de la catégorie

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)  # Titre du film
    description = models.TextField()  # Description détaillée du film
    release_date = models.DateField()  # Date de sortie du film
    image = models.ImageField(upload_to='movies/')  # Champ pour l'image du film
    youtube_url = models.URLField()  # URL de la bande-annonce ou du film sur YouTube
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création du film, ajoutée automatiquement
    updated_at = models.DateTimeField(auto_now=True)  # Date de dernière mise à jour du film, mise à jour automatiquement
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # L'utilisateur qui a créé le film
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Lien vers la catégorie

    def __str__(self):
        return self.title
