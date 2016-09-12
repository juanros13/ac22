"""django_plumbago URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from apps.usuarios.views import login_view, dashboard_view
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_view, name="view_login"),
    url(r'^dashboard/$', dashboard_view, name="dashboard"),
    url(r'^usuarios/', include('apps.usuarios.urls')),
    url(r'^directorio/', include('apps.directorio.urls')),
    url(r'^avisos/', include('apps.avisos.urls')),
    url(r'^inventario/', include('apps.inventario.urls')),
    url(r'^obra/', include('apps.obras.urls')),
    url(r'^obra/especificaciones/', include('apps.especificaciones.urls')),
    url(r'^obra/propuesta_economica/', include('apps.propuesta_economica.urls')),
    url(r'^obra/propuesta_tecnica/', include('apps.propuesta_tecnica.urls')),
    url(r'^ingenieria/memorias/', include('apps.memorias.urls')),
    url(r'^ingenieria/proyecto_ejecutivo/', include('apps.proyecto_ejecutivo.urls')),
    url(r'^ingenieria/calculos/', include('apps.calculos.urls')),
    url(r'^ejecucion/programa_gral_de_obras/', include('apps.programa_gral_de_obras.urls')),
    url(r'^ejecucion/suministros/', include('apps.suministros.urls')),
    url(r'^ejecucion/seguimiento/', include('apps.seguimiento.urls')),
    url(r'^ejecucion/estimaciones/', include('apps.estimaciones.urls')),
    url(r'^recursos/', include('apps.recursos.urls')),
    url(r'^catalogo_de_conceptos/', include('apps.catalogo_de_conceptos.urls')),
    url(r'^gestion_financiera/', include('apps.gestion_financiera.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
