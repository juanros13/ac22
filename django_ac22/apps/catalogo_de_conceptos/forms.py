# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms.widgets import Select, Textarea, SelectMultiple, CheckboxSelectMultiple, TextInput
from apps.catalogo_de_conceptos.models import Agrupador, Concepto

class AgrupadorAddForm(forms.ModelForm):
  clave = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Nombre del edificio',
      }
    ), 
    label = "Clave",
    required=True
  )
  class Meta:
    model = Agrupador
    fields = ('clave','descripcion','parent')
    widgets = {
      'parent': Select(attrs={'class': 'form-control',}),
      'descripcion': Textarea(attrs={'class': 'form-control',}),
    }

class ConceptoAddForm(forms.ModelForm):
  clave = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Nombre del edificio',
      }
    ), 
    label = "Clave",
    required=True
  )
  cantidad = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'type': 'number',
        'step': '0.01',
        'value': '0.00',
        'placeholder':'0.00'
      }
    ), 
    label = "Cantidad",
    required=True
  )
  unidad = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Nombre del edificio',
      }
    ), 
    label = "Unidad",
    required=True
  )
  precio_unitario = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'type': 'number',
        'step': '0.01',
        'value': '0.00',
        'placeholder':'0.00'
      }
    ), 
    label = "Precio Unitario",
    required=True
  )
  class Meta:
    model = Concepto
    fields = ('clave','concepto','agrupador', 'unidad', 'cantidad', 'precio_unitario')
    widgets = {
      'agrupador': Select(attrs={'class': 'form-control',}),
      'concepto': Textarea(attrs={'class': 'form-control',}),
    }
