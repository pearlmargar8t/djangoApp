from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def send_money(request):
    return HttpResponse('send money')
