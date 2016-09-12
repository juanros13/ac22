# -*- encoding: utf-8 -*-
from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields, models, formsets, widgets
from django.forms.widgets import Select, Textarea, SelectMultiple, CheckboxSelectMultiple, TextInput
from apps.gestion_financiera.models import Ingreso, Gasto, GastoDetalle


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
    required=False
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
  class Meta:
    model = GastoDetalle
    fields = ('concepto', 'monto')
    widgets = {
    }

def get_ordereditem_formset(form, formset=models.BaseInlineFormSet, **kwargs):
    return models.inlineformset_factory(Gasto, GastoDetalle, form, formset, **kwargs)


CargoDetalleFormset = formsets.formset_factory(GastoDetalleAddForm)
