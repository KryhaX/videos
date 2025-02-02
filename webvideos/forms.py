from django.forms import ModelForm

from .models import Video, AddedInfo, Actor, Review

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'year','premiere', 'imdb_rating', 'poster']

class AddedInfoForm(ModelForm):
    class Meta:
        model = AddedInfo
        fields = ['duration', 'type']

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'surname']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'review']