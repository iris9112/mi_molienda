from django.shortcuts import render

# Create your views here.
def home(request):
    template_name = 'core/home.html'
    return render(request, template_name)

def about(request):
    template_name = 'core/about.html'
    return render(request, template_name)

def store(request):
    template_name = 'core/store.html'
    return render(request, template_name)

def contact(request):
    template_name = 'core/contact.html'
    return render(request, template_name)

def sample(request):
    template_name = 'core/sample.html'
    return render(request, template_name)