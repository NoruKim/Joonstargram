from django.db.models.aggregates import Count
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from joonstargram.users.models import User
from .models import *
from .serializers import *
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            comment_form = CommentForm()

            user = get_object_or_404(User, pk=request.user.id)
            followings = user.followings.all()
            posts = Post.objects.filter(
                Q(author__in=followings) | Q(author = user)
            ).order_by('-created')

            serializer = PostSerializer(posts, many=True)

            return render(request, 'posts/main.html',
                        {"posts": serializer.data, "comment_form": comment_form}
            )

def post_create(request):
    if request.method == 'GET':
        form = CreatePostForm()
        return render(request, 'posts/post_create.html', {"form": form})

    elif request.method == 'POST':
        if request.user.is_authenticated:
            user = get_object_or_404(User, pk=request.user.id)

            form = CreatePostForm(request.POST, request.FILES)
            if form.is_valid():
                # commit=False 데이터가 DB에 일단 저장 되지 않음.
                post = form.save(commit=False)

                post.author = user
                post.save()

            else:
                print(form.errors)


            return redirect(reverse('posts:index'))

        else:
            return render(request, 'users/main.html')

def post_update(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)

        if request.user != post.author:
            redirect(reverse('posts:index'))

        if request.method == 'GET':
            form = UpdatePostForm(instance=post)
            return render(request, 'posts/post_update.html',
                        {"form": form, "post": post}
            )

        elif request.method == 'POST':
            form = UpdatePostForm(request.POST, instance=post)
            if form.is_valid():
                post.caption = form.cleaned_data['caption']
                post.save()

            return redirect(reverse('posts:index'))

    else:
        return render(request, 'users/main.html')

def post_delete(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)

        if request.user == post.author:
            post.delete()

        return redirect(reverse('posts:index'))

    else:
        return render(request, 'users/main.html')

def post_image_like(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)

        if request.user in post.image_likes.all():
            post.image_likes.remove(request.user)
        else:
            post.image_likes.add(request.user)

        return redirect(reverse('posts:index'))

    else:
        return render(request, 'users/main.html')

def comment_create(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.posts = post
            comment.save()

            return redirect(reverse('posts:index'))

        else:
            return render(request, 'users/main.html')

def comment_delete(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)

        if request.user == comment.author:
            comment.delete()

        return redirect(reverse('posts:index'))

    else:
        return render(request, 'users/main.html')

def search(request):
    if request.user.is_authenticated:
        users = User.objects.all().exclude(pk=request.user.id)
        keyword = request.GET.get('keyword', '')

        if keyword:
            users = users.filter(username__icontains=keyword)

        serializer = PostAuthorSerializer(users, many=True)

        return render(request, 'posts/search.html',
                    {'users': serializer.data, 'keyword': keyword})

    else:
        return render(request, 'users/main.html')

def follow(request, user_id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=user_id)

        if request.user in user.followers.all():
            user.followers.remove(request.user)
            request.user.followings.remove(user)

        else:
            user.followers.add(request.user)
            request.user.followings.add(user)

        return redirect(reverse('posts:search'))

    else:
        return render(request, 'users/main.html')

def profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)

        posts = Post.objects.filter(
                Q(author = user)
            ).order_by('-created')

        serializer = PostSerializer(posts, many=True)

        return render(request, 'posts/profile.html', {'user': user, 'posts': serializer.data})

    else:
        return render(request, 'users/main.html')

def other_profile(request, user_id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=user_id)

        posts = Post.objects.filter(
                Q(author = user)
            ).order_by('-created')

        serializer = PostSerializer(posts, many=True)

        return render(request, 'posts/other_profile.html', {'user': user, 'posts': serializer.data})

    else:
        return render(request, 'users/main.html')

def profile_update(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)

        if request.method == 'GET':
            form = ProfileForm(instance=user)
            return render(request, 'posts/profile_update.html',
                        {"form": form, "user": user}
            )

        elif request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=user)

            if form.is_valid():
                user.username = form.cleaned_data['username']
                user.profile_photo = form.cleaned_data['profile_photo']
                user.website = form.cleaned_data['website']
                user.intro = form.cleaned_data['intro']
                user.phone_number = form.cleaned_data['phone_number']
                user.gender = form.cleaned_data['gender']
                user.save()
            else:
                print(form.errors)

            return redirect(reverse('posts:profile'))
