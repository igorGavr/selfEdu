from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *


def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Головна сторінка',
    }
    return render(request, 'women/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def addpage(request):
    return HttpResponse('Додавання статті')


def contact(request):
    return HttpResponse('Зворотній звязок')


def login(request):
    return HttpResponse('Авторизація')


def show_category(request, cat_slug):
    posts = Women.objects.filter(cat__slug=cat_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Відображення по рубрикам',
        'cat_selected': cat_slug,
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
