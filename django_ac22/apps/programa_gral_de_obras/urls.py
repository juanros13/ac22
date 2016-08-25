from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.programa_gral_de_obras import views as programa_gral_views

urlpatterns = [
	url(r'^$', programa_gral_views.programa_gral_view, name="vista_programa_gral"),
]
 