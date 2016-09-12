# -*- encoding: utf-8 -*-
from datetime import datetime, date, time
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from django.forms import formset_factory
from django.contrib.auth.models import User
from apps.obras.forms import ObraAddForm
from apps.obras.models import Obra, Estado

@login_required(login_url='/')
def estados_view(request):
  obras = Obra.objects.all()
  estados = Estado.objects.all()
  context = {
    'obras' : obras,
    'estados':estados
  }
  return render(request, 'obras/estados.html',context)


@login_required(login_url='/')
def estado_obras_view(request, abreviatura_estado):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  estado = Estado.objects.filter(abreviatura=abreviatura_estado)
  obras = Obra.objects.filter(estado=estado)
  context = {
    'obras':obras
  }
  return render(request, 'obras/obras_x_estado.html',context)



@login_required(login_url='/')
def edificio_view(request):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  obras = Obra.objects.all()
  context = {
    'obras' : obras,
  }
  return render(request, 'obras/obra.html',context)

@login_required(login_url='/')
def edificio_crear_view(request):
  url = reverse('vista_obra')
  obra_form = ObraAddForm()
  if request.method == "POST":
    obra_form = ObraAddForm(request.POST, request.FILES)
    if obra_form.is_valid():
      obra_form.save()
      messages.success(request, 'Obra agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'obra_form': obra_form,
  }
  return render(request, 'obras/obra_crear.html',context)

@login_required(login_url='/')
def edificio_editar_view(request, id_edificio):
  url = reverse('vista_obra')
  obra = get_object_or_404(Obra, pk=id_edificio)
  obra_form = ObraAddForm(instance=obra)
  if request.method == "POST":
    obra_form = ObraAddForm(request.POST, request.FILES, instance=obra)
    if obra_form.is_valid():
      obra_form.save()
      messages.success(request, 'Obra actualizada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'obra_form': obra_form,
    'obra':obra,
  }
  return render(request, 'obras/obra_editar.html',context)
