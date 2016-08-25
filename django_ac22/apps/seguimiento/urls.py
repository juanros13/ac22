from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.seguimiento import views as seguimiento_views

urlpatterns = [
	url(r'^$', seguimiento_views.seguimiento_view, name="vista_seguimiento"),
]
 