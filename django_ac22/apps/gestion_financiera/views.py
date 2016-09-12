from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from django.forms import fields, models, formsets, widgets
from apps.obras.models import Obra
from apps.gestion_financiera.forms import IngresoAddForm, GastoAddForm, get_ordereditem_formset, GastoDetalleAddForm
from apps.gestion_financiera.models import Ingreso, Gasto

@login_required(login_url='/')
def gasto_view(request):
  gasto = Gasto.objects.all()
  context = {
    'gasto' : gasto,
  }
  return render(request, 'gestion_financiera/egresos/gastos_consultar.html',context)

@login_required(login_url='/')
def gasto_crear_view(request):
  url = reverse('vista_ingreso')
  gasto_form = GastoAddForm()
  gasto_detalle_form = formsets.formset_factory(GastoDetalleAddForm, extra=5)
  if request.method == "POST":
    ingreso_form = IngresoAddForm(request.POST)
    obra = Obra.objects.get(id=request.session['obra_actual'][1])
    if ingreso_form.is_valid():
      ingreso = ingreso_form.save(commit=False)
      ingreso.obra = obra
      ingreso.usuario_creo = request.user
      ingreso.save()
      ingreso_form.save()
      messages.success(request, 'Ingreso agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'gasto_form':gasto_form,
    'gasto_detalle_form':gasto_detalle_form
  }
  return render(request, 'gestion_financiera/egresos/gastos_crear.html',context)

@login_required(login_url='/')
def gasto_editar_view(request):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  obras = Obra.objects.all()
  context = {
    'message': message,
    'obras' : obras,
  }
  return render(request, 'catalogo_de_conceptos/concepto_crear.html',context)


@login_required(login_url='/')
def ingreso_view(request):
  ingresos = Ingreso.objects.all()
  context = {
    'ingresos' : ingresos,
  }
  return render(request, 'gestion_financiera/ingreso/ingreso_consultar.html',context)

@login_required(login_url='/')
def ingreso_crear_view(request):
  url = reverse('vista_ingreso')
  ingreso_form = IngresoAddForm()
  if request.method == "POST":
    ingreso_form = IngresoAddForm(request.POST)
    obra = Obra.objects.get(id=request.session['obra_actual'][1])
    if ingreso_form.is_valid():
      ingreso = ingreso_form.save(commit=False)
      ingreso.obra = obra
      ingreso.usuario_creo = request.user
      ingreso.save()
      ingreso_form.save()
      messages.success(request, 'Ingreso agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'ingreso_form':ingreso_form,
  }
  return render(request, 'gestion_financiera/ingreso/ingreso_crear.html',context)

@login_required(login_url='/')
def ingreso_editar_view(request):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  obras = Obra.objects.all()
  context = {
    'message': message,
    'obras' : obras,
  }
  return render(request, 'catalogo_de_conceptos/concepto_crear.html',context)


@login_required(login_url='/')
def ingreso_eliminar_view(request, id_especificacion):
  especificacion = get_object_or_404(Especificaciones, pk=id_especificacion)
  url = reverse('vista_especificaciones')
  if request.user.has_perm('apps.especificaciones.delete_especificaciones'):
    test = especificacion.delete()
    print test
    if True:
      messages.success(request, 'Especificacion eliminada correctamente.')
    else:
      messages.error(request, 'Problemas para eliminar la especificacion.')
  else:
    messages.error(request, 'No cuentas con permisos para eliminar especificaciones.')
  
  return HttpResponseRedirect(url)
