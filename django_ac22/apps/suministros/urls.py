from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.suministros import views as suministros_views

urlpatterns = [
	url(r'^$', suministros_views.suministros_view, name="vista_suministros"),
]
 