from django.db import models
from ckeditor.fields import RichTextField

from backend.authuser.models.user import CustomUser
# Create your models here.


class Student(CustomUser):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    fullName = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, default='Nigeria', verbose_name='Country', blank=True, null=True)
    state = models.CharField(max_length=100, verbose_name='State', blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, verbose_name='Gender', blank=True, null=True)
    coursesPaidFor = models.TextField( blank=True, null=True)
    profilePhoto = models.ForeignKey('images.Image', on_delete=models.PROTECT, verbose_name='Profile Photo', blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    careerPath = models.CharField(max_length=300, verbose_name='Career Path', blank=True, null=True)
    courseDuration = models.CharField(max_length=300, verbose_name='Career Path', blank=True, null=True)
 
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Our Students"

    def __str__(self):
        return f'{self.fullName}'






