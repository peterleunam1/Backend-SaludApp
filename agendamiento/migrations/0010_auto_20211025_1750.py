# Generated by Django 3.2.7 on 2021-10-25 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamiento', '0009_auto_20211025_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='password',
            new_name='contrasenia',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='username',
            new_name='nombres',
        ),
    ]