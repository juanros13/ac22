from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from apps.obras import views as obras_view

urlpatterns = [
	url(r'^obra/$', obras_view.edificio_view, name="vista_obra"),
	url(r'^obra/crear/$', obras_view.edificio_crear_view, name="vista_obra_crear"),
	url(r'^obra/(?P<id_edificio>\d+)/$', obras_view.edificio_editar_view, name="vista_editar_obra"),
]
 