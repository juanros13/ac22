from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.calculos import views as calculos_view

urlpatterns = [
	url(r'^$', calculos_view.calculos_view, name="vista_calculos"),
]
 