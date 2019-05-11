from django.shortcuts import render
from article import models

# Create your views here.
def Homepage(request):
    return render(request, 'article/myblog.html')

def aricle_list(request):
    articles = models.ArticlePost.objects.all()
    content = {'articles': articles}
    return render(request, 'article/list.html', content)

def article_detail(request, id):
    article = models.ArticlePost.objects.get(id=id)
    content = {'article': article}
    return render(request, 'article/detail.html', content)