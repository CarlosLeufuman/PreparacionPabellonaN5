from django.urls import path 
from .views import  index1, fase_quirurgica, preparacionpabellon, InformarEquipoQuirurgico , SoluBrevedadInsumos,SoluBrevedadInfra,SoluProblemInfra, SoluBrevedadRRHH,SoliRRHH, form_equipo_insumo,form_registrar_pabellon, mostrar_pabellon,form_del_pabellon   


urlpatterns = [
    path('', index1, name="index1"),
    path('fase_quirurgica', fase_quirurgica, name="fase_quirurgica"),
    path('preparacionpabellon', preparacionpabellon, name="preparacionpabellon"),
    path('InformarEquipoQuirurgico', InformarEquipoQuirurgico, name="InformarEquipoQuirurgico"),
    path('SoluBrevedadInsumos',SoluBrevedadInsumos, name="SoluBrevedadInsumos"),
    path('SoluBrevedadInfra',SoluBrevedadInfra, name="SoluBrevedadInfra"),
    path('SoluBrevedadRRHH',SoluBrevedadRRHH, name="SoluBrevedadRRHH"),
    path('form_equipo_insumo',form_equipo_insumo, name="form_equipo_insumo"),
    path('form_registrar_pabellon',form_registrar_pabellon, name="form_registrar_pabellon"),
    path('SoliRRHH',SoliRRHH, name="SoliRRHH"),
    path('SoluProblemInfra',SoluProblemInfra, name="SoluProblemInfra"),
    path('mostrar_pabellon',mostrar_pabellon, name="mostrar_pabellon"),
    path('form_del_pabellon',form_del_pabellon, name="form_del_pabellon"),



    




 ]