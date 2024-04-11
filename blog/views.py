from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import *
import cloudinary
from cloudinary.uploader import upload
  
   # Function based category view
# CODE CREDIT - code institute - Walk through project (I think there fore i blog)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
    
class PostDetailEdit(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        categories = Category.objects.all()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "update_post.html",
            {    
                "is_post_user":(request.user.id==post.author.id),
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "categories":categories,
                "form": PostForm(instance=post)
            },
        )

    def post(self, request, slug=None, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        categories = Category.objects.all()
        #comments = post.comments.filter(approved=True).order_by("-created_on")            
        try:
            image = request.POST['featured_image']
            # Upload image to Cloudinary
            result = upload(image, use_filename=True)
            
            # Handle success or error response
            if 'url' in result:
                cloudinary_url = result['url']
            else:
                return render(request, 'update_post.html', {'msg': result.get('error', 'Unknown error')})
        except:
            cloudinary_url = "https://res.cloudinary.com/damp5dgzr/image/upload/v1712097422/dbb0ysf3wukulyemhmey.jpg"
        
        post_form = PostForm(data=request.POST,instance=post)
        if post_form.is_valid():
            #comment_form.instance.featured_image= cloudinary_url
            post_form.featured_image= cloudinary_url
            mypost = post_form.save(commit=False)
            mypost.save()
            msg="Saved Successfully"
        else:
            #post_form = PostForm()
            msg="Invalid Input!"

        return render(
            request,
            "update_post.html",
            {"form":post_form,"msg":msg},
        )

class PostDetail(View):

    def get(self, request, slug=None, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {    
                "is_post_user":(request.user.id==post.author.id),
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug=None, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
class DeletePostView(View):
    def get(self, request, slug=None, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        Post.objects.filter(slug=post.slug).delete()
        return redirect('home')

"""class DeleteComment(View):
    def get(self, request, slug=None, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        Post.objects.filter(slug=post.slug).delete()
        return redirect('home')"""

class PostView(View):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    def get(self, request, slug=None, *args, **kwargs):
        return render(
            request,
            "post.html",
            {"form":PostForm()},
        )
    
    def post(self, request, slug=None, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        #comments = post.comments.filter(approved=True).order_by("-created_on")            
        try:
            image = request.POST['featured_image']
            # Upload image to Cloudinary
            result = upload(image, use_filename=True)
            
            # Handle success or error response
            if 'url' in result:
                cloudinary_url = result['url']
            else:
                return render(request, 'error.html', {'error_message': result.get('error', 'Unknown error')})
        except:
            cloudinary_url = "https://res.cloudinary.com/damp5dgzr/image/upload/v1712097422/dbb0ysf3wukulyemhmey.jpg"
        
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            #comment_form.instance.featured_image= cloudinary_url
            post_form.featured_image= cloudinary_url
            mypost = post_form.save(commit=False)
            mypost.save()
            msg="Saved Successfully"
        else:
            #post_form = PostForm()
            msg="Invalid Input!"

        return render(
            request,
            "post.html",
            {"form":PostForm(),"msg":msg},
        )


