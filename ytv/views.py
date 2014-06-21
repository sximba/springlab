from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from ytv.models import Video

def index(request):
    if request.method == "GET":
        video_list = Video.objects.all().order_by('-post_date')
        paginator = Paginator(video_list, 10)
        page = request.GET.get('page')

        try:
            videos = paginator.page(page)
        except PageNotAnInteger:
            # Deliver first page
            videos = paginator.page(1)
        except EmptyPage:
            # Deliver last page
            videos = paginator.page(paginator.num_pages)
        context = {'video_list' : videos}
        return render(request, 'ytv/videos.html', context)
    elif request.method == "POST":
        return HttpResponse("You are posting a video")

def destroy(request, video_id):
    return HttpResponse("You are deleting video %s." % video_id)
