from django.db import models


# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ForeignKey('images.Image', on_delete=models.PROTECT, blank=True, null=True)
    author = models.ForeignKey('authuser.Staff', on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")

    def __str__(self):
        return self.title


