from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_published = models.DateTimeField(blank=True, null=True)


def publish(self):

    self.date_published = timezone(now)
    self.save()

