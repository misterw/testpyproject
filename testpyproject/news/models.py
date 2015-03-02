from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Date of Publication')
    content = models.TextField(max_length=10000)

    verbose_name_plural = "News"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/%i/" % self.id

    class Meta:
        verbose_name = u'News'
        verbose_name_plural = u'List of News'