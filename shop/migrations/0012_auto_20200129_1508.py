# Generated by Django 2.2.4 on 2020-01-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200129_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='part_number',
            field=models.CharField(blank=True, help_text='К примеру: 81XVS440S', max_length=30, null=True),
        ),
    ]