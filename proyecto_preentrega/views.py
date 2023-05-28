from django. shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def inicio(request):
    contexto = {}
    http_response = render(
        request = request,
        template_name = 'control_estudios/index.html',
        context = contexto,
    )
    return http_response


def plataforma_learning(request):
    return render(request, 'control_estudios/plataforma_learning.html')