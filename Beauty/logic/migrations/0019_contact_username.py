# Generated by Django 4.1.2 on 2023-01-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0018_remove_contact_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(default='default', max_length=100),
        ),
    ]