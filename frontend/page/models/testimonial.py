from django.db import models
from ckeditor.fields import RichTextField

class Testimonial(models.Model):
    img = models.ForeignKey('images.Image', on_delete=models.PROTECT, blank=True, null=True)
    studentName = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    testimonialNote = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'Testimonial by {self.studentName}'
