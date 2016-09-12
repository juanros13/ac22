from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.gestion_financiera import views as g_financiera_views

urlpatterns = [
  url(r'^ingreso/$', g_financiera_views.ingreso_view, name="vista_ingreso"),
  url(r'^ingreso/crear/$', g_financiera_views.ingreso_crear_view, name="vista_ingreso_crear"),
  url(r'^ingreso/editar/(?P<id_ingreso>\d+)/$', g_financiera_views.ingreso_editar_view, name="vista_ingreso_editar"),
  url(r'^ingresor/eliminar/$', g_financiera_views.ingreso_eliminar_view, name="vista_ingreso_eliminar"),
  url(r'^egresos/gasto/$', g_financiera_views.gasto_view, name="vista_gasto"),
  url(r'^egresos/gasto/crear$', g_financiera_views.gasto_crear_view, name="vista_gasto_crear"),
  url(r'^egresos/gasto/editar$', g_financiera_views.gasto_editar_view, name="vista_gasto_editar"),
]

 