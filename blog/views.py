from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    # model = Post -now redundant by queryset
    queryset = Post.objects.filter(status=1)
    template_name = 'post_list.html' 
    # above line is redundant by django's default naming rule which is <app_name>/<model_name>_list.html
