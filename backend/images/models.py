from django.db import models


# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or "Untitled"
