from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from backend.authuser.models.user import CustomUser

# Create your models here.


class Staff(CustomUser):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    firstName = models.CharField(max_length=200, verbose_name='First Name')
    lastName = models.CharField(max_length=200, verbose_name='Last Name')
    dob = models.DateField( verbose_name='Date of Birth')
    address = RichTextField( verbose_name='Address')
    country = models.CharField(max_length=100, default='Nigeria', verbose_name='Country')
    state = models.CharField(max_length=100, verbose_name='State')
    city = models.CharField(max_length=100, verbose_name='City')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, verbose_name='Gender')
    profilePhoto = models.ForeignKey(
        'images.Image', on_delete=models.PROTECT, verbose_name='Profile Photo', blank=True, null=True)

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Our Staff"

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

    def get_absolute_url(self):
        return reverse("staff_detail", kwargs={"pk": self.pk})
