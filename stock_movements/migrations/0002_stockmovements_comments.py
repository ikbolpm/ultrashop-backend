# Generated by Django 2.1.4 on 2018-12-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_movements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmovements',
            name='comments',
            field=models.TextField(blank=True, help_text='Дополнительные комментарии. Например кому отдали, за сколько и т.д.', null=True),
        ),
    ]