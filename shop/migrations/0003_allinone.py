# Generated by Django 2.2.4 on 2019-12-20 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resolution', '0001_initial'),
        ('processor', '0006_auto_20191105_1440'),
        ('displaySize', '0002_auto_20181211_1354'),
        ('graphicsCard', '0002_auto_20181211_1354'),
        ('audio', '0001_initial'),
        ('ram', '0001_initial'),
        ('shop', '0002_auto_20191117_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllInOne',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Product')),
                ('ram', models.IntegerField()),
                ('ssd', models.IntegerField(blank=True, null=True)),
                ('hdd', models.IntegerField(blank=True, null=True)),
                ('graphics_card_memory', models.IntegerField(blank=True, help_text='В ГГБ. К примеру 2 или 4', null=True)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aio_audio', to='audio.Audio')),
                ('graphics_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aio_graphics_card', to='graphicsCard.GraphicsCard')),
                ('processor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aio_processor', to='processor.Processor')),
                ('ram_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aio_ram_type', to='ram.Ram')),
                ('resolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aio_resolution', to='resolution.Resolution')),
                ('screen_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aio_screen_size', to='displaySize.DisplaySize')),
            ],
            bases=('shop.product',),
        ),
    ]
