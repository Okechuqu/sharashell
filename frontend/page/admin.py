from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
# Register your models here.

admin.site.register(Instructor)
admin.site.register(Slider)
admin.site.register(Service)


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SiteInfo.objects.exists():
            return False
        return True


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if About.objects.exists():
            return False
        return True


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Social.objects.exists():
            return False
        return True
