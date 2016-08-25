from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.propuesta_tecnica import views as propuesta_tec

urlpatterns = [
	url(r'^$', propuesta_tec.propuesta_tecnica_view, name="vista_propuesta_tecnica"),
]
 