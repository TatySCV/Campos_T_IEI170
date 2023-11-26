from django.shortcuts import render
from evaluacion_app.models import Reservas
from evaluacion_app.forms import FormReservas

# Create your views here.
def index(request):
    data = {"id": "20.733.436-7", "nombre": "Tatiana Campos", "correo": "tatiana.campos03@inacapmail.cl", "carrera": "Ingeniería en informática - 2023"}
    return render(request, 'index.html', data)

def listadoReservas(request):
    reservas = Reservas.objects.all()
    data = {'reserva': reservas}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormReservas()

    if(request.method == 'POST'):
        form = FormReservas(request.POST)
        if(form.is_valid()):
            form.save()
        return index(request)
    
    data = {'form': form}
    return render(request, 'agregar.html', data)