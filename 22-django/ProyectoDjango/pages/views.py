from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required


@login_required(login_url='n_login')    #Decorador para privatizar la vista de esta función
def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(
        request,
        'pages/page.html',
        {
            'page': page
        }
    )
