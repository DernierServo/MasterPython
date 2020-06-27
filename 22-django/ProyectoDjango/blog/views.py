from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required


@login_required(login_url='n_login')    #Decorador para privatizar la vista de esta función
def list(request):

    # Sacar artículos
    articles = Article.objects.all()

    # Paginar los artículos
    paginator = Paginator(articles, 2)  #ds: 2do parámetro es el número de objetos (artículos) por página.

    # Recoger número página
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(
        request,
        'articles/list.html',
        {
            'title': 'Artículos',
            'articles': page_articles
        }
    )


@login_required(login_url='n_login')    #Decorador para privatizar la vista de esta función
def category(request, p_category_id):
    category = get_object_or_404(Category, id=p_category_id)
    articles = Article.objects.filter(categories=p_category_id)

    return render(
        request,
        'categories/category.html',
        {
            'category': category,
            'articles': articles
        }
    )


@login_required(login_url='n_login')    #Decorador para privatizar la vista de esta función
def article(request, p_article_id):

    article = get_object_or_404(Article, id=p_article_id)

    return render(
        request,
        'articles/detail.html',
        {
            'article': article
        }
    )