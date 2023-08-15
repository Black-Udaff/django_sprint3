from django.shortcuts import render
from django.http import HttpResponseNotFound
from blog.models import Post




def index(request):
    template = "blog/index.html"
    post_list = Post.objects.select_related(
        )
    context = {"post_list": post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = "blog/detail.html"
    for post in posts:
        if post['id'] == pk:
            context = {'post': post}
            return render(request, template, context)
    return HttpResponseNotFound("Пост не найден")


def category_posts(request, category_slug):
    template = "blog/category.html"
    context = {"category_slug": category_slug}
    return render(request, template, context)
