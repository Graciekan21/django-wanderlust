from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from .models import Post, Comment

  
    
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
    

def home(request):
    return render(
        request, 
        'index.html'
        )
def update_post(request):
    return render(
        request, 
        'update_post.html'
        )