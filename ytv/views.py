from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse

from ytv.models import Video

def index(request):
    if request.method == "GET":
        video_list = Video.objects.all()
        context = {'video_list' : video_list}
        return render(request, 'ytv/videos.html', context)
    elif request.method == "POST":
        return HttpResponse("You are posting a video")

def destroy(request, video_id):
    return HttpResponse("You are deleting video %s." % video_id)
