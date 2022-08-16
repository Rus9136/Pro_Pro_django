from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Страница приложение django.")


def categories(request):
    if request.GET:
        print(request.get)
    return HttpResponse("Страница приложение categories.")
