# backend/film_recommendation/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),  # Inclut les routes de l'application movies
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Route pour obtenir le token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/movies/', include('movies.urls')),   # Route pour rafraîchir le token
]
