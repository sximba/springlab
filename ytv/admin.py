from django.contrib import admin
from ytv.models import Video

class VideoAdmin(admin.ModelAdmin):
    fields = ['ytid', 'title', 'description', 'url']

admin.site.register(Video, VideoAdmin)
