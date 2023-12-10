# En tu archivo models.py dentro de la aplicación blog
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
