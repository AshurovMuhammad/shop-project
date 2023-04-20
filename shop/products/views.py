from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Product, ProductCategory, Basket
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from telebot.sendmessage import send_telegram


# Create your views here.
def index(request):
    context = {
        'title': "Market Place"
    }
    return render(request, 'products/index.html', context=context)


def products(request, category_id=None):
    search_query = request.GET.get("search", "")
    context = {
        'title': "Market Place - Catalog",
        'categories': ProductCategory.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        if search_query:
            products = Product.objects.filter(
                Q(name__icontains=search_query) | Q(short_description__icontains=search_query))
        else:
            products = Product.objects.all()
    paginator = Paginator(products, 6)  # saifada 3 dona tavarni ko'rsatadi
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({"products": page_obj})
    return render(request, 'products/products.html', context=context)


@login_required
def basket_add(request, product_id):
    current_page = 'profile'
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return redirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return redirect(current_page)


def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Basket.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        baskets = Basket.objects.filter(user=user)

        one_price = 0
        for res in baskets:
            one_price = res.sum()
        total_quantity = sum(basket.quantity for basket in baskets)
        total_price = sum(basket.sum() for basket in baskets)

        data = {
            'quantity': c.quantity,
            'total_price': total_price,
            'total_quantity': total_quantity,
            "one_price": one_price,
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Basket.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        user = request.user
        baskets = Basket.objects.filter(user=user)

        one_price = 0
        for res in baskets:
            one_price = res.sum()
        total_quantity = sum(basket.quantity for basket in baskets)

        total_price = sum(basket.sum() for basket in baskets)

        data = {
            'quantity': c.quantity,
            'total_quantity': total_quantity,
            "one_price": one_price,
            'total_price': total_price,
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Basket.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.delete()
        user = request.user
        baskets = Basket.objects.filter(user=user)

        one_price = 0
        for res in baskets:
            one_price = res.sum()
        total_quantity = sum(basket.quantity for basket in baskets)

        total_price = sum(basket.sum() for basket in baskets)

        data = {
            'quantity': c.quantity,
            'total_quantity': total_quantity,
            "one_price": one_price,
            'total_price': total_price,
        }
        return JsonResponse(data)


def thanks_page(request):
    user = request.user
    baskets = Basket.objects.filter(user=user)
    name = user.first_name
    phone = user.phone
    res = ""
    for basket in baskets:
        pr_name = basket.product.name
        quantity = str(basket.quantity)
        ls = f"\n{pr_name} - {quantity} dona"
        res += ls
    send_telegram(tg_name=name, tg_phone=phone, tg_order=res)
    context = {
        "title": "Raxmat"
    }

    return render(request, 'products/thanks.html', context=context)
