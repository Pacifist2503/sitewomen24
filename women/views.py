from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, FormView, CreateView, UpdateView

from .forms import AddPostForm, UploadFileForm

from women.models import Women, Category, TagPost, UploadFiles

import random

menu = [{'title': 'О сайте', 'url': 'about'},
        {'title': 'Добавить статью', 'url': 'add_page'},
        {'title': 'Обратная связь', 'url': 'contact'},
        {'title': 'Войти', 'url': 'login'},
        ]


# def index(request):
#     posts = Women.published.all().select_related('cat', 'husband')
#     data = {'menu': menu,
#             'title': 'Главная страница',
#             'posts': posts,
#             'catselected': 0}
#     return render(request, 'women/index.html', context=data)


class WomenHome(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    extra_context = {'menu': menu,
                     'title': 'Главная страница',
                     # 'posts': Women.published.all().select_related('cat', 'husband'),
                     'catselected': 0}

    def get_queryset(self):
        return Women.published.all().select_related('cat', 'husband')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = menu
    #     context['title'] = 'Главная страница'
    #     context['posts'] = Women.published.all().select_related('cat', 'husband')
    #     context['catselected1'] = self.request.GET.get('cat_id')
    #     return context


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
            UploadFiles(file=form.cleaned_data['file']).save()
            # handle_uploaded_file(form.cleaned_data['file'])
        # handle_uploaded_file(request.FILES['upload_file'])
    else:
        form = UploadFileForm()
    data = {'menu': menu,
            'title': 'О сайте',
            'form': form}
    return render(request, 'women/about.html', context=data)


# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#             # try:
#             #     Women.objects.create(**form.cleaned_data)
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddPostForm()
#     data = {'menu': menu,
#             'title': 'Добавить страницу',
#             'form': form}
# class AddPost(FormView):
#     form_class = AddPostForm
#     template_name = 'women/addpage.html'
#     success_url = reverse_lazy('home')
#     extra_context = {
#         'menu': menu,
#         'title': 'Добавить страницу',
#     }
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
class AddPost(CreateView):
    model = Women
    fields = '__all__'
    template_name = 'women/addpage.html'
    # success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Добавить страницу',
    }


class UpdatePage(UpdateView):
    model = Women
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Править страницу',
    }


class DeletePage(DeleteView):
    model = Women
    success_url = reverse_lazy("home")
    template_name = 'women/women_confirm_delete.html'
    extra_context = {
        'menu': menu,
        'title': 'Удалить страницу',
    }


# class AddPost(View):
#     def post(self, request, *args, **kwargs):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         data = {'menu': menu,
#                 'title': 'Добавить страницу',
#                 'form': form}
#         return render(request, 'women/addpage.html', context=data)
#
#     def get(self, request, *args, **kwargs):
#         form = AddPostForm()
#         data = {'menu': menu,
#                 'title': 'Добавить страницу',
#                 'form': form}
#         return render(request, 'women/addpage.html', context=data)


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Логин')


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     data = {'menu': menu,
#             'title': post.title,
#             'post': post}
#     return render(request, 'women/post.html', context=data)


class ShowPost(DetailView):
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Women.published.filter(cat_id=category.pk).select_related('cat')
#     data = {'menu': menu,
#             'title': f'Рубрика: {category.name}',
#             'catselected1': cat_slug,
#             'post_cat': posts}
#     return render(request, 'women/show_cats.html', context=data)


class WomenCategory(ListView):
    template_name = 'women/show_cats.html'
    context_object_name = 'post_cat'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = f'Категория - {context['post_cat'][0].cat.name}'
        context['catselected1'] = self.kwargs['cat_slug']
        return context


# def show_tag_postlist(request, tag_slug):
#     tag = get_object_or_404(TagPost, slug=tag_slug)
#     posts = tag.posts_tag.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
#
#     data = {'menu': menu,
#             'title': f'Рубрика по тэгам: {tag}',
#             'catselected1': None,
#             'posts': posts}
#     return render(request, 'women/index.html', context=data)


class WomenTag(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = f'Тэг - {TagPost.objects.get(slug=self.kwargs['tag_slug'])}'
        # context['catselected1'] = self.kwargs['cat_slug']
        return context


def handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')
