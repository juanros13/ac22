# -*- encoding: utf-8 -*-
import datetime 
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

class Categoria(MPTTModel):
  nombre = models.CharField(max_length=50)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
  usuario_creo = models.ForeignKey(
    User
  )
  activo = models.BooleanField(default=1)
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  class MPTTMeta:
    order_insertion_by = ['nombre']
  def __str__(self):              
    return self.nombre.encode('utf8')
  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Categoria, self).save(*args, **kwargs)


class Catalogo(models.Model):
  categoria = models.ForeignKey(
    Categoria
  )
  ciudad = models.CharField(
    max_length=450
  )
  nombre = models.CharField(
    max_length=450
  )
  usuario_creo = models.ForeignKey(
    User
  )
  activo = models.BooleanField(default=1)
  descripcion = models.TextField()
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def __str__(self):
    return self.nombre.encode('utf8')
  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Catalogo, self).save(*args, **kwargs)

class Almacen(models.Model):
  nombre = models.CharField(
    max_length=450
  )
  telefono = models.CharField(
    max_length=450
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
    super(Almacen, self).save(*args, **kwargs)

class Movimiento(models.Model):
  TIPO_MOVIMIENTO = (
    ('entrada', 'Entrada'),
    ('baja', 'Baja'),
    ('traslado', 'Traslado'),
  )
  catalogo = models.ForeignKey(
    Catalogo
  )
  tipo = models.CharField(
    choices=TIPO_MOVIMIENTO, 
    default='entrada',
    max_length=20
  )
  #proveedor = models.ForeignKey(
  #  Proveedor,
  #  blank=True
  #)
  almacen = models.ForeignKey(
    Almacen,
  )
  unidades = models.PositiveIntegerField()
  costo_por_unidad = models.DecimalField(max_digits=9, decimal_places=2)
  marca = models.CharField(
    max_length=150
  )
  modelo = models.CharField(
    max_length=150
  )
  fecha =  models.DateTimeField()
  
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)

  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if self.tipo == 'entrada':
      pass

    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Movimiento, self).save(*args, **kwargs)

class Inventario(models.Model):
  catalogo = models.ForeignKey(
    Catalogo
  )
  movimiento_alta = models.ForeignKey(
    Movimiento,
    related_name="movimiento_alta",
  )
  movimiento_baja = models.ForeignKey(
    Movimiento,
    related_name="movimiento_baja",
    null=True, 
    blank=True
  )
  catalogo = models.ForeignKey(
    Catalogo
  )
  #proveedor = models.ForeignKey(
  #  Proveedor,
  #  blank=True
  #)
  almacen = models.ForeignKey(
    Almacen,
  )
  marca = models.CharField(
    max_length=150
  )
  modelo = models.CharField(
    max_length=150
  )
  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Inventario, self).save(*args, **kwargs)
