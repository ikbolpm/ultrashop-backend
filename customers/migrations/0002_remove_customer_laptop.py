# Generated by Django 2.1.4 on 2018-12-08 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='laptop',
        ),
    ]