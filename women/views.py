from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

menu = [{'title': 'О сайте', 'url': 'about'},
        {'title': 'Добавить статью', 'url': 'add_page'},
        {'title': 'Обратная связь', 'url': 'contact'},
        {'title': 'Войти', 'url': 'login'},
        ]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
    {'id': 4, 'title': 'Пугачева', 'content': 'Пугачева', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    data = {'menu': menu,
            'title': 'Главная страница',
            'posts': data_db,
            'catselected': 0}
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'menu': menu,
            'title': 'О сайте',
            'posts': data_db}
    return render(request, 'women/about.html', context=data)


def add_page(request):
    return HttpResponse('Добавить страницу')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Логин')


def show_post(request, post_id):
    return HttpResponse(f'Номер поста {post_id}')


def show_category(request, cat_id):
    data = {'menu': menu,
            'title': 'Отображение по рубрикам',
            'catselected1': cat_id}
    return render(request, 'women/show_cats.html', context=data)


def handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')
