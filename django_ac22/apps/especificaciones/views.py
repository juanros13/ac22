from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from apps.obras.models import Obra
from apps.especificaciones.models import Especificaciones
from apps.especificaciones.forms import EspecificacionesAddForm

@login_required(login_url='/')
def especificaciones_view(request):
  especificaciones = Especificaciones.objects.all()
  context = {
    'especificaciones' : especificaciones,
  }
  return render(request, 'especificaciones/especificaciones.html',context)

@login_required(login_url='/')
def especificaciones_crear_view(request):
  especificaciones_form = EspecificacionesAddForm()
  url = reverse('vista_especificaciones')
  if request.method == "POST":
    especificaciones_form = EspecificacionesAddForm(request.POST, request.FILES)
    if especificaciones_form.is_valid():
      especificaciones_form.save()
      messages.success(request, 'Especificacion agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'especificaciones_form' : especificaciones_form
  }
  return render(request, 'especificaciones/especificaciones_crear.html',context)

@login_required(login_url='/')
def especificaciones_editar_view(request, id_especificacion):
  especificacion = get_object_or_404(Especificaciones, pk=id_especificacion)
  especificaciones_form = EspecificacionesAddForm(instance=especificacion)
  url = reverse('vista_especificaciones')
  if request.method == "POST":
    especificaciones_form = EspecificacionesAddForm(request.POST, request.FILES,instance=especificacion)
    if especificaciones_form.is_valid():
      especificaciones_form.save()
      messages.success(request, 'Especificacion agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'especificacion' : especificacion,
    'especificaciones_form' : especificaciones_form
  }
  return render(request, 'especificaciones/especificaciones_editar.html',context)

@login_required(login_url='/')
def especificaciones_eliminar_view(request, id_especificacion):
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
