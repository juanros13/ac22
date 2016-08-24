from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.especificaciones import views as esp_view

urlpatterns = [
	url(r'^$', esp_view.especificaciones_view, name="vista_especificaciones"),
]
 