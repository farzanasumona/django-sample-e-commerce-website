# Generated by Django 4.1.2 on 2022-12-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0008_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='logic.product'),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
