from django.urls import path 
# from .views import post_view, like_post
from . import views
from .views import PostView, PostDetailView

app_name = "post"

urlpatterns = [
    # path('', views.post_view, name='post-list'),
    path('', PostView.as_view(), name="main"),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail')
    # path('like/', views.like_post, name="like-post"),
    # path('', views.create_post, name="create-post"),
    # path('createPost/', views.write_post, name="write-post"),
    
]