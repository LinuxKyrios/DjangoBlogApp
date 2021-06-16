from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Model for post on blog
class Post(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }
    #Post title
    title = models.CharField(max_length=250)
    #slug field for URL addresses
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    #Auhor field as foreing key in relation one to many
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    #Post body
    body = models.TextField()
    #Date and time of published post
    publish = models.DateTimeField(default=timezone.now)
    #Field for information when post was created
    created = models.DateTimeField(auto_now_add=True)
    #Date and time of last update
    updated = models.DateTimeField(auto_now=True)
    #Post status
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    #ordering posts by publish date
    class Meta:
        ordering = ('-publish',)

    #returns default representation of model
    def __str__(self):
        return self.title
