from django.db import models

class Video(models.Model):
    url = models.CharField(max_length = 1000)
    ytid = models.CharField('YouTube ID', max_length = 11)
    title = models.CharField(max_length = 300)
    description = models.TextField()

    def __unicode__(self):
        return self.title
