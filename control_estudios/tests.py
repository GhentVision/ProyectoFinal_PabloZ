from django.test import TestCase

from django.db import IntegrityError
from control_estudios.models import Curso


class CursoTests(TestCase):

    def test_creacion_curso(self):
        curso = Curso(nombre="Titulo", comision=1000, duracion='3 meses', descripcion='Hola mundo')
        curso.save()

        self.assertEqual(Curso.objects.count(), 1)
        self.assertEqual(curso.nombre, "Titulo")
        self.assertEqual(curso.comision, 1000)
        self.assertEqual(curso.duracion, '3 meses')
        self.assertEqual(curso.descripcion, 'Hola mundo')

    def test_curso_str(self):
        curso = Curso(nombre="Python", comision=20000, duracion= '1 mes', descripcion='Adios mundo')
        curso.save()

        self.assertEqual(curso.__str__(), "Python | 20000")
