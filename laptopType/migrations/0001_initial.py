# Generated by Django 2.1.1 on 2018-09-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',
                 models.CharField(help_text='Во множественном числе. К примеру: УльтрабукИ, трансформеры и т.д.',
                                  max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('name_singular',
                 models.CharField(help_text='В единственном числе. К примеру: Ультрабук, трансформер и т.д.',
                                  max_length=200)),
            ],
            options={
                'verbose_name': 'Laptop Type',
            },
        ),
    ]
