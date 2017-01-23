from django.shortcuts import render
from django.http import HttpResponse
from . import models


def welcome(request):
    return HttpResponse("Hello MyBlog")


def index(request):
    article = models.Article.objects.get(pk=1)
    return render(request,'blog/index1.html', {'article': article})