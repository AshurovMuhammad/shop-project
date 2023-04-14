from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': "Market Place"
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': "Market Place - Catalog"
    }
    return render(request, 'products/products.html', context=context)
