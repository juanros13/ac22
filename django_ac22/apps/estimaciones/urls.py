from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.estimaciones import views as estimaciones_views

urlpatterns = [
	url(r'^$', estimaciones_views.estimaciones_view, name="vista_estimaciones"),
]
 