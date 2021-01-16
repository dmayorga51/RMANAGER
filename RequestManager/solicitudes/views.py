from django.shortcuts import render, redirect, get_object_or_404
from .models import Solicitud
from .forms import SolicitudForm   
from django.contrib import messages 
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
def solicitud(request):
    data ={
        'form':  SolicitudForm() ## crea una instancia para enviar el formulario vacio
    }
    if request.method == 'POST':
        formulario = SolicitudForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Solicitud Ingresada Correctamente.")
            
        else:
            form = SolicitudForm()

    return render(request, 'solicitudes/solicitud.html', data )

@login_required
def listar_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(solicitudes, 10)
        solicitudes = paginator.page(page)
    
    except:
        raise Http404


    data = {
        'entity': solicitudes,
        'paginator': paginator
    }
    

    return render(request, 'solicitudes/listarsolicitudes.html', data)

@login_required
def modificar_solicitudes(request, id):

    solicitud = get_object_or_404(Solicitud, id=id)

    data = {
        'form': SolicitudForm(instance=solicitud)
    }

    if request.method == 'POST':
        formulario =SolicitudForm(data=request.POST, instance=solicitud, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Solicitud modificada correctamente.")
            return redirect(to="listar_solicitudes")
        data["form"] = formulario
            

    return render(request, 'solicitudes/modificarsolicitudes.html', data)

@login_required
def eliminar_solicitudes(request, id):
    solicitud= get_object_or_404(Solicitud, id=id)
    solicitud.delete()
    messages.success(request, "Solicitud eliminada correctamente.")
    return redirect(to="listar_solicitudes")