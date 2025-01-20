from django.contrib import admin
from .models import Video


# admin.site.register(Video)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'imdb_rating', 'year')
    list_filter = ('year', )
    search_fields = ('title', "description")