from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['verify']:
            try:
                check_user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'User already exist!'})
            
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password did not match'})

    else :
        return render(request, 'accounts/signup.html')

def show_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None :
            login(request,user)
            return render(request, 'accounts/login.html', {'error':'Login sucessful!'})
        else:
            return render(request, 'accounts/login.html',{'error':'The username did not match password'})


    else :
        return render(request, 'accounts/login.html')