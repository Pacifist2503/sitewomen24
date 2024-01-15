from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from women.models import Women

menu = [{'title': 'О сайте', 'url': 'about'},
        {'title': 'Добавить статью', 'url': 'add_page'},
        {'title': 'Обратная связь', 'url': 'contact'},
        {'title': 'Войти', 'url': 'login'},
        ]


cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    posts = Women.objects.filter(is_published=1)
    data = {'menu': menu,
            'title': 'Главная страница',
            'posts': posts,
            'catselected': 0}
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'menu': menu,
            'title': 'О сайте'}
    return render(request, 'women/about.html', context=data)


def add_page(request):
    return HttpResponse('Добавить страницу')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Логин')


def show_post(request, post_slug):
    post = Women.objects.get(slug=post_slug)
    data = {'menu': menu,
            'title': post.title,
            'post': post}
    return render(request, 'women/post.html', context=data)


def show_category(request, cat_id):
    data = {'menu': menu,
            'title': 'Отображение по рубрикам',
            'catselected1': cat_id}
    return render(request, 'women/show_cats.html', context=data)


def handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')
