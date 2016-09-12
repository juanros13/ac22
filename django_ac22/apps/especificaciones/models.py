import datetime
import os
from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
from django.utils.deconstruct import deconstructible
from sorl.thumbnail import ImageField
from mptt.models import MPTTModel, TreeForeignKey
from apps.ac22.validators import validate_file_extension_pdf,validate_file_extension_pdf_and_zip
from apps.obras.models import Obra


@deconstructible
class PathAndRename(object):
  def __init__(self, sub_path):
    self.path = sub_path
  def __call__(self, instance, filename):
    ext = filename.split('.')[-1]
    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(self.path, filename)


path_and_rename = PathAndRename("especificaciones")


TIPO_PROPUESTAS = (
  ('propuesta_economica','Propuesta economica'),
  ('propuesta_tecnica',u'Propuesta tecnica'),
)

class Especificaciones(MPTTModel):
  nombre_documento = models.CharField(
    max_length=450,
    blank=True,
    null=True,
  )
  contenido = models.CharField(
    max_length=450,
  )
  nombre_anexo = models.CharField(
    max_length=450,
    blank=True,
    null=True,
  )
  tipo_propuesta = models.CharField(
    max_length=450,
    choices = TIPO_PROPUESTAS, default='propuesta_economica'
  )
  anexo = models.FileField(
    upload_to=path_and_rename, 
    blank=True,
    null=True,
    validators=[validate_file_extension_pdf_and_zip]
  )
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

  fecha_creacion =  models.DateTimeField(editable=False)
  fecha_modificacion =  models.DateTimeField(editable=False)
  def __unicode__(self):
    return self.nombre_documento+" "+self.contenido
  def save(self, *args, **kwargs):
    if not self.id:
      self.fecha_creacion = datetime.datetime.today()
    self.fecha_modificacion = datetime.datetime.today()
    super(Especificaciones, self).save(*args, **kwargs)
  class MPTTMeta:
    order_insertion_by = ['nombre_documento']

