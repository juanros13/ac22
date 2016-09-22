from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.gestion_financiera import views as g_financiera_views

urlpatterns = [
  url(r'^ingreso/$', g_financiera_views.ingreso_view, name="vista_ingreso"),
  url(r'^ingreso/crear/$', g_financiera_views.ingreso_crear_view, name="vista_ingreso_crear"),
  url(r'^ingreso/editar/(?P<id_ingreso>\d+)/$', g_financiera_views.ingreso_editar_view, name="vista_ingreso_editar"),
  url(r'^ingreso/eliminar/$', g_financiera_views.ingreso_eliminar_view, name="vista_ingreso_eliminar"),
  url(r'^egresos/gasto/$', g_financiera_views.gasto_view, name="vista_gasto"),
  url(r'^egresos/gasto/crear$', g_financiera_views.gasto_crear_view, name="vista_gasto_crear"),
  url(r'^egresos/gasto/editar$', g_financiera_views.gasto_editar_view, name="vista_gasto_editar"),
  url(r'^egresos/facturas_por_pagar/$', g_financiera_views.gasto_view, name="vista_gasto"),
  url(r'^egresos/facturas_por_pagar/crear$', g_financiera_views.gasto_crear_view, name="vista_gasto_crear"),
  url(r'^egresos/facturas_por_pagar/pagar$', g_financiera_views.gasto_crear_view, name="vista_gasto_crear"),
  url(r'^egresos/facturas_por_pagar/editar$', g_financiera_views.gasto_editar_view, name="vista_gasto_editar"),
  url(r'^transferencia/$', g_financiera_views.transferencia_view, name="vista_transferencia"),
  url(r'^transferencia/crear/$', g_financiera_views.transferencia_crear_view, name="vista_transferencia_crear"),
  url(r'^transferencia/editar/(?P<id_transferencia>\d+)/$', g_financiera_views.transferencia_editar_view, name="vista_transferencia_editar"),
  url(r'^cuentas_contables/$', g_financiera_views.cuentas_contables_view, name="vista_cuentas_contables"),
  url(r'^cuentas_contables/crear/$', g_financiera_views.cuentas_contables_crear_view, name="vista_cuentas_contables_crear"),
  url(r'^cuentas_contables/editar/(?P<id_cuenta>\d+)/$', g_financiera_views.cuentas_contables_editar_view, name="vista_cuentas_contables_editar"),
]