from django.contrib import admin
from django.urls import path

from control_estudios.views import listar_estudiantes,listar_cursos,listar_profesores,\
    crear_curso,añadir_estudiante,añadir_profesor,buscar_cursos,buscar_estudiante,buscar_profesor,eliminar_curso,\
    eliminar_profesor, eliminar_estudiante,editar_curso, editar_profesor,editar_estudiante, ver_estudiante, ver_profesor, ver_curso

urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("nuevo-estudiante/", añadir_estudiante, name="nuevo_estudiante"),
    path("buscar-estudiante/", buscar_estudiante, name="buscar_estudiante"),
    path("eliminar-estudiante/<int:id>/", eliminar_estudiante, name="eliminar_estudiante"),
    path("editar-estudiante/<int:id>/", editar_estudiante, name="editar_estudiante"),
    path("estudiantes/<int:id>/", ver_estudiante, name="ver_estudiante"),

    path("profesores/", listar_profesores, name="lista_profesores"),
    path("nuevo-profesor/", añadir_profesor, name="nuevo_profesor"),
    path("buscar-profesor/", buscar_profesor, name="buscar_profesor"),
    path("eliminar-profesor/<int:id>/", eliminar_profesor, name="eliminar_profesor"),
    path('editar-profesor/<int:id>/', editar_profesor, name="editar_profesor"),
    path("profesores/<int:id>/", ver_profesor, name="ver_profesor"),
    
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
    path("eliminar-curso/<int:id>/", eliminar_curso, name="eliminar_curso"),
    path('editar-curso/<int:id>/', editar_curso, name="editar_curso"),
    path("cursos/<int:id>/", ver_curso, name="ver_curso"),
    
]


