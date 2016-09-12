import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import Truncator
from mptt.models import MPTTModel, TreeForeignKey
from apps.obras.models import Obra

class Agrupador(MPTTModel):
  clave = models.CharField(
    max_length=100,
  )
  descripcion = models.TextField(
    max_length=450,
  )
  parent = TreeForeignKey(
    'self', 
    null=True, 
    blank=True, 
    related_name='children', 
    db_index=True,
    verbose_name="Padre"
  )
  obra = models.ForeignKey(Obra)
  usuario_creo = models.ForeignKey(User)
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def __unicode__(self):
    return self.clave+" - "+Truncator(self.descripcion ).words(3)
  def save(self, *args, **kwargs):
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Agrupador, self).save(*args, **kwargs)
  def get_total(self):
    total = 0
    for concepto in self.concepto_set.all():
      total += concepto.cantidad * concepto.precio_unitario
    return '{0:,.2f}'.format(total)
  class MPTTMeta:
    order_insertion_by = ['clave']



class Concepto(models.Model):
  clave = models.CharField(
    max_length=100,
  )
  concepto = models.TextField(
    max_length=450,
  )
  unidad = models.CharField(
    max_length=150,
  )
  cantidad = models.DecimalField(max_digits=12, decimal_places=2)
  precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)

  agrupador =  models.ForeignKey(
    Agrupador
  )
  obra = models.ForeignKey(Obra)
  usuario_creo = models.ForeignKey(User)

  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def get_precio_unitario(self):
    return '{0:,.2f}'.format(self.precio_unitario)
  def get_cantidad(self):
    return '{0:,.2f}'.format(self.cantidad)
  def get_total(self):
    return '{0:,.2f}'.format(self.cantidad*self.precio_unitario)
  def __unicode__(self):
    return self.nombre
  def __unicode__(self):
    return self.nombre_documento+" "+self.contenido
  def save(self, *args, **kwargs):
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Concepto, self).save(*args, **kwargs)

