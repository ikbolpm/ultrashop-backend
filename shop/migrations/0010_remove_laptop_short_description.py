# Generated by Django 2.2.4 on 2020-01-27 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_laptop_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='short_description',
        ),
    ]