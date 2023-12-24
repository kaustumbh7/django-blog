from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['username', 'password']

class BlogPostSerializer(serializers.ModelSerializer):
    user =  UserSerializer()
    class Meta:
        model = BlogPost
        fields = ['id', 'heading', 'body', 'user']