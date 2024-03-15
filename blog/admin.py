from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModleAdmin


@dmin.register(Post)
class PostAdmin(SummernoteModleAdmin):

    summernote_fields = ('content')
