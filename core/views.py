from django.shortcuts import render, redirect
from .form import ArticleForm
from .models import Article
# Create your views here.

def home(request):
    article_obj = Article.objects.all()
    context = {
        'articles' : article_obj
    }
    return render(request, 'core/index.html', context)


def writeArticle(request):
    context = {}
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
           instance = form.save(commit = False)
           instance.save()
           return redirect('home-view')
        print(form.errors)
    else:
        form = ArticleForm()

    context['form'] = form
    return render(request, 'core/create.html', context)