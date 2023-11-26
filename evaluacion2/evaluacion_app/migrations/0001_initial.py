# Generated by Django 4.2.5 on 2023-11-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('fechaReserva', models.DateField()),
                ('hora', models.TimeField()),
                ('cantPersona', models.IntegerField()),
                ('correoElectronico', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], max_length=20)),
                ('observacion', models.CharField(max_length=255)),
            ],
        ),
    ]
