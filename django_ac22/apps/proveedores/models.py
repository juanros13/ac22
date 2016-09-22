# -*- encoding: utf-8 -*-
import datetime 
from django.db import models
from django.contrib.auth.models import User

class Proveedor(models.Model):
  nombre = models.CharField(
    max_length=450
  )
  telefono = models.CharField(
    max_length=450
  )
  rfc = models.CharField(
    max_length=450,
    blank=True
  )
  ciudad = models.CharField(
    max_length=450
  )
  codigo_postal = models.IntegerField()
  direccion = models.TextField()
  usuario_creo = models.ForeignKey(
    User
  )
  activo = models.BooleanField(default=1)
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def __str__(self):
    return self.nombre.encode('utf8')
  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Proveedor, self).save(*args, **kwargs)

