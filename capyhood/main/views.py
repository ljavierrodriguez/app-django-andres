from django.shortcuts import render, redirect
from .models import Task
from accounts.models import User
from django.contrib.auth import login as django_login, authenticate, logout

# Create your views here.

def home(request):
    
    if not request.user.is_authenticated:
        return redirect('login')
    
    template_name="index.html"
    
    tasks = Task.objects.all()
    
    return render(request, template_name, { "saludo": "Hola desde django", "tasks": tasks})

def login(request):
    template_name="login.html"
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if not request.POST:
        return render(request, template_name, {})
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            django_login(request, user)
            return redirect('home')
        
        return redirect('login')
    
def logout_view(request):
    logout(request)
    
    return redirect('login')


def register(request):
    template_name="register.html"
    
    if not request.POST:
        return render(request, template_name, { "name": "", "username": "", "password": ""})
    
    if request.POST:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = User.objects.create_user(username, email, password)
        user.is_staff = True
        user.save()
        
        return redirect('register')
        
        


def save_task(request):
    
    if not request.POST:
        return redirect('home')
    
    label = request.POST.get('label')
    
    newTask = Task(label=label)
    newTask.save()
    
    return redirect('home')

def delete_task(request, id):
    
    oldTask = Task.objects.get(pk=id)
    oldTask.delete()
    
    return redirect('home')


def complete_task(request, id):
    
    oldTask = Task.objects.get(pk=id)
    oldTask.done = True
    oldTask.save()
    
    return redirect('home')