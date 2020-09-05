from django.shortcuts import render, redirect
from .models import Post, Like
from .forms import PostForm
# Create your views here.


def post_view(request):
    qs = Post.objects.all()
    liked
    user = request.user
    context = {
        'qs': qs,
        'user': user,
    }

    return render(request, 'post/main.html', context)


def like_post(request):
    
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('post:post-list')

def classify_post():
    like_number = request.GET.get('numberLike')
    like_number_sorted = sorted(like_number)


def write_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    context = {'form': form}
    return render(request, 'post/main.html', context)