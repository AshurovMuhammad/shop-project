from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path("products/<int:category_id>", views.products, name='category'),
    path("products/page/<int:page>", views.products, name='page'),
    path('products/basket-add/<int:product_id>', views.basket_add, name='basket_add'),

    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("removecart/", views.remove_cart),

    path('products/basket/thanks/', views.thanks_page, name="thanks_page"),
]