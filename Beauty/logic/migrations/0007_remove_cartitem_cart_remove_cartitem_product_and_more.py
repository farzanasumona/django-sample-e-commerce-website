# Generated by Django 4.1.2 on 2022-12-15 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0006_cart_alter_product_price_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
