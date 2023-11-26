from django.shortcuts import redirect, render
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

    if request.method == 'POST':
        form = FormReservas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reservas')

    data = {'form': form}
    return render(request, 'agregar.html', data)

def eliminarReserva(request, IN_id):
    reserva = Reservas.objects.get(id = IN_id)
    reserva.delete()
    return redirect('/reservas')

def modificarReserva(request, IN_id):
    reserva = Reservas.objects.get(id=IN_id)
    form = FormReservas(instance=reserva)

    if request.method == 'POST':
        form = FormReservas(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('/reservas')

    data = {'form': form}
    return render(request, 'agregar.html', data)