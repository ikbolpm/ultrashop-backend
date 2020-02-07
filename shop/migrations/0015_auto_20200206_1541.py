# Generated by Django 2.2.4 on 2020-02-06 10:41

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('productconfig', '0003_auto_20200206_1541'),
        ('shop', '0014_auto_20200203_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='allinone',
            name='desktop_type',
            field=models.ManyToManyField(to='productconfig.AllInOneType'),
        ),
        migrations.AddField(
            model_name='desktop',
            name='desktop_type',
            field=models.ManyToManyField(to='productconfig.DesktopType'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='laptop_type',
            field=models.ManyToManyField(to='productconfig.LaptopType'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='perks',
            field=models.ManyToManyField(to='productconfig.ComputerPerk'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='title', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.PositiveIntegerField(help_text='скорость печати за 1 минуту', max_length=4)),
                ('description', tinymce.models.HTMLField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productconfig.PrinterColorType')),
                ('formats', models.ManyToManyField(to='productconfig.PrinterFormat')),
                ('functions', models.ManyToManyField(to='productconfig.PrinterFunction')),
                ('perks', models.ManyToManyField(to='productconfig.PrinterPerks')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productconfig.PrinterTechnologyType')),
            ],
        ),
    ]
