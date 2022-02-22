from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .forms import RegisterUserForm


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


def signup(request):
    form = RegisterUserForm
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, ("Registration successful!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error restering you, try again"))
            form = RegisterUserForm()
            return redirect('signup')
    else:
        return render(request, 'signup.html',
                      {'form': form}
                      )
