# Generated by Django 2.1.5 on 2019-01-20 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_customerreturns'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerreturns',
            options={'verbose_name': 'Sales Return', 'verbose_name_plural': 'Sales Returns'},
        ),
    ]
