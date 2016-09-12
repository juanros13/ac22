from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.recursos import views as rec_view

urlpatterns = [
  url(r'^crear/$', rec_view.recursos_crear_view, name="vista_recursos_crear"),
  url(r'^recursos_todos/$', rec_view.recursos_todos_view, name="vista_recursos_todos"),
  url(r'^materiales/$', rec_view.recursos_materiales_view, name="vista_recursos_materiales"),
  url(r'^equipo-de-seguridad/$', rec_view.recursos_eq_seguridad_view, name="vista_recursos_eq_seguridad"),
  url(r'^herramienta-menor/$', rec_view.recursos_herramienta_menor_view, name="vista_recursos_herramienta_menor"),
  url(r'^equipo-y-maquinaria/$', rec_view.equipo_y_maquinaria_view, name="vista_equipo_y_maquinaria"),

]
 