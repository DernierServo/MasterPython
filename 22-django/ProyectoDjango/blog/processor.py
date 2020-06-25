from blog.models import Category

def get_categories(request):

    # Similar a: SELECT id, title, slug FROM Page
    categories = Category.objects.values_list('id', 'name')

    return {
        'categories': categories
    }