# Generated by Django 2.1.4 on 2018-12-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_auto_20181216_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
