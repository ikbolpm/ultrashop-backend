# Generated by Django 2.2.4 on 2020-01-25 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_laptop_optane'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='awaiting',
        ),
    ]
