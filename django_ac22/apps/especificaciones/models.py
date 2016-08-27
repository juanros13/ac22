from __future__ import unicode_literals

from django.db import models

# Create your models here.
def path_and_rename(path):
  def wrapper(instance, filename):  
    ext = filename.split('.')[-1]
    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(path, filename)


class Especificaciones(models.Model):
	nombre = models.CharField().3

class Especificaciones(models.Model):
  nombre = models.CharField(
    max_length=450,
  )
  contenido = models.CharField(
    max_length=450,
  )
  anexo = ImageField(upload_to=path_and_rename('anexos/'), blank=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def __str__(self):
    return self.nombre
  def save(self, *args, **kwargs):
    ''' On save, update timestamps '''
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Especificaciones, self).save(*args, **kwargs)
  class MPTTMeta:
    order_insertion_by = ['nombre']
