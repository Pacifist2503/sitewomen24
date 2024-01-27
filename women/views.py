from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import AddPostForm, UploadFileForm

from women.models import Women, Category, TagPost

import random

menu = [{'title': 'О сайте', 'url': 'about'},
        {'title': 'Добавить статью', 'url': 'add_page'},
        {'title': 'Обратная связь', 'url': 'contact'},
        {'title': 'Войти', 'url': 'login'},
        ]


def index(request):
    posts = Women.published.all().select_related('cat', 'husband')
    data = {'menu': menu,
            'title': 'Главная страница',
            'posts': posts,
            'catselected': 0}
    return render(request, 'women/index.html', context=data)


def handle_uploaded_file(f):
    """
    Функция для загрузки файла на сервер
    """
    with open(f"uploads/{f.name}_{random.random()}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
        # handle_uploaded_file(request.FILES['upload_file'])
    else:
        form = UploadFileForm()
    data = {'menu': menu,
            'title': 'О сайте',
            'form': form}
    return render(request, 'women/about.html', context=data)


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, 'Ошибка добавления поста')



    else:
        form = AddPostForm()
    data = {'menu': menu,
            'title': 'Добавить страницу',
            'form': form}
    return render(request, 'women/addpage.html', context=data)


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Логин')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {'menu': menu,
            'title': post.title,
            'post': post}
    return render(request, 'women/post.html', context=data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')
    data = {'menu': menu,
            'title': f'Рубрика: {category.name}',
            'catselected1': cat_slug,
            'post_cat': posts}
    return render(request, 'women/show_cats.html', context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.posts_tag.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    data = {'menu': menu,
            'title': f'Рубрика по тэгам: {tag}',
            'catselected1': None,
            'posts': posts}
    return render(request, 'women/index.html', context=data)


def handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')
