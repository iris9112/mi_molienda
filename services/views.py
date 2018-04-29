from django.shortcuts import render
from .models import Service

# Create your views here.
def serviceView(request):
    services = Service.objects.all()
    template_name = 'services/services.html'
    return render(request, template_name, {'services':services})
