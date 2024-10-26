from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'created_by')
    search_fields = ('title',)

admin.site.register(Movie, MovieAdmin)
