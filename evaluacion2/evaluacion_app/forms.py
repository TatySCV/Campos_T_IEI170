from django import forms
from evaluacion_app.models import Reservas

class FormReservas(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'