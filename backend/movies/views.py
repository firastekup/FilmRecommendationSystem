# backend/movies/views.py

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import generics
from .models import Movie, User  # Assurez-vous d'importer le modèle User
from .serializers import MovieSerializer, UserSerializer  # Assurez-vous d'importer UserSerializer
from rest_framework.exceptions import PermissionDenied

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Vérifie le rôle de l'utilisateur avant d'ajouter un film
        if self.request.user.userrole.role == 'admin':
            serializer.save(created_by=self.request.user)
        else:
            raise PermissionDenied("Vous n'avez pas la permission d'ajouter un film.")

    def perform_destroy(self, instance):
        # Vérifie le rôle de l'utilisateur avant de supprimer un film
        if self.request.user.userrole.role == 'admin':
            instance.delete()  # Supprime l'instance
        else:
            raise PermissionDenied("Vous n'avez pas la permission de supprimer ce film.")

# Ajoutez la vue RegisterView
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
