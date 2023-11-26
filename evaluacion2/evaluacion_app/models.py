from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator, MaxLengthValidator

# Create your models here.
class Reservas(models.Model):
    ESTADOS_RESERVA = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombrePersona = models.CharField(max_length=80, validators=[MaxLengthValidator(limit_value=80)])
    telefono = models.IntegerField()
    fechaReserva = models.DateField() 
    hora = models.TimeField()
    cantPersona = models.IntegerField()
    correoElectronico = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA)
    observacion = models.CharField(max_length=255, blank=True)