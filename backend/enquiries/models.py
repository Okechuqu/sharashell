from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Contact(models.Model):

    title = models.CharField(max_length=255,blank=True, null=True)

    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = RichTextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    location = models.URLField(max_length=20000,blank=True, null=True, help_text="Please input the src in the map imbeded HTML")

    

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.title


class Enquiry(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = RichTextField(blank=True, null=True)
    
    class Meta:
        verbose_name = ("Enquiry")
        verbose_name_plural = ("Enquiries")

    def __str__(self):
        return f'Enquiry: {self.name}'


class EmailConfiguration(models.Model):
    sender_email = models.EmailField()

    def __str__(self):
        return self.sender_email
