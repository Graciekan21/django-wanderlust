from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', views.PostDetailEdit.as_view(), name='post_detail_edit'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('comment/edit/<slug:slug>/<int:pk>/', views.CommentEdit.as_view(), name='comment_edit'),
    path('comment/delete/<slug:slug>/<int:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('post.html/', views.PostView.as_view(), name='post'),
    #path('add_category.html/', views.AddCategoryView.as_view(), name='add_category'),
    #path('<slug:slug>/update/', views.EditPostView.as_view(), name='update_post'),
    path('delete/<slug:slug>/', views.DeletePostView.as_view(), name='delete_post'),
    #path('category/<str:cats>/', CategoryView, name='category'),
]
