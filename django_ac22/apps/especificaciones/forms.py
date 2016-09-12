# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms.widgets import Select, Textarea, SelectMultiple, CheckboxSelectMultiple, TextInput
from apps.especificaciones.models import Especificaciones

class EspecificacionesAddForm(forms.ModelForm):
  nombre_documento = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Documento',
      }
    ), 
    label = "Nombre del documento",
    required=False
  )
  contenido = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Contenido',
      }
    ), 
    label = "Contenido",
    required=True
  )
  nombre_anexo = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Nombre anexo',
      }
    ), 
    label = "Nombre anexo",
    required=False
  )
  class Meta:
    model = Especificaciones
    fields = ('nombre_documento','contenido','nombre_anexo','anexo', 'parent','tipo_propuesta')
    widgets = {
      'tipo_propuesta': Select(attrs={'class': 'form-control',}),
      'parent': Select(attrs={'class': 'form-control',}),
    }