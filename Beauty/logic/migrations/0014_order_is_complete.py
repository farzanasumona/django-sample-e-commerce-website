# Generated by Django 4.1.2 on 2023-01-22 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0013_alter_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]