from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from backend.enquiries.forms import EnquiryForm
from .models import *


def enquiry(request):
    if request.method == 'POST':
        form_eq = EnquiryForm(request.POST)
        if form_eq.is_valid():
            data = form_eq.save(commit=False) 
            # Get the cleaned data from the form
            name = form_eq.cleaned_data['name']
            email = form_eq.cleaned_data['email']
            subject = form_eq.cleaned_data['subject']
            message = form_eq.cleaned_data['message']

            email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage: {message}"

            email_config = EmailConfiguration.objects.first()
            from_email = email_config.sender_email if email_config else settings.DEFAULT_FROM_EMAIL

            to_email = request.email

            send_mail(subject, message, from_email, [to_email], email_message)

            data.save() 
            messages.success(request, 'Enquiry submitted successfully. You will be contacted soon.')
        else:
            messages.error(request, 'Form is Invalid')
    messages.error(request, 'Nice One')
    return render(request, 'contact.html')
