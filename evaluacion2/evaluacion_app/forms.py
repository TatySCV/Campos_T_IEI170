from django import forms
from evaluacion_app.models import Reservas
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class FormReservas(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'

    def clean_nombrePersona(self):
        nombre_persona = self.cleaned_data['nombrePersona']
        if len(nombre_persona) > 80:
            raise forms.ValidationError('El nombre de la persona no puede superar los 80 caracteres.')
        return nombre_persona

    def clean_cantPersona(self):
        cant_persona = self.cleaned_data['cantPersona']
        if not 1 <= cant_persona <= 15:
            raise forms.ValidationError('La cantidad de personas debe estar entre 1 y 15.')
        return cant_persona

    def clean_correoElectronico(self):
        correo_electronico = self.cleaned_data['correoElectronico']
        try:
            validate_email(correo_electronico)
        except ValidationError:
            raise ValidationError('Ingrese una dirección de correo electrónico válida.')        
        return correo_electronico