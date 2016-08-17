# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms.widgets import Select, Textarea
from django.utils.encoding import smart_unicode
from apps.usuarios.models import UserProfile, UserMensaje


#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit, Fieldset, HTML
#from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class UserLoginForm(forms.Form):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'autocomplete' : 'off',
        'placeholder' : 'Usuario',
      }
    ), 
    label = "Usuario",
    required=True
  )
  password = forms.CharField(
    widget=forms.PasswordInput(
      render_value=False,
      attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'autocomplete' : 'off',
        'placeholder' : 'Password',
      }
    ), 
    label = "Contraseña",
    required=True
  )



class UserUpdatePassword(forms.ModelForm):
  password_actual = forms.CharField(
    widget=forms.PasswordInput(
      render_value=False,
      attrs={
        'class': 'form-control',
        'autocomplete' : 'off',
        'placeholder' : 'Password actual',
      }
    ), 
    label = "Contraseña actual",
    required=False
  )
  password1 = forms.CharField(
    widget=forms.PasswordInput(
      render_value=False,
      attrs={
        'class': 'form-control',
        'autocomplete' : 'off',
        'placeholder' : 'Nuevo password',
      }
    ), 
    label = "Nueva contraseña",
    required=False
  )
  password2 = forms.CharField(
    widget=forms.PasswordInput(
      render_value=False,
      attrs={
        'class': 'form-control',
        'autocomplete' : 'off',
        'placeholder' : 'Confirma nuevo password',
      }
    ), 
    label = "Confirma la contraseña",
    required=False
  )
  class Meta:
    model = User
    fields = ("password_actual", "password1", "password2", )
  
class UserUpdateProfile(forms.ModelForm):
  telefono = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'autocomplete' : 'off',
        'placeholder' : 'Telefono',
      }
    ), 
    label = "Telefono",
    required=False
  )
  celular = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'autocomplete' : 'off',
        'placeholder' : 'Celular',
      }
    ), 
    label = "Celular",
    required=False
  )
  rfc = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'autocomplete' : 'off',
        'placeholder' : 'RFC',
      }
    ), 
    label = "RFC",
    required=False
  )
  direccion_fisica = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'autocomplete' : 'off',
        'placeholder' : 'Dirección fisica',
      }
    ), 
    label = "Dirección fisica",
    required=False
  )
  colonia_fisica = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'autocomplete' : 'off',
        'placeholder' : 'Colonia',
      }
    ), 
    label = "Colonia",
    required=False
  )

  class Meta:
    model = UserProfile
    fields = ("telefono", "celular", "rfc", "direccion_fisica", "colonia_fisica")
  
class UserUpdateAvatar(forms.ModelForm):
  avatar = forms.ImageField(required=True, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
  class Meta:
    model = UserProfile
    fields = ("avatar",)
  
class UserMensajeForm(forms.ModelForm):
  class Meta:
    model = UserMensaje
    fields = ("usuario_recibe", "mensaje")
    widgets = {
      'usuario_recibe': Select(attrs={'class': 'form-control selectpicker',}),
      'mensaje': Textarea(
        attrs={
          'class': 'form-control todo-taskbody-taskdesc',
          'rows' : '8',
          'placeholder' :'Mensaje'
        }
      ),
    }
  