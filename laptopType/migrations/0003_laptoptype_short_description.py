# Generated by Django 2.1 on 2018-10-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptopType', '0002_laptoptype_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptoptype',
            name='short_description',
            field=models.TextField(default='Ultrabuki'),
        ),
    ]