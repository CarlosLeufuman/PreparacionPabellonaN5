from django.shortcuts import render , redirect
from django.views.decorators import csrf
from .models import  Usuarios , SolicitudEquipoeInsumos , PabellonEnCondiciones
from .forms import   UsuarioForm , SolicitudEIForm , RegistrarPabellonForm

# Create your views here.

def SoluProblemInfra(request):
    return render(request, 'SoluProblemInfra.html')

def SoluBrevedadRRHH(request):
    return render(request, 'SoluBrevedadRRHH.html')

def SoluBrevedadInsumos(request):
    return render(request, 'SoluBrevedadInsumos.html')

def SoluBrevedadInfra(request):
    return render(request, 'SoluBrevedadInfra.html')

def InformarEquipoQuirurgico(request):
    return render(request, 'InformarEquipoQuirurgico.html')

def preparacionpabellon(request):
    return render(request, 'preparacionpabellon.html')

def fase_quirurgica(request):
    return render(request, 'fase_quirurgica.html')

def index1(request):
    return render(request, 'index1.html')

def SoliRRHH(request):
    return render(request, 'SoliRRHH.html')

def form_equipo_insumo(request):                             
    if request.method== 'POST':
        solicitudei_form = SolicitudEIForm(request.POST)

        if solicitudei_form.is_valid():
            solicitudei_form.save()
            return redirect ('preparacionpabellon')

    else:
        solicitudei_form = SolicitudEIForm()
    return render(request, 'SoliEquipoInsu.html' ,{'solicitudei_form': solicitudei_form })



def form_registrar_pabellon(request):                             
    if request.method== 'POST':
        registrar_pabellon_form = RegistrarPabellonForm(request.POST)

        if registrar_pabellon_form.is_valid():
            registrar_pabellon_form.save()
            return redirect ('mostrar_pabellon')

    else:
        registrar_pabellon_form = RegistrarPabellonForm()
    return render(request, 'RegistrarPabellon.html' ,{'registrar_pabellon_form': registrar_pabellon_form })


def mostrar_pabellon(request):
    pabellonencondiciones = PabellonEnCondiciones.objects.all()
    datos3 = {
        'pabellonencondiciones': pabellonencondiciones
    }
    return render(request, 'mostrar_pabellon.html',datos3)


def form_del_pabellon(request,id):
    pabellonencondiciones = PabellonEnCondiciones.objects.get(n_pabellon=id)
    pabellonencondiciones.delete()
    return redirect('mostrar_pabellon')





