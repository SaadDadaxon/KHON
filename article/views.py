from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, Http404, redirect, reverse
from .models import Article
from .forms import ArticleForm
import random
from django.contrib import messages


def _index(request):
    _id = random.randint(1, 4)
    article = Article.objects.get(id=_id)
    title = article.title
    content = article.content
    HTML_Content = f"""
    <h1>{title} (id:{article.id})<h1>
    <p>{content}<p>
"""
    return HttpResponse(HTML_Content)


def index(request):
    articles = Article.objects.filter(is_deleted__exact=False)
    q = request.GET.get('q')
    if q is not None:
        articles = articles.filter(title__icontains=q)
    return render(request, 'article/index.html', {'object_list': articles})


def detail(request, slug):
    if slug:
        article = Article.objects.get(slug=slug)
        context = {
            'object': article
        }
        return render(request, 'article/detail.html', context)
    return Http404


def create_1(request):
    context = {
        'created': False
    }
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        context['object'] = article
        context['created'] = True
    return render(request, 'article/create.html', context)


def create_2(request):
    form = ArticleForm
    context = {
        'form': form
    }
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Mr.{request.user} siz Muvaffaqiyatli Kirdingiz')
            context['object'] = form.data
            context['created'] = True
    return render(request, 'article/create.html', context)


@login_required
def create(request):
    form = ArticleForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, f'Mr.{request.user} siz Muvaffaqiyatli Article Yaratdingiz')
        return redirect('article:list')
    context = {
        'form': form
    }
    return render(request, 'article/create.html', context)


def newcreate_1(request):
    context = {

    }
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        context['object'] = article
        return redirect('article:list')
    return render(request, 'article/NewCreate.html', context)


def newcreate_2(request):
    form = ArticleForm
    context = {
        'form': form
    }
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            context['object'] = form.data
            context['created'] = True
            return redirect('article:list')

    return render(request, 'article/NewCreate.html', context)


@login_required
def newcreate(request):
    form = ArticleForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, f'Mr.{request.user} siz Muvaffaqiyatli Yangiz Article Yaratdingiz')
        return redirect('article:list')
    context = {
        'form': form
    }
    return render(request, 'article/NewCreate.html', context)


def edit_1(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(data=request.POST, instance=article)
        form.save()
        return redirect(reverse('article:detail', kwargs={'pk': article.id}))
    ctx = {
        'form': form
    }
    return render(request, "article/edit.html", ctx)


def edit_2(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(data=request.POST, instance=article)
        form.save()
        return redirect(reverse('article:detail', kwargs={'pk': article.id}))

    ctx = {
        'form': form
    }
    return render(request, 'article/edit.html', ctx)


def delete_1(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        article.delete()
        return redirect('article:list')
    ctx = {
        'object': article
    }
    return render(request, 'article/delete.html', ctx)


def edit_3(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(data=request.POST, instance=article)
        form.save()
        return redirect(reverse('article:detail', kwargs={'pk': article.id}))
    ctx = {
        'form': form
    }
    return render(request, 'article/edit.html', ctx)


@login_required
def delete(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == "POST":
        # article.delete()
        article.is_deleted = True
        article.save()
        return redirect('article:list')
    context = {
        'object': article
    }
    return render(request, 'article/delete.html', context)


@login_required
def edit(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(data=request.POST, instance=article, files=request.FILES)
        form.save()
        messages.success(request, f"Mr.{request.user} siz Muvaffaqiyatli O'zgarishni Amalga Oshirdingiz")
        return redirect(reverse('article:detail', kwargs={'slug': article.slug}))
    context = {
        'form': form
    }
    return render(request, 'article/edit.html', context)


@login_required
def delete_2(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        article.is_deleted = True
        article.save()
        messages.success(request, f"Mr.{request.user} siz Muvaffaqiyatli O'chirdingiz")
        return redirect('article:list')
    context = {
        'object': article
    }
    return render(request, 'article/delete.html', context)


def new_index(request):
    articles = Article.objects.filter(is_deleted=False).order_by('-slug')
    q = request.GET.get('q')
    if q is not None:
        articles = articles.filter(title__icontains=q)
    return render(request, 'article/newedit.html', {'object_list': articles})

















