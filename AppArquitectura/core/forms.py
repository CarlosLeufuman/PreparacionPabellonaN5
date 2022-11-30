from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria , Usuarios , Categoria2 , SolicitudEquipoeInsumos , PabellonEnCondiciones , Categoria3




class UsuarioForm(forms.ModelForm):

    class Meta: 
        model= Usuarios
        fields = ['nombre', 'email', 'numero', 'passs','dire','categoria2']
        labels ={
            'nombre': 'Nombre:', 
            'email': 'Email:', 
            'numero': 'Numero:', 
            'passs': 'Rut:',
            'dire': 'Dirección:',
            'categoria2': 'Sexo:',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre y Apellido', 
                    'id': 'nombre'
                }
            ), 
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Email (nick@gmail.com)', 
                    'id': 'email'
                }
            ), 
            'numero': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese numero EJ: 9 5432 1234', 
                    'id': 'numero'
                }
            ), 
            'passs': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese RUT EJ: 20418238-1',
                    'id': 'passs',
                }
            ),
            'dire': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su dirección',
                    'id': 'dire',
                }
            ),
            'categoria2': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria2',
                }
            )

        }




class  RegistrarPabellonForm(forms.ModelForm):

    class Meta: 
        model= PabellonEnCondiciones
        fields = ['n_pabellon', 'c_infra', 'c_equipo', 'c_rrhh','msg']
        labels ={
            'n_pabellon': 'Numero de pabellón:', 
            'c_infra': '¿Infraestructura en Condiciones?:', 
            'c_equipo': '¿Equipo e Insumos Disponibles?', 
            'c_rrhh': '¿RRHH Disponioble?:',
            'msg': 'Comentario Adicional:',
        }
        widgets={
            'n_pabellon': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Numero de Pabellón', 
                    'id': 'n_pabellon'
                }
            ), 
            'c_infra': forms.Select(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Infraestructura en condiciones?', 
                    'id': 'c_infra'
                }
            ), 
            'c_equipo': forms.Select(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Equipo a solicitar', 
                    'id': 'c_equipo'
                }
            ), 
            'c_rrhh': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Insumo a solicitar',
                    'id': 'c_rrhh',
                }
            ),
            'msg': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Comentario Adicional',
                    'id': 'msg',
                }
            )

        }


class SolicitudEIForm(forms.ModelForm):

    class Meta: 
        model= SolicitudEquipoeInsumos
        fields = ['n_pabellon', 'nombre', 'equipo', 'insumo','msg']
        labels ={
            'n_pabellon': 'Numero de pabellón:', 
            'nombre': 'Nombre de identificación:', 
            'equipo': 'Equipo a solicitar:', 
            'insumo': 'Insumo a solicitar:',
            'msg': 'Comentario Adicional:',
        }
        widgets={
            'n_pabellon': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Numero de Pabellón', 
                    'id': 'n_pabellon'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Nombre de Identificación', 
                    'id': 'nombre'
                }
            ), 
            'equipo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Equipo a solicitar', 
                    'id': 'equipo'
                }
            ), 
            'insumo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Insumo a solicitar',
                    'id': 'insumo',
                }
            ),
            'msg': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Comentario Adicional',
                    'id': 'msg',
                }
            )

        }



