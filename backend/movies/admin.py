# movies/admin.py

from django.contrib import admin
from .models import UserRole, Movie

admin.site.register(UserRole)
admin.site.register(Movie)
