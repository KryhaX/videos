from django.urls import path
from .views import all_videos, new_video, edit_video, delete_video

urlpatterns = [
    path('all/',all_videos, name='all_videos'),
    path('new_video/', new_video, name='new_video'),
    path('edit_video/<int:video_id>/', edit_video, name='edit_video'),
    path('delete_video/<int:video_id>/', delete_video, name='delete_video'),
    ]
