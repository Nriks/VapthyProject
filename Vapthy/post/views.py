from django.shortcuts import render, redirect
# from .models import Post, Like
from .models import Post

from .forms import PostForm
from django.views.generic import ListView, DetailView

# Create your views here.

class PostView(ListView):
    model = Post 
    template_name = 'post/main.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_details.html'

# def post_view(request):
#     # qs = Post.objects.order_by('post__liked')
#     # qs = Post.objects.all().order_by('-liked')
#     qs = Post.objects.all()
#     user = request.user

#     context = {
#         'qs': qs,
#         'user': user,
#     }

#     return render(request, 'post/main.html', context)





# def like_post(request):
#     user = request.user
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         post_obj = Post.objects.get(id=post_id)

#         if user in post_obj.liked.all():
#             post_obj.liked.remove(user)
#         else:
#             post_obj.liked.add(user)

#         like, created = Like.objects.get_or_create(user=user, post_id=post_id)

#         if not created:
#             if like.value == 'Like':
#                 like.value = 'Unlike'
#             else:
#                 like.value = 'Like'

#         like.save()
#     return redirect('post:post-list')

# def create_post(request):
#     return render(request, 'createPost.html')

# def write_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             body = form.cleaned_data['body']
#             try:
#                 form.save()
#                 return redirect('main')
#             except:
#                 pass
#     else:
#         form= PostForm()
#     return render(request, 'main.html', {'form':form})