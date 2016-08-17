# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms.widgets import Select, Textarea, SelectMultiple
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
  class Meta:
    model = Obra
    fields = ('nombre','direccion', 'imagen', 'administrador')
    widgets = {
      'direccion': Textarea(attrs={'class': 'form-control',}),
      'administrador': SelectMultiple(attrs={'class': 'form-control',}),
    }
