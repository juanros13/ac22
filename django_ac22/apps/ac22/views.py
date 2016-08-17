# -*- encoding: utf-8 -*-
import urllib2
import datetime
from datetime import timedelta
from xml.dom import minidom
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseServerError
from django.core.urlresolvers import reverse
from apps.departamentos.models import Departamento, DepartamentoWeb, DepartamentoWebImage
from apps.noticias.models import Noticia
from apps.plumbago.paginator import Paginator


def inmuebles_view(request):

  items = DepartamentoWeb.objects.all()
  imagenes = DepartamentoWebImage.objects.all()

  paginator = Paginator(items, 12) # Show 25 contacts per page

  try:
    page = request.GET.get('page', 1)
  except PageNotAnInteger:
    page = 1


  try:
    items_list = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    items_list = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    items_list = paginator.page(paginator.num_pages)

  for item in items_list.object_list:
    item.thumbs = [b for b in imagenes if b.departamento_web.id==item.id]

  return render_to_response('secciones/inmuebles.html',{'items_list': items_list},context_instance=RequestContext(request))

def inmuebles_detalle_view(request, item_id):
  item = get_object_or_404(DepartamentoWeb, pk=item_id)
  imagenes = DepartamentoWebImage.objects.filter(departamento_web=item)
  ctx = {'item':item,'imagenes':imagenes}
  return render_to_response('secciones/inmuebles_detalle.html',ctx,context_instance=RequestContext(request))

