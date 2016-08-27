# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms.widgets import Select, Textarea, SelectMultiple, CheckboxSelectMultiple, TextInput
from apps.obras.models import Obra

class ObraAddForm(forms.ModelForm):
  nombre = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Nombre del edificio',
      }
    ), 
    label = "Nombre",
    required=True
  )
  fecha_inicio = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix date-picker',
        'placeholder' : 'Fecha inicio',
      }
    ), 
    label = "Fecha inicio",
    required=True
  )
  fecha_termino = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix date-picker',
        'placeholder' : 'Fecha termino',
      }
    ), 
    label = "Fecha termino",
    required=True
  )
  class Meta:
    model = Obra
    fields = ('nombre','direccion', 'imagen', 'administrador', 'estado', 'fecha_inicio', 'fecha_termino')
    widgets = {
      'direccion': Textarea(attrs={'class': 'form-control',}),
      'estado': Select(attrs={'class': 'form-control',}),
      'administrador': CheckboxSelectMultiple(attrs={'class': 'form-control radio-list',}),
    }
