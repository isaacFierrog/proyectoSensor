from django.shortcuts import render


def modulos(request):
    return render(request, 'modulo/modulo.html')