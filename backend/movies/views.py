from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import UserRole, Movie
from .serializers import MovieSerializer

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

        # Créez ou récupérez le token pour l'utilisateur
        token, created = Token.objects.get_or_create(user=user)

        try:
            user_role = user.userrole
            if user_role.role == 'admin':
                return Response({"message": "Connexion réussie en tant qu'administrateur.", "token": token.key})
            else:
                return Response({"message": "Connexion réussie en tant qu'utilisateur.", "token": token.key})
        except UserRole.DoesNotExist:
            return Response({"error": "Rôle d'utilisateur introuvable."}, status=status.HTTP_400_BAD_REQUEST)

# CRUD pour le modèle Movie
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAdminUser]

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAdminUser]

class MovieUserListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
