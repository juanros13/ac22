from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.proyecto_ejecutivo import views as proy_ejecutivo

urlpatterns = [
	url(r'^$', proy_ejecutivo.proyecto_ejecutivo_view, name="vista_proyecto_ejecutivo"),
]
 