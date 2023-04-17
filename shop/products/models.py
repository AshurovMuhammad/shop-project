from django.db import models
from users.models import User


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Kategoriya")
    description = models.TextField(blank=True, verbose_name="Kategoriya tavsifi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="Mahsulot nomi")
    image = models.ImageField(upload_to="products_images", blank=True, verbose_name="Rasm")
    description = models.TextField(blank=True, verbose_name="Mahsulot tavsifi")
    short_description = models.CharField(max_length=100, blank=True, verbose_name="Qisqa tavsifi")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Narxi")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Miqdori")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Kategoriya")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_database = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}ning savati | Maxsulot {self.product.name}"

    def sum(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = 'Savatdagi maxsulot'
        verbose_name_plural = 'Savatdagi maxsulotlar'
