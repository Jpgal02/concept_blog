import django_filters 

from .models import Post, Category, Comment

class PostFilter(django_filters.FilterSet):
    class Meta:
        models = Post
        fields = ['title']