# Generated by Django 2.2.4 on 2019-11-24 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='url',
            field=models.CharField(max_length=300),
        ),
    ]
