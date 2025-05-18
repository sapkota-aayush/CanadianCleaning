from django.shortcuts import render
from .forms import ServiceForm
from .models import Service, Booking, ContactMessage

# Create your views here.

def home(request):
    return render(request, 'my_app/Home.html')

def about(request):
    return render(request, 'my_app/About.html')

def service(request):
    return render(request, 'my_app/Services.html')

def book_service(request):
    form = ServiceForm()  # Default for GET requests
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=ServiceForm()
       
    
    return render(request, 'my_app/book-service.html', {'form': form}) 