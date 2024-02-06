from django.contrib import admin
from .forms import EmailConfigurationForm
from .models import *


# Register your models here.
@admin.register(EmailConfiguration)
class EmailConfigurationAdmin(admin.ModelAdmin):
    form = EmailConfigurationForm

    def has_add_permission(self, request):
        if EmailConfiguration.objects.exists():
            return False
        return True


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Contact.objects.exists():
            return False
        return True


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','email')

