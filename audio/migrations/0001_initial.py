# Generated by Django 2.1.1 on 2018-09-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='К примеру: Bang & Olufsen Play', max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Audio',
            },
        ),
    ]
