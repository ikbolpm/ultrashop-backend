# Generated by Django 2.2.4 on 2019-11-25 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0012_laptop_black_friday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='black_friday',
            new_name='on_sale',
        ),
    ]
