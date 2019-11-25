# Generated by Django 2.2.4 on 2019-11-17 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processor', '0006_auto_20191105_1440'),
        ('ram', '0001_initial'),
        ('resolution', '0001_initial'),
        ('displaySize', '0002_auto_20181211_1354'),
        ('audio', '0001_initial'),
        ('graphicsCard', '0002_auto_20181211_1354'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='upc',
            field=models.CharField(help_text='Отсканируйте баркод', max_length=12, unique=True),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Product')),
                ('ram', models.IntegerField()),
                ('ssd', models.IntegerField(blank=True, null=True)),
                ('hdd', models.IntegerField(blank=True, null=True)),
                ('graphics_card_memory', models.IntegerField(blank=True, help_text='В ГГБ. К примеру 2 или 4', null=True)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_audio', to='audio.Audio')),
                ('graphics_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laptop_graphics_card', to='graphicsCard.GraphicsCard')),
                ('processor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_processor', to='processor.Processor')),
                ('ram_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_ram_type', to='ram.Ram')),
                ('resolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_resolution', to='resolution.Resolution')),
                ('screen_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laptop_screen_size', to='displaySize.DisplaySize')),
            ],
            bases=('shop.product',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='images/products/productimages/%Y-%m-%d/')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='shop.Product')),
            ],
        ),
    ]
