from blog.models import Category, Article

def get_categories(request):

    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    # Similar a: SELECT id, name FROM Category
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')

    return {
        'categories': categories,
        'ids': categories_in_use
    }