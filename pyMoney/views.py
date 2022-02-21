from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {})


def send_money(request):
    return HttpResponse('send money')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in, try again"))
            return redirect('login')

    else:
        return render(request, 'login.html', {})
