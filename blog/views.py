from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('datetime')
    return render(request, 'blog/post_list.html', {'posts': posts})
