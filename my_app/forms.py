from django import forms
from .models import Service, Booking, ContactMessage

class ServiceForm(forms.ModelForm):
    class Meta:
        model= Booking
        fields = ['name', 'address', 'phone', 'date', 'service', 'special_requests', 'discount_coupon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'service': forms.Select(attrs={'class': 'form-control service-select'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control'}),
            'discount_coupon': forms.TextInput(attrs={'class': 'form-control'}),
        }    
