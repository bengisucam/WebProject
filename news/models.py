from django.db import models
import accounts.models
from accounts.models import Instructor

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500, blank=False)
    likes = models.PositiveSmallIntegerField(default=0)


class NewsInstructorMatch(models.Model):
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
