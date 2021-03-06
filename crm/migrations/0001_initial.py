# Generated by Django 2.1.4 on 2018-12-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_or_im', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('NOT_CONTACTED', 'Not Contacted'), ('ATTEMPTED_TO_CONTACT', 'Attempted to Contact'), ('ASKED_TO_CALL_LATER', 'Asked to Call Later'), ('DECISION_MAKING', 'Decision Making'), ('CLOSED_WON', 'Closed Won'), ('CLOSED LOST', 'Closed Lost')], default='NOT_CONTACTED', max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='lead',
            unique_together={('name', 'phone_or_im')},
        ),
    ]
