from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import *
import cloudinary
from cloudinary.uploader import upload
import re
import random
# Function based category view
# CODE CREDIT - code institute Walk through project


def custom_404_view(request, exception):
    return render(request, "post.html", status=404)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetailEdit(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter().order_by("-created_on")
        categories = Category.objects.all()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "update_post.html",
            {
                "is_post_user": (request.user.id == post.author.id),
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "categories": categories,
                "form": PostForm(instance=post),
            },
        )

    def post(self, request, slug=None, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        categories = Category.objects.all()
# comments = post.comments.filter(approved=True).order_by("-created_on")
        rPost = request.POST.copy()
        rPost["author"] = request.user.id
        rPost = request.POST.copy()
        rPost["slug"] = request.POST['title']
        rPost['slug'] = re.sub(r'\W+', '', rPost['slug'])
        post_form = PostForm(rPost, request.FILES, instance=post)
        if post_form.is_valid():
            # post_form.slug=re.sub(r'\W+', '',rPost['slug'])
            # comment_form.instance.featured_image= cloudinary_url
            mypost = post_form.save(commit=False)
            mypost.save()
            msg = "Saved Successfully"
        else:
            # post_form = PostForm()
            msg = "Invalid Input!"

        return render(
            request,
            "update_post.html",
            {"form": post_form, "msg": msg, "post": post},
        )


class PostDetail(View):
    def get(self, request, slug=None, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter().order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_data = []
        for comment in comments:
            if comment.username.lower() == request.user.username.lower():
                comment_data.append({"mycomment": comment, "is_owner": True})
            else:
                comment_data.append({"mycomment": comment, "is_owner": False})

        return render(
            request,
            "post_detail.html",
            {
                "is_post_user": (request.user.id == post.author.id),
                "post": post,
                "comments": comment_data,
                "comments_2": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug=None, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter().order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        rPost = request.POST.copy()

        comment_form = CommentForm(data=rPost)
        if comment_form.is_valid():
            comment_form.instance.username = request.user.username
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        comment_data = []
        for comment in comments:
            if comment.username.lower() == request.user.username.lower():
                comment_data.append({"mycomment": comment, "is_owner": True})
            else:
                comment_data.append({"mycomment": comment, "is_owner": False})

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comment_data,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class DeletePostView(View):
    def get(self, request, slug=None, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        Post.objects.filter(slug=post.slug).delete()
        return redirect("home")


class CommentEdit(View):
    def get(self, request, slug=None, pk=None, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug, status=1)
        cqs = post.comments.filter(pk=pk)
        comments = get_object_or_404(cqs)

        return render(
            request,
            "update_comment.html",
            {
                "msg": "",
                "post": post,
                "comments": comments,
                "form": CommentForm(instance=comments),
            },
        )

    def post(self, request, slug=None, pk=None, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug, status=1)
        cqs = post.comments.filter(pk=pk)
        comments = get_object_or_404(cqs)
        comment_form = CommentForm(data=request.POST, instance=comments)
        if comment_form.is_valid():
            mycomment = comment_form.save(commit=False)
            mycomment.save()
            msg = "Saved Successfully"
        else:
            msg = "Invalid Input!"

        return render(
            request,
            "update_comment.html",
            {"form": comment_form, "msg": msg, "post": post},
        )


class CommentDeleteView(View):
    def get(self, request, slug=None, pk=None, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug, status=1)
        cqs = post.comments.filter(pk=pk)
        comment = get_object_or_404(cqs)
        if comment.delete():
            msg = "Comment Deleted Successfully"
            return redirect("post_detail", slug)
        else:
            msg = "Comment Deletion Failed!"
        comments = post.comments.filter().order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "is_post_user": (request.user.id == post.author.id),
                "msg": msg,
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostView(View):
    model = Post
    form_class = PostForm
    template_name = "post.html"

    def get(self, request, slug=None, *args, **kwargs):
        return render(
            request,
            "post.html",
            {"form": PostForm()},
        )

    def post(self, request, slug=None, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
# comments = post.comments.filter(approved=True).order_by("-created_on")
        rPost = request.POST.copy()
        rPost["author"] = request.user.id
        rPost["slug"] = request.POST['title']
        rPost['slug'] = re.sub(r'\W+', '', rPost['slug'])
        post_form = PostForm(rPost, request.FILES)
        # post_form.author.username=request.user.username
        if post_form.is_valid():
            # post_form.slug=re.sub(r'\W+', '',rPost['slug'])
            mypost = post_form.save(commit=True)
            mypost.save()
            msg = "Saved Successfully"
        else:
            # post_form = PostForm()
            msg = "Invalid Input!"
            rPost['slug'] = ''

        return render(
            request,
            "post.html",
            {"form": post_form, "msg": msg, 'slug': rPost['slug']},
        )
