from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('user/<str:username>/', UserPostListView.as_view(),name='user-posts'),
    path('users/<int:pk>/',UserDetialView.as_view(),name='user-detial'),
    path('post/<int:pk>/',PostDetialView.as_view(),name='post-detial'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('about/',views.about,name='blog-about' ),
    path('',views.postlist,name='blog-home' ),  
    path('oldposts/',views.oldpostlist,name='oldposts'), 
    path('postitle/',views.postitle,name='postitle'), 
    path('username/',views.username,name='username'), 
    path('post/new/',PostCreateView.as_view(),name='post-create' ),
    path('comment/new/<int:pk>',CommentCreateView.as_view(),name='comment-create' ),
    path('comment/delete/<int:pk>',CommentDeleteView.as_view(),name='comment-delete' ),
    path('Comment/update/<int:pk>/',CommentUpdateView.as_view(),name='comment-update'),
    
]
