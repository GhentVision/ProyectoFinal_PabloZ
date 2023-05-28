from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Q

from control_estudios.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
from control_estudios.models import Estudiante, Curso, Profesor

#Vistas Estudiantes

@login_required
def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiante.objects.all(),
        }
    http_response = render(
        request = request,
        template_name = 'control_estudios/lista_estudiantes.html',
        context = contexto,
    )
    return http_response

@login_required
def añadir_estudiante(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            fecha_nac = data["fecha_nac"]
            dni = data["dni"]
            email = data["email"]
            telefono = data["telefono"]
            creador = request.user
            estudiante = Estudiante(nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, dni=dni,email=email,telefono=telefono,creador=creador)
            estudiante.save()
            
            url_exitosa = reverse('lista_estudiantes')
            return redirect(url_exitosa)
    
    else:
        formulario = EstudianteFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_estudiantes.html',
        context={'formulario': formulario}
    )
    return http_response

@login_required
def buscar_estudiante(request):
    if request.method == "POST":
        busqueda = request.POST.get("busqueda")
        if busqueda:
            estudiantes = Estudiante.objects.filter(Q(apellido__iexact=busqueda))
        else:
            estudiantes = Estudiante.objects.none()
    else:
        estudiantes = Estudiante.objects.none()

    contexto = {
        "estudiantes": estudiantes,
    }

    return render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto
    )

@login_required
def ver_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    context = {
        'object': estudiante
    }
    return render(request, 'control_estudios/estudiantes_detail.html', context)

@login_required
def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == "POST":
        estudiante.delete()
        url_exitosa = reverse('lista_estudiantes')
        return redirect(url_exitosa)

@login_required
def editar_estudiante(request, id):
   estudiante = Estudiante.objects.get(id=id)
   if request.method == "POST":
       formulario = ProfesorFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           estudiante.nombre = data['nombre']
           estudiante.apellido = data['apellido']
           estudiante.fecha_nac = data['fecha_nac']
           estudiante.dni = data['dni']
           estudiante.email = data['email']
           estudiante.telefono = data['telefono']
           estudiante.save()
           url_exitosa = reverse('lista_profesores')
           return redirect(url_exitosa)
   else:  
       formulario = EstudianteFormulario(initial={
           'nombre': estudiante.nombre,
           'apellido': estudiante.apellido,
           'fecha_nac': estudiante.fecha_nac,
           'dni': estudiante.dni,
           'email': estudiante.email,
           'telefono': estudiante.telefono,
       })
   context = {
       'formulario': formulario,
       'estudiante_id': id,
   }
   return render(
       request=request,
       template_name='control_estudios/formulario_estudiantes.html',
       context=context,
   )

#Vistas Cursos


def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
        }

    http_response = render(
        request = request,
        template_name = 'control_estudios/lista_cursos.html',
        context = contexto,
    )
    return http_response

@login_required
def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            comision = data["comision"]
            descripcion = data["descripcion"]
            duracion = data["duracion"]
            creador = request.user
            curso = Curso(nombre=nombre, comision=comision, creador=creador, descripcion=descripcion, duracion=duracion) 
            curso.save()
            
            url_exitosa = reverse('lista_cursos')
            return redirect(url_exitosa)
    else:
        formulario = CursoFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario}
    )
    return http_response 

def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data.get("busqueda", "").strip()
        
        if not busqueda:
            messages.error(request, "Por favor, ingresa un valor válido para la búsqueda.")
            return redirect('lista_cursos')
        
        try:
            cursos = Curso.objects.filter(comision=int(busqueda))
            contexto = {
                "cursos": cursos,
            }
    
            return render(
                request=request,
                template_name='control_estudios/lista_cursos.html',
                context=contexto
            )
        except (ValueError, ValidationError):
            return redirect('lista_cursos')

    return redirect('lista_cursos')

@login_required
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)

@login_required
def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.descripcion = data['descripcion']
            curso.duracion = data['duracion']
            curso.save()

            url_exitosa = reverse('lista_cursos')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
            'descripcion': curso.descripcion,
            'duracion': curso.duracion,      
        }
        formulario = CursoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario},
    )

def ver_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    context = {
        'object': curso
    }
    return render(request, 'control_estudios/cursos_detail.html', context)

#Vistas Profesores

def listar_profesores(request):
    contexto = {
        "profesores": Profesor.objects.all(),
        }
    http_response = render(
        request = request,
        template_name = 'control_estudios/lista_profesores.html',
        context = contexto,
    )
    return http_response

@login_required
def añadir_profesor(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            fecha_nac = data["fecha_nac"]
            dni = data["dni"]
            email = data["email"]
            telefono = data["telefono"]
            profesion = data["profesion"]
            bio = data["bio"]
            creador = request.user
            profesor = Profesor(nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, dni=dni,email=email,telefono=telefono,profesion=profesion,bio=bio,creador=creador) 
            profesor.save()
            
            url_exitosa = reverse('lista_profesores')
            return redirect(url_exitosa)
    else:
        formulario = ProfesorFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_profesores.html',
        context={'formulario': formulario}
    )
    return http_response 

def buscar_profesor(request):
    if request.method == "POST":
        busqueda = request.POST.get("busqueda")
        if busqueda:
            profesores = Profesor.objects.filter(Q(apellido__iexact=busqueda))
        else:
            profesores = Profesor.objects.none()
    else:
        profesores = Profesor.objects.none()

    contexto = {
        "profesores": profesores,
    }

    return render(
        request=request,
        template_name='control_estudios/lista_profesores.html',
        context=contexto
    )

@login_required
def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        profesor.delete()
        url_exitosa = reverse('lista_profesores')
        return redirect(url_exitosa)

@login_required
def editar_profesor(request, id):
   profesor = Profesor.objects.get(id=id)
   if request.method == "POST":
       formulario = ProfesorFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           profesor.nombre = data['nombre']
           profesor.apellido = data['apellido']
           profesor.fecha_nac = data['fecha_nac']
           profesor.dni = data['dni']
           profesor.email = data['email']
           profesor.telefono = data['telefono']
           profesor.profesion = data['profesion']
           profesor.bio = data['bio']
           profesor.save()
           url_exitosa = reverse('lista_profesores')
           return redirect(url_exitosa)
   else:  
       formulario = ProfesorFormulario(initial={
           'nombre': profesor.nombre,
           'apellido': profesor.apellido,
           'fecha_nac': profesor.fecha_nac,
           'dni': profesor.dni,
           'email': profesor.email,
           'telefono': profesor.telefono,
           'profesion': profesor.profesion,
           'bio': profesor.bio,

       })
   context = {
       'formulario': formulario,
       'profesor_id': id,
   }
   return render(
       request=request,
       template_name='control_estudios/formulario_profesores.html',
       context=context,
   )

@login_required
def ver_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    context = {
        'object': profesor
    }
    return render(request, 'control_estudios/profesores_detail.html', context)