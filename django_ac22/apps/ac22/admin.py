from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from apps.obras.models import Obra, Estado
from apps.usuarios.models import UserProfile, UserMensaje
from apps.recursos.models import Recurso, RecursoTipo, RecursoUnidad
from apps.gestion_financiera.models import Ingreso, Cuenta, MetodoPago

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Usuario Profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserMensaje)
admin.site.register(Obra)
admin.site.register(Estado)
admin.site.register(Recurso)
admin.site.register(RecursoTipo)
admin.site.register(RecursoUnidad)
admin.site.register(Ingreso)
admin.site.register(Cuenta)
admin.site.register(MetodoPago)
