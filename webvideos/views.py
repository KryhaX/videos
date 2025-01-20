from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import VideoForm
from .models import Video
from .forms import VideoForm

def all_videos(request):
    all_videos = Video.objects.all()
    return render(request, 'videos.html', {'all_videos': all_videos})

def new_video(request):
    form = VideoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_videos)
    return render(request , 'video_form.html', {'form': form})

def edit_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)

    form = VideoForm(request.POST or None, request.FILES or None , instance=video)

    if form.is_valid():
        form.save()
        return redirect(all_videos)
    return render(request, 'video_form.html', {'form': form})

def delete_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)

    if request.method == 'POST':
        video.delete()
        return redirect(all_videos)

    return render(request, 'confirm.html', {'video': video})