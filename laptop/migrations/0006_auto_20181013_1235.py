# Generated by Django 2.1.2 on 2018-10-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0005_merge_20181011_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='viewed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]