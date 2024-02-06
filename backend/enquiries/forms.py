from django import forms
from backend.enquiries.models import Enquiry
from .models import EmailConfiguration


class EmailConfigurationForm(forms.ModelForm):
    class Meta:
        model = EmailConfiguration
        fields = ['sender_email']


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'required': True}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a message here', 'row': '4', 'required': True}),
        }
