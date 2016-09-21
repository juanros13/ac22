# -*- encoding: utf-8 -*-
from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields, models, formsets, widgets
from django.forms.widgets import Select, Textarea, SelectMultiple, CheckboxSelectMultiple, TextInput
from apps.gestion_financiera.models import Ingreso, Gasto, GastoDetalle, Transferencia, Cuenta


class IngresoAddForm(forms.ModelForm):
  fecha = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix  date-picker',
        'placeholder' : 'Fecha',
      }
    ), 
    label = "Fecha",
    required=True
  )

  concepto = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Concepto',
      }
    ), 
    label = "Concepto",
    required=True
  )
  referencia = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Referencia',
      }
    ), 
    label = "Referencia",
    required=True
  )
  monto = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'type': 'number',
        'step': '0.01',
        'value': '0.00',
        'placeholder':'0.00'
      }
    ), 
    label = "Monto",
    required=True
  )
  class Meta:
    model = Ingreso
    fields = ('fecha','metodo_pago', 'concepto','referencia','monto','comentario','cuenta')
    widgets = {
      'metodo_pago': Select(attrs={'class': 'form-control',}),
      'comentario': Textarea(attrs={'class': 'form-control',}),
      'cuenta': Select(attrs={'class': 'form-control',}),
    }

class GastoAddForm(forms.ModelForm):
  fecha = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix  date-picker',
        'placeholder' : 'Fecha',
      }
    ), 
    label = "Fecha",
    required=True
  )

  class Meta:
    model = Gasto
    fields = ('fecha','metodo_pago', 'cuenta')
    widgets = {
      'metodo_pago': Select(attrs={'class': 'form-control',}),
      #'comentario': Textarea(attrs={'class': 'form-control',}),
      'cuenta': Select(attrs={'class': 'form-control',}),
    }

class GastoDetalleAddForm(forms.ModelForm):
  concepto = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'placeholder' : 'Concepto',
      }
    ), 
    label = "Concepto",
    required=True
  )
  monto = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'type': 'number',
        'step': '0.01',
        'value': '0.00',
        'placeholder':'0.00'
      }
    ), 
    label = "Monto",
    required=True
  )
  class Meta:
    model = GastoDetalle
    fields = ('concepto', 'monto', 'obra')
    widgets = {
      'obra': Select(attrs={'class': 'form-control',}),
    }

class TransferenciaAddForm(forms.ModelForm):
  fecha = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix  date-picker',
        'placeholder' : 'Fecha',
      }
    ), 
    label = "Fecha",
    required=True
  )
  monto = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'type': 'number',
        'step': '0.01',
        'value': '0.00',
        'placeholder':'0.00'
      }
    ), 
    label = "Monto",
    required=True
  )
  class Meta:
    model = Transferencia
    fields = ('fecha', 'monto', 'cuenta_retiro','cuenta_deposito')
    widgets = {
      'obra': Select(attrs={'class': 'form-control',}),
    }

class CuentaAddForm(forms.ModelForm):
  nombre = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
      }
    ), 
    label = "Nombre",
    required=True
  )
  numero_cuenta = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
      }
    ), 
    label = "Numero cuenta",
    required=True
  )
  saldo_inicial = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'type': 'number',
        'step': '0.01',
        'value': '0.00',
        'placeholder':'0.00'
      }
    ), 
    label = "Saldo incial",
    required=True
  )
  fecha = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix date-picker',
      }
    ), 
    label = "Fecha",
    required=True
  )
  class Meta:
    model = Cuenta
    fields = ('nombre','numero_cuenta', 'saldo_inicial', 'fecha','activo')
    widgets = {
      #'parent': Select(attrs={'class': 'form-control',}),
    }

class CuentaEditForm(forms.ModelForm):
  nombre = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
      }
    ), 
    label = "Nombre",
    required=True
  )
  numero_cuenta = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
      }
    ), 
    label = "Numero cuenta",
    required=True
  )
  saldo_inicial = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'type': 'number',
        'step': '0.01',
        'value': '0.00',
        'placeholder':'0.00'
      }
    ), 
    label = "Saldo incial",
    required=True,
    disabled=True
  )
  fecha = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix date-picker',
      }
    ), 
    label = "Fecha",
    required=True,
    disabled=True
  )
  activo = forms.BooleanField(
    widget=forms.CheckboxInput(
      attrs={
        'class': 'form-control form-control-solid icheck',
        'data-radio':'iradio_flat-grey'
      }
    ), 
    label = "Activo",
    required=True
  )
  class Meta:
    model = Cuenta
    fields = ('nombre','numero_cuenta', 'saldo_inicial', 'fecha','activo')
    widgets = {
      #'parent': Select(attrs={'class': 'form-control',}),
    }

