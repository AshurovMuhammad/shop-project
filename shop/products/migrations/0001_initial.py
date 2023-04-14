# Generated by Django 4.2 on 2023-04-14 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Kategoriya')),
                ('description', models.TextField(blank=True, verbose_name='Kategoriya tavsifi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Mahsulot nomi')),
                ('image', models.ImageField(blank=True, upload_to='products_images', verbose_name='Rasm')),
                ('description', models.TextField(blank=True, verbose_name='Mahsulot tavsifi')),
                ('short_description', models.CharField(blank=True, max_length=100, verbose_name='Qisqa tavsifi')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Narxi')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Miqdori')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='Kategoriya')),
            ],
            options={
                'verbose_name': 'Mahsulot',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
    ]