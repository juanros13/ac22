import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import Truncator
from mptt.models import MPTTModel, TreeForeignKey
from apps.obras.models import Obra
from apps.inventario.models import Proveedor



class Cuenta(models.Model):
  nombre = models.CharField(
    max_length=255,
    unique=True
  )
  numero_cuenta = models.CharField(
    max_length=255,
    unique=True
  )
  saldo_inicial = models.DecimalField(max_digits=12, decimal_places=2)
  fecha = models.DateField()
  activo = models.BooleanField()
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def __unicode__(self):
    return self.nombre
  def save(self, *args, **kwargs):
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Cuenta, self).save(*args, **kwargs)

class MetodoPago(models.Model):
  nombre = models.CharField(max_length=450)
  def __unicode__(self):
    return self.nombre

class Ingreso(models.Model):
  fecha = models.CharField(
    max_length=100,
  )
  metodo_pago = models.ForeignKey(
    MetodoPago
  )
  concepto = models.CharField(max_length=450)
  referencia = models.CharField(
    max_length=450, 
    null=True, 
    blank=True
  )
  monto = models.DecimalField(max_digits=12, decimal_places=2)
  comentario = models.TextField(
    null=True, 
    blank=True
  )
  usuario_creo = models.ForeignKey(User)
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  cuenta = models.ForeignKey(
    Cuenta
  )
  def __unicode__(self):
    return self.clave+" - "+Truncator(self.descripcion ).words(3)
  def save(self, *args, **kwargs):
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Ingreso, self).save(*args, **kwargs)


class Gasto(models.Model):
  fecha = models.CharField(
    max_length=100,
  )
  metodo_pago = models.ForeignKey(
    MetodoPago
  )
  referencia = models.CharField(
    max_length=450, 
    null=True, 
    blank=True
  )
  monto = models.DecimalField(max_digits=12, decimal_places=2)
  comentario = models.TextField(
    null=True, 
    blank=True
  )
  usuario_creo = models.ForeignKey(User)
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  cuenta = models.ForeignKey(
    Cuenta
  )
  def get_referencia(self):
    if self.referencia:
      return self.referencia
    else:
      return ''
  def __unicode__(self):
    return self.clave+" - "+Truncator(self.descripcion ).words(3)
  def save(self, *args, **kwargs):
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Gasto, self).save(*args, **kwargs)

class GastoDetalle(models.Model):
  gasto = models.ForeignKey(Gasto)
  concepto = models.CharField(max_length=450)
  monto = models.DecimalField(max_digits=12, decimal_places=2)
  obra = models.ForeignKey(
    Obra,
    blank=True,
    null=True
  )
  def __unicode__(self):
    return self.concepto + " - " + self.monto

class Transferencia(models.Model):
  fecha = models.DateField()
  monto = models.ForeignKey(Gasto)
  cuenta_retiro = models.ForeignKey(
    Cuenta,
    related_name='cuenta_retiro'
  )
  cuenta_deposito = models.ForeignKey(
    Cuenta,
    related_name='cuenta_deposito'
  )
  comentario = models.TextField()
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def __unicode__(self):
    return self.concepto + " - " + self.monto
  def save(self, *args, **kwargs):
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Transferecia, self).save(*args, **kwargs)

