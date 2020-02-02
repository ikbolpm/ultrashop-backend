# Generated by Django 2.2.4 on 2020-01-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaptopPerks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='К примеру: Сенсорный экран', max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name': 'Perks',
                'verbose_name_plural': 'Perks',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LaptopType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Во множественном числе. К примеру: УльтрабукИ, трансформеры и т.д.', max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('name_singular', models.CharField(help_text='В единственном числе. К примеру: Ультрабук, трансформер и т.д.', max_length=200)),
                ('short_description', models.TextField(blank=True, default='Ultrabuki', null=True)),
                ('logo', models.ImageField(default='default.png', upload_to='laptop-types')),
            ],
            options={
                'verbose_name': 'Laptop Type',
            },
        ),
    ]
