from django.shortcuts import render,redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from .forms import Creatform
# Create your views here.
def home (request):
    blogs=Blog.objects.all()
    text={'blogs':blogs}
    return render(request,'my_blog/index.html',text)
def blog (request,pk):
    blog=Blog.objects.get(id=pk)
    text={'blog':blog}
    return render(request,'my_blog/blog.html',text)
@login_required(login_url='login')
def creat(request):
     form=Creatform()
     if request.method=='POST':
        form=Creatform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
     text={'fild':form}
     return render(request,'my_blog/creat.html',text)
@login_required(login_url='login')
def admin(request):
    blogs=Blog.objects.all()
    text={'blogs':blogs}
    return render(request,'my_blog/admin.html',text)
@login_required(login_url='login')
def delet(request,pk):
    blog=Blog.objects.get(id=pk)
    blog.delete()
    return redirect('admin')
@login_required(login_url='login')
def updata(request,pk):
     blog=Blog.objects.get(id=pk)
     form=Creatform(instance=blog)
     if request.method=='POST':
        form=Creatform(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('admin')
     text={'fild':form}
     return render(request,'my_blog/creat.html',text)