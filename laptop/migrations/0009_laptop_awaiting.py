# Generated by Django 2.1.1 on 2019-04-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0008_laptop_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='awaiting',
            field=models.BooleanField(default=False),
        ),
    ]
