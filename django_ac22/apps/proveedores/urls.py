from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.proveedores import views as proveedores_views

urlpatterns = [
  url(r'^proveedor/$', proveedores_views.proveedor_view, name="vista_proveedor"),
  url(r'^proveedor/crear/$', proveedores_views.proveedor_crear_view, name="vista_proveedor_crear"),
]
 