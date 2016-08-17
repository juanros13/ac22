# -*- encoding: utf-8 -*-
from datetime import datetime, date, time
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from django.forms import formset_factory
from django.contrib.auth.models import User
from apps.inventario.forms import CatalogoForm, CategoriaForm, AlmacenAddForm, ProveedorAddForm, MovimientoForm, IventarioAltaForm
from apps.inventario.models import Catalogo, Categoria, Almacen, Proveedor, Movimiento, Inventario

@login_required(login_url='/')
def inventario_resumen_view(request):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  catalogos = Catalogo.objects.all()
  context = {
    'catalogos': catalogos,
    'message': message
  }
  return render(request, 'inventario/inventario_resumen.html',context)

@login_required(login_url='/')
def inventario_view(request):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  inventarios = Inventario.objects.all()
  context = {
    'inventarios': inventarios,
    'message': message
  }
  return render(request, 'inventario/inventario.html',context)

@login_required(login_url='/')
def almacen_view(request):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  almacenes = Almacen.objects.all()
  context = {
    'almacenes': almacenes,
    'message': message
  }
  return render(request, 'inventario/almacen.html',context)

@login_required(login_url='/')
def almacen_crear_view(request):
  url = reverse('vista_almacen')
  almacen_form = AlmacenAddForm()
  if request.method == "POST":
    almacen_form = AlmacenAddForm(request.POST)
    if almacen_form.is_valid():
      almacen = almacen_form.save(commit=False)
      almacen.usuario_creo = request.user
      almacen.save()
      request.session['_info_message']  = 'Almacen agregado correctamente'  
      return HttpResponseRedirect(url)

  context = {
    'almacen_form': almacen_form,
  }
  return render(request, 'inventario/crear_almacen.html',context)

@login_required(login_url='/')
def proveedor_view(request):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  proveedores = Proveedor.objects.all()
  context = {
    'proveedores': proveedores,
    'message': message
  }
  return render(request, 'inventario/proveedor.html',context)

@login_required(login_url='/')
def proveedor_crear_view(request):
  url = reverse('vista_proveedor')
  proveedor_form = ProveedorAddForm()
  if request.method == "POST":
    proveedor_form = ProveedorAddForm(request.POST)
    if proveedor_form.is_valid():
      proveedor = proveedor_form.save(commit=False)
      proveedor.usuario_creo = request.user
      proveedor.save()
      request.session['_info_message']  = 'Catalogo agregado correctamente'  
      return HttpResponseRedirect(url)

  context = {
    'proveedor_form': proveedor_form,
  }
  return render(request, 'inventario/crear_proveedor.html',context)

@login_required(login_url='/')
def catalogo_crear_view(request):
  url = reverse('vista_inventario')
  catalogo_form = CatalogoForm()
  if request.method == "POST":
    catalogo_form = CatalogoForm(request.POST)
    if catalogo_form.is_valid():
      catalogo = catalogo_form.save(commit=False)
      catalogo.usuario_creo = request.user
      catalogo.save()
      request.session['_info_message']  = 'Catalogo agregado correctamente'  
      return HttpResponseRedirect(url)

  context = {
    'catalogo_form': catalogo_form,
  }
  return render(request, 'inventario/crear_catalogo.html',context)

@login_required(login_url='/')
def categoria_crear_view(request):
  url = reverse('vista_inventario')
  categoria_form = CategoriaForm()
  if request.method == "POST":
    categoria_form = CategoriaForm(request.POST)
    if categoria_form.is_valid():
      categoria = categoria_form.save(commit=False)
      categoria.usuario_creo = request.user
      categoria.save()
      request.session['_info_message']  = 'Categoria agregada correctamente'  
      return HttpResponseRedirect(url)

  context = {
    'categoria_form': categoria_form,
  }
  return render(request, 'inventario/crear_categoria.html',context)


@login_required(login_url='/')
def movimiento_view(request):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  movimientos = Movimiento.objects.all()
  context = {
    'movimientos': movimientos,
    'message': message
  }
  return render(request, 'inventario/movimiento.html',context)

@login_required(login_url='/')
def movimiento_crear_view(request):
  url = reverse('vista_inventario')
  movimiento_form = MovimientoForm()
  if request.method == "POST":
    movimiento_form = MovimientoForm(request.POST)
    if movimiento_form.is_valid():
      movimiento = movimiento_form.save(commit=False)
      movimiento.usuario_creo = request.user
      movimiento.save()
      if movimiento.tipo == 'entrada':
        for counter in range(0, movimiento.unidades):
          inventario = Inventario(
            catalogo=movimiento.catalogo, 
            movimiento_alta=movimiento, 
            proveedor=movimiento.proveedor, 
            almacen=movimiento.almacen, 
            marca=movimiento.marca, 
            modelo=movimiento.modelo, 
          )
          inventario.save()
      
      request.session['_info_message']  = 'Categoria agregada correctamente'  
      return HttpResponseRedirect(url)

  context = {
    'movimiento_form': movimiento_form,
  }
  return render(request, 'inventario/crear_movimiento.html',context)
