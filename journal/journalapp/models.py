from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"), (2, "Rejected"))


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='article_post')
    keywords = models.CharField(max_length=200, null=True)
    published_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    abstract = models.TextField()
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return self.title
