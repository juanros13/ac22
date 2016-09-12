from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.catalogo_de_conceptos import views as c_de_conceptos_views

urlpatterns = [
	url(r'^$', c_de_conceptos_views.catalogo_de_conceptos_view, name="vista_catalogo_de_conceptos"),
  url(r'^concepto/crear/$', c_de_conceptos_views.concepto_crear_view, name="vista_concepto_crear"),
  url(r'^concepto/editar/(?P<id_concepto>\d+)/$', c_de_conceptos_views.concepto_editar_view, name="vista_concepto_editar"),
  url(r'^agrupador/crear/$', c_de_conceptos_views.agrupador_crear_view, name="vista_agrupador_crear"),
  url(r'^agrupador/editar/(?P<id_agrupador>\d+)/$', c_de_conceptos_views.agrupador_editar_view, name="vista_agrupador_editar"),
  url(r'^agrupador/eliminar/$', c_de_conceptos_views.agrupador_eliminar_view, name="vista_agrupador_eliminar"),
]

 