# Generated by Django 2.1.4 on 2018-12-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displaySize', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='displaysize',
            options={'ordering': ['size']},
        ),
        migrations.AlterField(
            model_name='displaysize',
            name='size',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
