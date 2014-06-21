from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.utils import timezone

from ytv import youtube
from ytv.models import Video

def index(request):
    context = {}
    if request.method == "POST":
        yturl = request.POST['yturl']
        details = youtube.get_details(yturl)
        if details == None:
            context["error_message"] = "Can't seem to reach that video :( sure it exists?"
        else:
            _ytid, _title, _descr = details
            if _title == None:
                context["error_message"] = "Video not interesting :( Has no title"
            elif _descr == None:
                context["error_message"] = "Video has no description :( Not interesting to me"
            else:
                pt = timezone.now()
                v = Video(url=yturl, ytid=_ytid, title=_title, description=_descr, post_date=pt)
                v.save()

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
    context["video_list"] = videos
    return render(request, 'ytv/videos.html', context)
            

def destroy(request, video_id):
    return HttpResponse("You are deleting video %s." % video_id)
