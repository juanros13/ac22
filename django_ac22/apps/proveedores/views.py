from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from apps.proveedores.models import Proveedor
from apps.proveedores.forms import ProveedorAddForm

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
  return render(request, 'proveedores/proveedor.html',context)

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
  return render(request, 'proveedores/crear_proveedor.html',context)
