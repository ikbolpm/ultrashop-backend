# Generated by Django 2.1.4 on 2018-12-11 09:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0006_auto_20181013_1235'),
        ('crm', '0002_lead_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='interested_in',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='laptop.Laptop'),
            preserve_default=False,
        ),
    ]