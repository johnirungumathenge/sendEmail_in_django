from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from .settings import EMAIL_HOST_USER
# from .models import Students

def home(request):
    subject ="New order is placed"
    message = "thankyou for shopping with us"
    email ="<email_to_the_recipient>"
    recipient_list = [email]

    send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True)

    return render(request, 'index.html')
    
