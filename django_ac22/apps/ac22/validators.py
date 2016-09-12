import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
  ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
  valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
  if not ext.lower() in valid_extensions:
    raise ValidationError(u'Archivo no valido.')


def validate_file_extension_pdf(value):
  ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
  valid_extensions = ['.pdf']
  if not ext.lower() in valid_extensions:
    raise ValidationError(u'Archivo no valido.')

def validate_file_extension_pdf_and_zip(value):
  ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
  valid_extensions = ['.pdf', '.zip', '.rar']
  if not ext.lower() in valid_extensions:
    raise ValidationError(u'Archivo no valido.')