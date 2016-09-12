from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from apps.obras.models import Obra
from apps.especificaciones.models import Especificaciones
from apps.propuesta_tecnica.forms import PropuestaTecnicaAddForm

@login_required(login_url='/')
def propuesta_tecnica_view(request):
  especificaciones = Especificaciones.objects.filter(tipo_propuesta='propuesta_tecnica')
  context = {
    'especificaciones' : especificaciones,
  }
  return render(request, 'propuesta_tecnica/propuesta_tecnica.html',context)


@login_required(login_url='/')
def propuesta_tecnica_crear_view(request):
  propuesta_tecnica_form = PropuestaTecnicaAddForm()
  url = reverse('vista_especificaciones')
  if request.method == "POST":
    propuesta_tecnica_form = PropuestaTecnicaAddForm(request.POST, request.FILES)
    if propuesta_tecnica_form.is_valid():
      propuesta_tecnica_form.save()
      messages.success(request, 'Especificacion agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'propuesta_tecnica_form' : propuesta_tecnica_form
  }
  return render(request, 'propuesta_tecnica/propuesta_tecnica_crear.html',context)

@login_required(login_url='/')
def propuesta_tecnica_editar_view(request, id_especificacion):
  especificacion = get_object_or_404(Especificaciones, pk=id_especificacion)
  propuesta_tecnica_form = PropuestaTecnicaAddForm(instance=especificacion)
  url = reverse('vista_especificaciones')
  if request.method == "POST":
    propuesta_tecnica_form = PropuestaTecnicaAddForm(request.POST, request.FILES,instance=especificacion)
    if propuesta_tecnica_form.is_valid():
      propuesta_tecnica_form.save()
      messages.success(request, 'Especificacion agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'especificacion' : especificacion,
    'propuesta_tecnica_form' : propuesta_tecnica_form
  }
  return render(request, 'propuesta_tecnica/propuesta_tecnica_editar.html',context)

@login_required(login_url='/')
def propuesta_tecnica_eliminar_view(request, id_especificacion):
  especificacion = get_object_or_404(Especificaciones, pk=id_especificacion)
  url = reverse('vista_especificaciones')
  if request.user.has_perm('apps.propuesta_tecnica.delete_especificaciones'):
    test = especificacion.delete()
    print test
    if True:
      messages.success(request, 'Especificacion eliminada correctamente.')
    else:
      messages.error(request, 'Problemas para eliminar la especificacion.')
  else:
    messages.error(request, 'No cuentas con permisos para eliminar especificaciones.')
  
  return HttpResponseRedirect(url)
