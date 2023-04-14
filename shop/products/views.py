from django.shortcuts import render
from .models import Product, ProductCategory
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    context = {
        'title': "Market Place"
    }
    return render(request, 'products/index.html', context=context)


def products(request, category_id=None):
    context = {
        'title': "Market Place - Catalog",
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)  # saifada 3 dona tavarni ko'rsatadi
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({"products": page_obj})
    return render(request, 'products/products.html', context=context)
