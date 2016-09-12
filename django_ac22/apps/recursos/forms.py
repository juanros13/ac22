# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms.widgets import Select, Textarea, SelectMultiple, CheckboxSelectMultiple, TextInput
from apps.recursos.models import Recurso

class RecursoAddForm(forms.ModelForm):
  nombre = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Nombre',
      }
    ), 
    label = "Nombre",
    required=False
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
    required=False
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
    label = "Precio unitario",
    required=False
  )
  class Meta:
    model = Recurso
    fields = ('nombre','tipo', 'cantidad','unidad', 'precio_unitario')
    widgets = {
      'tipo': Select(attrs={'class': 'form-control',}),
      'unidad': Select(attrs={'class': 'form-control selectpicker',}),
    }