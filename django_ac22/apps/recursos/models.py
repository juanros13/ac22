import datetime 
from django.db import models
from django.contrib.auth.models import User
from apps.obras.models import Obra



class RecursoTipo(models.Model):
  nombre = models.CharField(
    max_length=450,
  )
  def __unicode__(self):
    return self.nombre


class RecursoUnidad(models.Model):
  nombre = models.CharField(
    max_length=450,
  )
  abreviacion = models.CharField(
    max_length=10
  )
  def __unicode__(self):
    return self.nombre

class Recurso(models.Model):
  nombre = models.CharField(
    max_length=450,
  )
  tipo = models.ForeignKey(RecursoTipo)
  unidad = models.ForeignKey(RecursoUnidad)
  cantidad = models.DecimalField(max_digits=12, decimal_places=2)
  precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
  usuario_creo = models.ForeignKey(
    User
  )
  obra = models.ForeignKey(Obra)
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def save(self, *args, **kwargs):
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Recurso, self).save(*args, **kwargs)
  def get_precio_unitario(self):
    return '{0:,.2f}'.format(self.precio_unitario)
  def get_cantidad(self):
    return '{0:,.2f}'.format(self.cantidad)
  def get_total(self):
    return '{0:,.2f}'.format(self.cantidad*self.precio_unitario)
  def __unicode__(self):
    return self.nombre