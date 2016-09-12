from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.propuesta_tecnica import views as propuesta_tec

urlpatterns = [
	url(r'^$', propuesta_tec.propuesta_tecnica_view, name="vista_propuesta_tecnica"),
  url(r'^crear/$', propuesta_tec.propuesta_tecnica_crear_view, name="vista_propuesta_tecnica_crear"),
  url(r'^editar/(?P<id_especificacion>\d+)/$', propuesta_tec.propuesta_tecnica_editar_view, name="vista_propuesta_tecnica_editar"),
  url(r'^eliminar/(?P<id_especificacion>\d+)/$', propuesta_tec.propuesta_tecnica_eliminar_view, name="vista_propuesta_tecnica_eliminar"),
]
 