from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.inventario import views as inventario_view

urlpatterns = [
	url(r'^$', inventario_view.inventario_resumen_view, name="vista_inventario_resumen"),
	url(r'^crear/catalogo/$', inventario_view.catalogo_crear_view, name="vista_catalogo_crear"),
	url(r'^crear/categoria/$', inventario_view.categoria_crear_view, name="vista_categoria_crear"),
	url(r'^almacen/$', inventario_view.almacen_view, name="vista_almacen"),
	url(r'^crear/almacen/$', inventario_view.almacen_crear_view, name="vista_almacen_crear"),
	url(r'^proveedor/$', inventario_view.proveedor_view, name="vista_proveedor"),
	url(r'^proveedor/crear/$', inventario_view.proveedor_crear_view, name="vista_proveedor_crear"),
	url(r'^movimientos/$', inventario_view.movimiento_view, name="vista_movimiento"),
	url(r'^movimientos/crear/$', inventario_view.movimiento_crear_view, name="vista_movimiento_crear"),
	url(r'^inventario/$', inventario_view.inventario_view, name="vista_inventario"),
]
 