# Generated by Django 2.1.4 on 2018-12-16 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_sales_sold_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='sold_by',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]