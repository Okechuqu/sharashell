from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class FrontendStaff(models.Model):
    staff = models.ForeignKey('authuser.Staff', on_delete=models.PROTECT, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    is_active = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Frontend")
        verbose_name_plural = ("FrontendStaff")

    def __str__(self):
        return self.staff.username
