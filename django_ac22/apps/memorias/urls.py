from django.conf.urls import  include, url
from django.conf.urls.static import static
from apps.memorias import views as mem_views

urlpatterns = [
	url(r'^$', mem_views.memorias_view, name="vista_memorias"),
]
 