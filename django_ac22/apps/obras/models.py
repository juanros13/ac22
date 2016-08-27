import datetime 
import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


def path_and_rename(path):
  def wrapper(instance, filename):  
    ext = filename.split('.')[-1]
    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(path, filename)

class Estado(models.Model):
  nombre = models.CharField(
    max_length=450,
  )
  abreviatura = models.CharField(
    max_length=5,
  )
  clave = models.CharField(
    max_length=5,
  )
  imagen = ImageField(upload_to=path_and_rename('estados/'), blank=True)
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def __unicode__(self):
    return self.nombre
  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Estado, self).save(*args, **kwargs)

class Obra(models.Model):
  nombre = models.CharField(
    max_length=450,
  )
  direccion = models.TextField()
  imagen = ImageField(upload_to=path_and_rename('edificios/'), blank=True)
  administrador = models.ManyToManyField(
    User,
    blank=True,
    related_name='administradores'
  )
  estado = models.ForeignKey('estado')
  fecha_inicio =  models.DateField()
  fecha_termino =  models.DateField()
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def __unicode__(self):
    return self.nombre
  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Obra, self).save(*args, **kwargs)

