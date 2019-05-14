from django.shortcuts import render, redirect
from django.http import HttpResponse
from article import models
from .forms import ArticlePostForm
from django.contrib.auth.models import User
import markdown


# Create your views here.
def Homepage(request):
    return render(request, 'article/myblog.html')

def aricle_list(request):
    articles = models.ArticlePost.objects.all()
    content = {'articles': articles}
    return render(request, 'article/list.html', content)

def article_detail(request, id):
    article = models.ArticlePost.objects.get(id=id)

    #将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
         extensions=[
             # 包含 缩写、表格等常用扩展
             'markdown.extensions.extra',
             # 语法高亮扩展
             'markdown.extensions.codehilite',
         ])
    content = {'article': article}
    return render(request, 'article/detail.html', content)

def article_create(request):
    #用户提交数据
    if request.method == "POST":
        #将提交的数据赋值给表单实例
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            #将新文章保存至数据库
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    #用户请求数据
    else:
        #创建表单类实例
        article_post_form = ArticlePostForm()
        content = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', content)


def article_delete(request,id):
    article = models.ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article_list")


def article_update(request, id):
    #获取需要修改的文章对象
    article = models.ArticlePost.objects.get(id=id)
    if request.method=="POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("表单内容有误，请重新填写")
    else:
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = {'article': article, 'article_post_form': article_post_form}
        return render(request, 'article/update.html', context)