from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models
# Create your views here.

def home(request):
    return render(request,'posts/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = models.Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request,'posts/create.html', {"error": "You need a title and an url"})


    else:
        return render(request, 'posts/create.html')


@login_required
def edit(request):
    return render(request, "You want to edit a post!")