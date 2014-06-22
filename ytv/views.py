from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib import messages

from ytv import youtube, msgs
from ytv.models import Video

def index(request):
    if request.method == "POST":
        yturl = request.POST['yturl']
        details = youtube.get_details(yturl)
        if details == None:
            messages.error(request, msgs.unreachable)
        else:
            _ytid, _title, _descr = details
            if _title == None:
                messages.error(request, msgs.no_title)
            elif _descr == None:
                messages.error(request, msgs.no_descr)
            else:
                pt = timezone.now()
                v = Video(url=yturl, ytid=_ytid, title=_title, description=_descr, post_date=pt)
                v.save()
                messages.success(request, msgs.added + " " + v.title)
        return HttpResponseRedirect(reverse('ytv:index'))
    else:
        context = {"video_list":paginate(request)}
        return render(request, 'ytv/videos.html', context)

def destroy(request, video_id):
    try:
        video_id = int(video_id)
    except ValueError:
        message.error(request, msgs.nan_id)
    else:
        if request.method == "POST":
            try:
                if request.POST["_method"] == "DELETE":
                    return delete_video(request, video_id)
                else:
                    messages.error(request, msgs.lost)
            except KeyError:
                messages.error(request, msgs.lost)
        else:
            messages.error(request, msgs.lost)
    context = {"video_list" : paginate(request)}
    return render(request, 'ytv/videos.html', context)

def delete_video(request, video_id):
    try:
        v = Video.objects.get(pk=video_id)
        v.delete()
        messages.error(request, msgs.deleted + " " + v.title)
    except Video.DoesNotExist:
        messages.error(request, msgs.not_exist)
    except Exception:
        messages.error(request, msgs.not_deleted)

    context = {"video_list" : paginate(request)}
    return render(request, 'ytv/videos.html', context)
        
    
def paginate(request):
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
    return videos
