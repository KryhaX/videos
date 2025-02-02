from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, AddedInfo, Review, Actor
from .forms import VideoForm, AddedInfoForm, ActorForm, ReviewForm
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, VideoSerializer


class Videoview(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class Userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def all_videos(request):
    all_videos = Video.objects.all()
    return render(request, 'videos.html', {'all_videos': all_videos})

@login_required
def new_video(request):
    is_new = True
    form_video = VideoForm(request.POST or None, request.FILES or None)
    form_added_info = AddedInfoForm(request.POST or None)


    if all( (form_video.is_valid(), form_added_info.is_valid()) ):
        video = form_video.save(commit=False)
        added_info = form_added_info.save()
        video.added = added_info
        video.save()

        return redirect(all_videos)
    return render(request , 'video_form.html', {'form_video': form_video,
                                                'form_added_info':form_added_info, 'is_new':is_new})

@login_required
def edit_video(request, video_id):
    is_new = False
    video = get_object_or_404(Video, pk=video_id)
    reviews = Review.objects.filter(video=video)
    actors = video.actors.all()

    try:
        added = AddedInfo.objects.get(video=video_id)
    except AddedInfo.DoesNotExist:
        added = None

    form_video = VideoForm(request.POST or None, request.FILES or None , instance=video)
    form_added_info = AddedInfoForm(request.POST or None, instance=added)

    form_review = ReviewForm(request.POST or None)

    if request.method == 'POST':
        if 'stars' in request.POST:
            review = form_review.save(commit=False)
            review.video = video
            review.save()

    if all((form_video.is_valid(), form_added_info.is_valid())):
        video = form_video.save(commit=False)
        added_info = form_added_info.save()
        video.added = added_info
        video.save()

        return redirect(all_videos)
    return render(request, 'video_form.html', {'form_video': form_video,
                                               'form_added_info':form_added_info,'reviews':reviews,
                                               'form_review':form_review,'actors':actors,'is_new':is_new})

@login_required
def delete_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)

    if request.method == 'POST':
        video.delete()
        return redirect(all_videos)

    return render(request, 'confirm.html', {'video': video})