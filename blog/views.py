from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from accounts import views as user_views

# Create your views here.

def home(request):
    posts = Post.objects.all
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.writer = request.user
            post.save()
            return redirect('home')
            
    else:
        form = PostForm()
    return render(request, 'home.html',{'posts_list':posts, 'form' : form})
    
def post_detail(request, index):
    post = get_object_or_404(Post, pk=index)
    return render(request, 'post_detail.html',{'post':post})
    
def post_edit(request, index):
    post = get_object_or_404(Post, pk=index)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('post_detail',index=post.pk)
            
    else:
        form = PostForm(instance = post)
            
    return render(request, 'post_edit.html', {'form':form})
    
def post_delete(request, index):
    post = get_object_or_404(Post, pk=index)
    post.delete()
    return redirect('home')
    
def javascript(request):
    return render(request, 'javascript.html')