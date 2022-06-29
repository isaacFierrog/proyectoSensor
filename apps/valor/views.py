from django.shortcuts import render
from .forms import ValorForm


def valores(request):
    if request.method == 'POST':
        print('Este es el metodo post')
        
        
    valor_form = ValorForm()
    
    return render(request, 'index.html', {
        'form': valor_form
    })
