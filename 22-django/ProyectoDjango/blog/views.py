from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article

# Create your views here.
def list(request):

    articles = Article.objects.all()

    return render(
        request,
        'articles/list.html',
        {
            'title': 'Artículos',
            'articles': articles
        }
    )


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