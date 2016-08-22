import datetime 
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  # This field is required.
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  telefono = models.CharField(
    max_length=21, 
    null=True, 
    blank=True, 
    default=None
  )
  celular = models.CharField(
    max_length=21, 
    null=True, 
    blank=True, 
    default=None
  )
 
  avatar = models.FileField(
    upload_to='avatars/%Y/%m/%d'
  )
  def get_absolute_url_mensajes(self):
    return "/usuario/mensajes/%s/" % (self.user.username)

class UserMensaje(models.Model):
  usuario_envia = models.ForeignKey(
    User,
    related_name='usuario_crea'
  )
  usuario_recibe = models.ForeignKey(
    User,
    related_name='usuario_entrega'
  )
  mensaje = models.TextField(
    default=None 
  )
  visto = models.BooleanField(
    default=0
  )
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(UserMensaje, self).save(*args, **kwargs)










