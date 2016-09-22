# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.forms.widgets import Select, Textarea
from apps.proveedores.models import Proveedor

class ProveedorAddForm(forms.ModelForm):
  nombre = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el nombre',
      }
    ), 
    label = "Nombre",
  )
  telefono = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el telefono',
      }
    ), 
    label = "Telefono",
  )
  
  rfc = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el RFC',
      }
    ), 
    label = "RFC",
  )
  ciudad = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el ciudad',
      }
    ), 
    label = "Ciudad",
  )
  codigo_postal = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el codigo postal',
      }
    ), 
    label = "Codigo postal",
  )
  class Meta:
    model = Proveedor
    fields = ('nombre','telefono','direccion','rfc','ciudad','codigo_postal')
    widgets = {
      'direccion': Textarea(
        attrs={
          'class': 'form-control',
          'rows' : '8',
        }
      ),
    }
    
