from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie

# Obtention du modèle User (vous pouvez remplacer par votre modèle utilisateur si nécessaire)
User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'description', 'video_url', 'created_by']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Utiliser le modèle utilisateur
        fields = ['id', 'username', 'email']  # Ajoutez les champs que vous souhaitez exposer
