from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Главная страница')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1> категория {cat_id}")


def year_archive(request, year):
    return HttpResponse(f"<h1>Статьи по категориям</h1> Год {year}")


def categories_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1> SLUG {cat_slug}")