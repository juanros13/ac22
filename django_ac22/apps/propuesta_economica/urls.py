from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.propuesta_economica import views as propuesta_e_view

urlpatterns = [
	url(r'^$', propuesta_e_view.propuesta_economica_view, name="vista_propuesta_economica"),
]
 