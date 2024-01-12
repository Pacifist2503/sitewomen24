from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
    {'id': 4, 'title': 'Пугачева', 'content': 'Пугачева', 'is_published': True},
]


def index(request):
    data = {'menu': menu,
            'title': 'Главная страница',
            'posts': data_db}
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'menu': menu,
            'title': 'О сайте',
            'posts': data_db}
    return render(request, 'women/about.html', context=data)


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1> категория {cat_id}")


def year_archive(request, year):
    if year > 2024:
        # raise Http404()
        uri = reverse('categories_slug', args=['year'])
        return redirect(uri)
    return HttpResponse(f"<h1>Статьи по категориям</h1> Год {year}")


def categories_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1> SLUG {cat_slug}")


def handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')
