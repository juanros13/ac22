# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms.widgets import Select, Textarea
from apps.inventario.models import Catalogo, Categoria, Almacen, Movimiento, Inventario
from mptt.forms import TreeNodeChoiceField

class IventarioAltaForm(forms.ModelForm):
  
  class Meta:
    model = Inventario
    fields = ('movimiento_alta','catalogo', 'almacen','marca','modelo')

class MovimientoForm(forms.ModelForm):
  unidades = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el numero de unidades',
      }
    ), 
    label = "Total de unidades",
  )
  costo_por_unidad = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el costo por unidad',
      }
    ), 
    label = "Costo por unidad",
  )
  fecha = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa la fecha del movimiento',
      }
    ), 
    label = "Fecha del movimiento",
  )
  marca = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa la marca',
      }
    ), 
    label = "Marca",
  )
  modelo = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el modelo',
      }
    ), 
    label = "Modelo",
  )
  class Meta:
    model = Movimiento
    fields = ('tipo','catalogo', 'unidades', 'costo_por_unidad', 'marca', 'modelo','fecha','almacen')
    widgets = {
      'tipo': Select(
        attrs={
          'class': 'form-control',
        }
      ),
      'catalogo': Select(
        attrs={
          'class': 'form-control',
        }
      ),
      'almacen': Select(
        attrs={
          'class': 'form-control',
        }
      ),
      'proveedor': Select(
        attrs={
          'class': 'form-control',
        }
      ),
    }


class CatalogoForm(forms.ModelForm):
  categoria = TreeNodeChoiceField(
    queryset=Categoria.objects.all(),
    level_indicator='+--',
  )
  nombre = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el nombre',
      }
    ), 
    label = "Nombre",
    required=False
  )
  class Meta:
    model = Catalogo
    fields = ('nombre','descripcion','categoria')
    widgets = {
      'descripcion': Textarea(
        attrs={
          'class': 'form-control',
          'rows' : '8',
        }
      ),
    }
    
class CategoriaForm(forms.ModelForm):
  parent = TreeNodeChoiceField(
    queryset=Categoria.objects.all(),
    level_indicator='+--',
    required=False,
  ) 
  nombre = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el nombre',
      }
    ), 
    label = "Nombre",
    required=False
  )
  class Meta:
    model = Categoria
    fields = ('nombre','parent')
    
    
class AlmacenAddForm(forms.ModelForm):
  nombre = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el nombre',
      }
    ), 
    label = "Nombre",
  )
  ciudad = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder' : 'Ingresa el nombre de la ciudad',
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
    model = Almacen
    fields = ('nombre','direccion', 'ciudad', 'codigo_postal')
    widgets = {
      'direccion': Textarea(
        attrs={
          'class': 'form-control',
          'rows' : '8',
        }
      ),
    }
    
