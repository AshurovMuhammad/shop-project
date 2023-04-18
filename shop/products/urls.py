from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path("products/<int:category_id>", views.products, name='category'),
    path("products/page/<int:page>", views.products, name='page'),
    path('products/basket-add/<int:product_id>', views.basked_add, name='basket_add'),
    path('products/basket-minus/<int:product_id>', views.basked_minus, name='basket_minus'),
    path('products/basket-delete/<int:id>', views.basket_delete, name='basket_delete'),
    path('products/basket/thanks/', views.thanks_page, name="thanks_page"),
]