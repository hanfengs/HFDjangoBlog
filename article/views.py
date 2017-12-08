from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from article.models import *

# Create your views here.本质是函数，类似Controller

#HttpRequest；1有请求；2有返回
def hello(request):

    #返回 HttpRequest
    return HttpResponse("Hello World, QuXue_Django")

# def home(request):
#     return HttpResponse("home_首页")


def test(request):
    #给html中传递参数
    list_book = Book.objects.all()
    # list_article = Article.objects.all()
    context = {'title': 'Book列表', 'list_article': list_book, 'current_time': datetime.now()}
    return render(request, 'test.html', context)


def detail(request, id):
    list = Book.objects.get(id = id).article_set.all()
    context = {'title': 'Article列表', 'list_article': list, 'current_time': datetime.now()}
    return render(request, 'test.html', context)


def home(request):
    list_book = Book.objects.all()
    context = {'post_list' : list_book}
    return render(request, 'home.html', context)
