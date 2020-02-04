# Generated by Django 2.2.4 on 2020-02-03 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20200203_1729'),
        ('orders', '0002_auto_20200126_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('NOT_CONTACTED', 'Not Contacted'), ('ATTEMPTED_TO_CONTACT', 'Attempted to Contact'), ('ASKED_TO_CALL_LATER', 'Asked to Call Later'), ('DECISION_MAKING', 'Decision Making'), ('CLOSED_WON', 'Closed Won'), ('CLOSED LOST', 'Closed Lost')], default='NOT_CONTACTED', max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquired_product', to='shop.Product')),
            ],
            options={
                'verbose_name_plural': 'Inquiries',
            },
        ),
    ]
