# backend/movies/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Créez un routeur par défaut pour les vues de Movie
router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    # Inclus les routes de MovieViewSet
    path('', include(router.urls)),  
    
    # Route pour l'inscription d'un nouvel utilisateur
    path('register/', RegisterView.as_view(), name='register'),  
    
    # Route pour l'obtention d'un token après login
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    
    # Route pour rafraîchir le token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]
