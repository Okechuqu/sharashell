from django.db import models
from ckeditor.fields import RichTextField


class Slider(models.Model):

    name = models.CharField(max_length=150,blank=True, null=True)
    img = models.ForeignKey('images.Image', on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    subNote = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    index = models.IntegerField(default=0)

    

    class Meta:
        verbose_name = ("Slider")
        verbose_name_plural = ("Sliders")

    def __str__(self):
        return self.name


class Service(models.Model):

    title = models.CharField(max_length=150, blank=True, null=True)
    subNote = RichTextField(max_length=150, blank=True, null=True)
    boxIcon = models.CharField(max_length=150, blank=True, null=True, help_text="Enter your Boxicons here")

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.title
