from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from apps.obras.models import Obra
from apps.recursos.models import Recurso, RecursoTipo
from apps.recursos.forms import RecursoAddForm

@login_required(login_url='/')
def recursos_todos_view(request):
  recursos = Recurso.objects.filter(obra=request.session['obra_actual'][1])
  total_recursos = 0
  for recurso in recursos:
    total_recursos += recurso.cantidad * recurso.precio_unitario
  total_recursos = '{0:,.2f}'.format(total_recursos)
  context = {
    'recursos' : recursos,
    'total_recursos' : total_recursos
  }
  return render(request, 'recursos/recursos_todos.html',context)


@login_required(login_url='/')
def recursos_crear_view(request):
  recurso_form = RecursoAddForm()
  url = reverse('vista_recursos_todos')
  if request.method == "POST":
    recurso_form = RecursoAddForm(request.POST)
    obra = Obra.objects.get(id=request.session['obra_actual'][1])
    if recurso_form.is_valid():
      recurso = recurso_form.save(commit=False)
      recurso.obra = obra
      recurso.usuario_creo = request.user
      recurso.save()
      messages.success(request, 'Recurso agregada correctamente')
      return HttpResponseRedirect(url)
    else:
      messages.error(request, 'Errores en la forma')
  context = {
    'recurso_form' : recurso_form
  }
  return render(request, 'recursos/recursos_crear.html',context)

@login_required(login_url='/')
def recursos_materiales_view(request):
  tipo_recurso = get_object_or_404(RecursoTipo,nombre='Material')
  recursos = Recurso.objects.filter(
    obra=request.session['obra_actual'][1],
    tipo=tipo_recurso
  )
  total_recursos = 0
  for recurso in recursos:
    total_recursos += recurso.cantidad * recurso.precio_unitario
  total_recursos = '{0:,.2f}'.format(total_recursos)
  context = {
    'recursos' : recursos,
    'total_recursos' : total_recursos
  }
  return render(request, 'recursos/recursos_todos.html',context)

@login_required(login_url='/')
def recursos_eq_seguridad_view(request):
  tipo_recurso = get_object_or_404(RecursoTipo,nombre='Equipo de seguridad')
  recursos = Recurso.objects.filter(
    obra=request.session['obra_actual'][1],
    tipo=tipo_recurso
  )
  total_recursos = 0
  for recurso in recursos:
    total_recursos += recurso.cantidad * recurso.precio_unitario
  total_recursos = '{0:,.2f}'.format(total_recursos)
  context = {
    'recursos' : recursos,
    'total_recursos' : total_recursos
  }
  return render(request, 'recursos/recursos_todos.html',context)

@login_required(login_url='/')
def recursos_herramienta_menor_view(request):
  tipo_recurso = get_object_or_404(RecursoTipo,nombre='Herramienta menor')
  recursos = Recurso.objects.filter(
    obra=request.session['obra_actual'][1],
    tipo=tipo_recurso
  )
  total_recursos = 0
  for recurso in recursos:
    total_recursos += recurso.cantidad * recurso.precio_unitario
  total_recursos = '{0:,.2f}'.format(total_recursos)
  context = {
    'recursos' : recursos,
    'total_recursos' : total_recursos
  }
  return render(request, 'recursos/recursos_todos.html',context)

@login_required(login_url='/')
def equipo_y_maquinaria_view(request):
  tipo_recurso = get_object_or_404(RecursoTipo,nombre='Equipo y maquinaria')
  recursos = Recurso.objects.filter(
    obra=request.session['obra_actual'][1],
    tipo=tipo_recurso
  )
  total_recursos = 0
  for recurso in recursos:
    total_recursos += recurso.cantidad * recurso.precio_unitario
  total_recursos = '{0:,.2f}'.format(total_recursos)
  context = {
    'recursos' : recursos,
    'total_recursos' : total_recursos
  }
  return render(request, 'recursos/recursos_todos.html',context)

