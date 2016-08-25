from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from apps.obras.models import Obra

@login_required(login_url='/')
def seguimiento_view(request):
  message = ''
  if request.session.get('_info_message'):
    message = request.session.get('_info_message')
  request.session['_info_message'] = ''
  obras = Obra.objects.all()
  context = {
    'message': message,
    'obras' : obras,
  }
  return render(request, 'seguimiento/seguimiento.html',context)
