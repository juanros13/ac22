from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from apps.obras.models import Obra
from apps.catalogo_de_conceptos.forms import AgrupadorAddForm, ConceptoAddForm
from apps.catalogo_de_conceptos.models import Agrupador, Concepto

@login_required(login_url='/')
def catalogo_de_conceptos_view(request):
  agrupadores = Agrupador.objects.filter(obra=request.session['obra_actual'][1])
  context = {
    'agrupadores' : agrupadores,
  }
  return render(request, 'catalogo_de_conceptos/catalogo_de_conceptos.html',context)

@login_required(login_url='/')
def concepto_editar_view(request):
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
def concepto_crear_view(request):
  url = reverse('vista_catalogo_de_conceptos')
  concepto_form = ConceptoAddForm()
  if request.method == "POST":
    concepto_form = ConceptoAddForm(request.POST)
    obra = Obra.objects.get(id=request.session['obra_actual'][1])
    if concepto_form.is_valid():
      agrupador = concepto_form.save(commit=False)
      agrupador.obra = obra
      agrupador.usuario_creo = request.user
      agrupador.save()
      concepto_form.save()
      messages.success(request, 'Agrupador agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'concepto_form':concepto_form,
  }
  return render(request, 'catalogo_de_conceptos/concepto_crear.html',context)

@login_required(login_url='/')
def agrupador_editar_view(request, id_agrupador):
  url = reverse('vista_catalogo_de_conceptos')
  agrupador = Agrupador.objects.get(id=id_agrupador)
  agrupador_form = AgrupadorAddForm(instance=agrupador)
  if request.method == "POST":
    agrupador_form = AgrupadorAddForm(request.POST, instance=agrupador)
    obra = Obra.objects.get(id=request.session['obra_actual'][1])
    if agrupador_form.is_valid():
      agrupador = agrupador_form.save(commit=False)
      agrupador.obra = obra
      agrupador.usuario_creo = request.user
      agrupador.save()
      agrupador_form.save()
      messages.success(request, 'Agrupador editado correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'agrupador_form': agrupador_form,
    'agrupador': agrupador
  }
  return render(request, 'catalogo_de_conceptos/agrupador_editar.html',context)
@login_required(login_url='/')
def agrupador_crear_view(request):
  url = reverse('vista_catalogo_de_conceptos')
  agrupador_form = AgrupadorAddForm()
  if request.method == "POST":
    agrupador_form = AgrupadorAddForm(request.POST)
    obra = Obra.objects.get(id=request.session['obra_actual'][1])
    if agrupador_form.is_valid():
      agrupador = agrupador_form.save(commit=False)
      agrupador.obra = obra
      agrupador.usuario_creo = request.user
      agrupador.save()
      agrupador_form.save()
      messages.success(request, 'Agrupador agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'agrupador_form': agrupador_form,
  }
  return render(request, 'catalogo_de_conceptos/agrupador_crear.html',context)

@login_required(login_url='/')
def agrupador_eliminar_view(request, id_especificacion):
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
