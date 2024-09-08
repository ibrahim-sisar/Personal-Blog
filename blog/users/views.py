from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def loginform(request):
    if request.user.is_authenticated:
       return redirect('admin')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            print('hello')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('admin')
    return render(request,'users/login.html')
