# Generated by Django 2.2.4 on 2019-11-21 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptopType', '0003_laptoptype_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptoptype',
            name='isLaptop',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
