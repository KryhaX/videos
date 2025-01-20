from django.forms import ModelForm

from .models import Video

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'year','premiere', 'imdb_rating', 'poster']

