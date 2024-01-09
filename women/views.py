from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request):
    return HttpResponse('Главная страница')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1> категория {cat_id}")


def year_archive(request, year):
    if year > 2024:
        raise Http404()
    return HttpResponse(f"<h1>Статьи по категориям</h1> Год {year}")


def categories_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1> SLUG {cat_slug}")


def handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')
