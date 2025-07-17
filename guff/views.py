from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import CustomuserCreationForms, PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts' : posts})

def register(request):
    if request.method == 'POST':
        form =CustomuserCreationForms(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User is registered successfully, now you can login')
            return redirect('login')
    else:
        form = CustomuserCreationForms()
    return render(request, 'registration/register.html', {'form': form})

# @login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit= False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post is created successfully')
            return redirect('home')
    else:
        form = PostForm()
    return render (request, 'posts/post_create.html', {'form' : form})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if post.user != request.user:
        messages.error(request, 'You cannot edit others post')
        return redirect('home')
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post is updated successfully')
            return redirect('home')
        
    else:
        form = PostForm(instance=post)
    return (request, 'posts/post_edit.html', {'form' : form, 'post': post})


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id= post_id)
    
    if post.user != request.user:
        messages.error(request, 'You cannot delete others post')
        return redirect('home')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully')
        return redirect('home')
    return render(request, 'posts/post_delete.html', {'post': post})