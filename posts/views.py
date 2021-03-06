from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.

@xframe_options_exempt
def home(request):
    posts = Post.objects.order_by('-votes_total')
    return render(request,'posts/home.html', {'posts':posts})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            if request.POST['description']:
                post.description = request.POST['description']
            
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'https://'+request.POST['url']
            
            post.pub_date = timezone.datetime.now()
            post.author = request.user
         
            post.save()
            return redirect('home')
        else:
            return render(request,'posts/create.html', {"error": "You need a title and an url"})


    else:
        return render(request, 'posts/create.html')

    
@xframe_options_exempt
def upvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1 
        post.save()
        return redirect('home')
    
    
@xframe_options_exempt
def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1 
        post.save()
        return redirect('home')

@login_required
def edit(request):
    return render(request, "You want to edit a post!")
