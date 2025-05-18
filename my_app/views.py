from django.shortcuts import render
from .forms import ServiceForm, ContactForm
from .models import Service, Booking, ContactMessage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect

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

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            
            try:
                send_mail(
                    subject=f"New message from {contact.name} ({contact.email})",
                    message=contact.message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                contact.save()
                messages.success(request,"Your message has been sent successfully.")
                return redirect('home')
            except Exception as e:
                messages.error(request,f"Error sending email: {e}")
        else:
                messages.error(request,"Please correct the errors below.")
    else:
                form=ContactForm()
                
    return render(request, 'my_app/contact.html', {'form': form})



def testimonial(request):
    return render(request, 'my_app/testimonial.html')