# movies/urls.py

from django.urls import path
from .views import RegisterView, LoginView
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView, MovieUserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
     path('movies/', MovieUserListView.as_view(), name='movie-list'),  # Liste des films pour utilisateurs
    path('admin/movies/', MovieListCreateView.as_view(), name='admin-movie-list-create'),  # Liste et création de films (admin)
    path('admin/movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='admin-movie-detail'),
]
