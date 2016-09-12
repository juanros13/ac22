from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.especificaciones import views as esp_view

urlpatterns = [
	url(r'^$', esp_view.especificaciones_view, name="vista_especificaciones"),
	url(r'^crear/$', esp_view.especificaciones_crear_view, name="vista_especificaciones_crear"),
  url(r'^editar/(?P<id_especificacion>\d+)/$', esp_view.especificaciones_editar_view, name="vista_especificaciones_editar"),
  url(r'^eliminar/(?P<id_especificacion>\d+)/$', esp_view.especificaciones_eliminar_view, name="vista_especificaciones_eliminar"),
]
 