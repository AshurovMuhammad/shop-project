# Generated by Django 4.2 on 2023-04-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_basket_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Telefon'),
        ),
    ]