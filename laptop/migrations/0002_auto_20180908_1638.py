# Generated by Django 2.1.1 on 2018-09-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(upload_to='laptop_images/%Y-%m-%d/'),
        ),
    ]
