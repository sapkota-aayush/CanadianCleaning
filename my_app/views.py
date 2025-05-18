from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'my_app/Home.html')

def about(request):
    return render(request, 'my_app/About.html')

def service(request):
    return render(request, 'my_app/Services.html')