from django import forms

class CursoFormulario(forms.Form):
    elegir_duracion = [
        ('1 mes', '1 mes'),
        ('2 meses', '2 meses'),
        ('3 meses', '3 meses'),   
        ('4 meses', '4 meses'),  
        ]
    nombre = forms.CharField(required=True, max_length=60) 
    comision = forms.IntegerField(required=True, max_value=50000)
    descripcion = forms.CharField(required=False, max_length=800)
    duracion = forms.ChoiceField(required=True, choices=elegir_duracion)
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(required=True,max_length=256)
    apellido = forms.CharField(required=True,max_length=256)
    fecha_nac = forms.DateField()
    dni = forms.CharField(required=True,max_length=32)
    email = forms.EmailField()
    telefono = forms.CharField(required=True,max_length=20)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(required=True,max_length=256)
    apellido = forms.CharField(required=True,max_length=256)
    fecha_nac = forms.DateField()
    dni = forms.CharField(required=True,max_length=32)
    email = forms.EmailField()
    telefono = forms.CharField(required=True,max_length=20)
    profesion = forms.CharField(required=True,max_length=256)
    bio = forms.CharField(required=True,max_length=1000)

