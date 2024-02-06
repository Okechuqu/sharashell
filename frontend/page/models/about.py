from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):

    img = models.ForeignKey('images.Image', on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    shortNote = RichTextField(blank=True, null=True, help_text="First Paragraph")
    fullNote = models.TextField(blank=True, null=True, help_text="Rest of the Description")

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("Abouts")

    def __str__(self):
        return self.name


class Instructor(models.Model):
    img = models.ForeignKey('images.Image', on_delete=models.PROTECT, blank=True, null=True, help_text="please add a portrait photo")
    staff = models.ForeignKey('authuser.Staff', on_delete=models.CASCADE, blank=True, null=True)
    designation = models.CharField(max_length=100,blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    tiktok_link = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.staff.firstName
