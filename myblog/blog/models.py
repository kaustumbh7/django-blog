from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    heading = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images/',blank=True, null=True)