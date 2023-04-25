from django.shortcuts import render
import os
from django.conf import settings

def homes(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'index.html')
    print(template_path)  # Imprime la ruta completa de la plantilla en la consola
    return render(request, 'a.html')
