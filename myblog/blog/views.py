from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login")
def all_blogs(request):
    all_blogs = BlogPost.objects.all()
    return render(request, 'blog/all_blogs.html', context={'blogs': all_blogs})

@login_required(login_url="/login")
def create_blog(request):
    if request.method == 'POST':
        data = request.POST
        
        blog_heading = data.get('heading')
        blog_body = data.get('body')
        blog_image = request.FILES.get('image')

        BlogPost.objects.create(heading=blog_heading, body=blog_body, image=blog_image)

        return redirect('/')
    return render(request, 'blog/create_blog.html');

@login_required(login_url="/login")
def view_blog_by_id(request, id):
    blog = BlogPost.objects.get(id=id)
    
    return render(request, 'blog/blog.html', context={'blog': blog})

@login_required(login_url="/login")
def edit_blog(request, id):
    blog = BlogPost.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        
        blog.heading = data.get('heading')
        blog.body = data.get('body')
        
        if (request.FILES.get('image')):
            blog.image = request.FILES.get('image')

        blog.save()

        return redirect('/')

    return render(request, 'blog/edit_blog.html', context={'blog': blog})

@login_required(login_url="/login")
def delete_blog(request, id):
    blog = BlogPost.objects.get(id=id)

    blog.delete();

    return redirect('/')

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        
        username = data.get('username')
        password = data.get('password')


        if not User.objects.filter(username=username).exists():
            print('Username does not exist.')
            messages.error(request, 'Username does not exist.')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:        
            messages.info(request, 'Incorrect password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'blog/login.html')

def register_page(request):
    if request.method == 'POST':
        data = request.POST
        
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already exists.')
            return redirect('/register/')
        
        user = User.objects.create(username=username)
        user.set_password(password)

        user.save()
        
        messages.success(request, 'Account created successfully.')

        return redirect('/login')
    return render(request, 'blog/register.html')
    
def logout_user(request):
    logout(request)
    return redirect('/login/')