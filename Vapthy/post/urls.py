from django.urls import path 
# from .views import post_view, like_post
from . import views

app_name = "post"

urlpatterns = [
    path('', views.post_view, name='post-list'),
    path('like/', views.like_post, name="like-post"),
    path('', views.write_post, name="post-form"),
    
]