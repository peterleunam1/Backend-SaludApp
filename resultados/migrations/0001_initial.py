# Generated by Django 3.2.7 on 2021-10-05 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamenMedico',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Examenes medicos',
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('muestra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('valoracion', models.CharField(max_length=200)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamiento.especialidad')),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.examenmedico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamiento.usuario')),
            ],
            options={
                'verbose_name_plural': 'Resultados de Laboratorio',
            },
        ),
    ]
