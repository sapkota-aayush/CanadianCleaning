# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import time

@shared_task
def send_email_task(name, email, message):
    # Simulate delay for testing
    time.sleep(15)

    send_mail(
        subject=f"New message from {name} ({email})",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
