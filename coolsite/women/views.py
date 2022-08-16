from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'women/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request):
    if request.GET:
        print(request.get)
    return HttpResponse("Страница приложение categories.")
