# Generated by Django 3.2.7 on 2021-10-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citasmedicas',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
