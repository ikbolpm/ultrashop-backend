# Generated by Django 2.2.4 on 2019-12-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_auto_20190121_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricelist', models.FileField(upload_to='pricelist')),
            ],
        ),
    ]
