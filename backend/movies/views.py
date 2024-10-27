# movies/views.py

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserRole

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        role = request.data.get('role')

        if not username or not password or not email:
            return Response({"error": "Nom d'utilisateur, mot de passe et email sont obligatoires."}, status=status.HTTP_400_BAD_REQUEST)

        if role not in ['user', 'admin']:
            return Response({"error": "Rôle non valide. Utilisez 'user' ou 'admin'."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user_role = UserRole.objects.create(user=user, role=role)
            return Response({"message": "Utilisateur créé avec succès."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Nom d'utilisateur ou mot de passe incorrect."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user_role = user.userrole  # Cela peut lever une exception si userrole n'existe pas
            if user_role.role == 'admin':
                return Response({"message": "Connexion réussie en tant qu'administrateur."})
            else:
                return Response({"message": "Connexion réussie en tant qu'utilisateur."})
        except UserRole.DoesNotExist:
            return Response({"error": "Rôle d'utilisateur introuvable."}, status=status.HTTP_400_BAD_REQUEST)
