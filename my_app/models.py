from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.timezone import now

# Phone number validator
phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',  
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

def validate_future_date(value):
    """ Ensure the booking date is not in the past """
    if value < now():
        raise ValidationError("Booking date cannot be in the past.")

class Service(models.Model):
    name = models.CharField(max_length=100, choices=[
        ('HOUSEKEEPING', 'Housekeeping'),
        ('CARPET AND UPHOLSTERY', 'Carpet and Upholstery'),
        ('FLOOR CARE', 'Floor Care'),
        ('DISINFECTING', 'Disinfecting'),
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    description = models.TextField()
    duration = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])  # Example: 1 to 500 minutes
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Service'

class Booking(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, validators=[phone_validator])
    date = models.DateTimeField(validators=[validate_future_date])
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    special_requests = models.TextField(null=True, blank=True)
    discount_coupon = models.CharField(max_length=20, null=True, blank=True)

    def clean(self):
        """ Additional model-level validation """
        if self.service and self.date:
            # Example: Check if the booking date is not on a holiday (can add logic here)
            pass

    def __str__(self):
        return f'Booking for {self.name} on {self.date.strftime("%Y-%m-%d %H:%M")}'

    class Meta:
        ordering = ['-date']
        verbose_name = 'Booking'

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
