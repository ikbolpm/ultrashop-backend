# Generated by Django 2.2.4 on 2020-01-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_allinone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(blank=True, help_text='Старая цена. Оставьте 0 если не идет акция', null=True),
        ),
    ]
