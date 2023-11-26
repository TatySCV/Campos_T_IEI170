from django.db import models

# Create your models here.
class Reservas(models.Model):
    ESTADOS_RESERVA = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombrePersona = models.CharField(max_length=100)
    telefono = models.IntegerField()
    fechaReserva = models.DateField() 
    hora = models.TimeField()
    cantPersona = models.IntegerField()
    correoElectronico = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA)
    observacion = models.CharField(max_length=255)