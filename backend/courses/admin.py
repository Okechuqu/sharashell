from django.contrib import admin

from backend.courses.models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseArticle)
admin.site.register(CourseCategory)
