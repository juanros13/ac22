from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.forms import formsets
from apps.obras.models import Obra
from apps.gestion_financiera.forms import IngresoAddForm, GastoAddForm, GastoDetalleAddForm, TransferenciaAddForm, CuentaAddForm, CuentaEditForm
from apps.gestion_financiera.models import Ingreso, Gasto, Transferencia, Cuenta

@login_required(login_url='/')
def gasto_view(request):
  gastos = Gasto.objects.all()
  context = {
    'gastos' : gastos,
  }
  return render(request, 'gestion_financiera/egresos/gastos_consultar.html',context)


@login_required(login_url='/')
def gasto_crear_view(request):
  url = reverse('vista_gasto')
  gasto_form = GastoAddForm()
  GastoDetalleFormset = formsets.formset_factory(GastoDetalleAddForm, extra=0, max_num=20, min_num=1)
  gasto_detalle_form = GastoDetalleFormset()
  if request.method == "POST":
    total_gasto = 0.0
    gasto_form = GastoAddForm(request.POST)
    obra = Obra.objects.get(id=request.session['obra_actual'][1])
    gasto_detalle_form = GastoDetalleFormset(request.POST)
    if gasto_form.is_valid() and gasto_detalle_form.is_valid():
      gasto = gasto_form.save(commit=False)
      for form in gasto_detalle_form:
        total_gasto += float(form.cleaned_data['monto'])
      gasto.monto = total_gasto
      gasto.usuario_creo = request.user
      gasto.save()
      print gasto.id
      for detalle_form in gasto_detalle_form:
        gasto_detalle = detalle_form.save(commit=False)
        gasto_detalle.gasto = gasto
        gasto_detalle.save()
      messages.success(request, 'Gasto agregada correctamente')
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
  return render(request, 'gestion_financiera/ingreso/ingreso_crear.html', context)


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


@login_required(login_url='/')
def transferencia_view(request):
  transferencias = Transferencia.objects.all()
  context = {
    'transferencias' : transferencias,
  }
  return render(request, 'gestion_financiera/transferencia/transferencia_consultar.html',context)


@login_required(login_url='/')
def transferencia_crear_view(request):
  url = reverse('vista_ingreso')
  transferencia_form = TransferenciaAddForm()
  if request.method == "POST":
    ingreso_form = TransferenciaAddForm(request.POST)
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
    'transferencia_form':transferencia_form,
  }
  return render(request, 'gestion_financiera/transferencia/transferencia_crear.html', context)


@login_required(login_url='/')
def transferencia_editar_view(request):
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
def transferencia_eliminar_view(request, id_especificacion):
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



@login_required(login_url='/')
def cuentas_contables_view(request):
  cuentas = Cuenta.objects.all()
  context = {
    'cuentas' : cuentas,
  }
  return render(request, 'gestion_financiera/cuentas_contables/cuenta_consultar.html',context)


@login_required(login_url='/')
def cuentas_contables_crear_view(request):
  url = reverse('vista_cuentas_contables_crear')
  cuenta_form = CuentaAddForm()
  if request.method == "POST":
    cuenta_form = CuentaAddForm(request.POST)
    obra = Obra.objects.get(id=request.session['obra_actual'][1])
    if cuenta_form.is_valid():
      cuenta = cuenta_form.save(commit=False)
      cuenta.save()
      messages.success(request, 'Cuenta agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'cuenta_form':cuenta_form,
  }
  return render(request, 'gestion_financiera/cuentas_contables/cuenta_crear.html', context)


@login_required(login_url='/')
def cuentas_contables_editar_view(request, id_cuenta):
  url = reverse('vista_cuentas_contables_crear')
  cuenta = get_object_or_404(Cuenta, pk=id_cuenta)
  cuenta_form = CuentaEditForm(instance=cuenta)
  if request.method == "POST":
    cuenta_form = CuentaEditForm(request.POST)
    obra = Obra.objects.get(id=request.session['obra_actual'][1])
    if cuenta_form.is_valid():
      cuenta = cuenta_form.save(commit=False)
      cuenta.save()
      messages.success(request, 'Cuenta agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'cuenta_form':cuenta_form,
  }
  return render(request, 'gestion_financiera/cuentas_contables/cuenta_crear.html', context)
