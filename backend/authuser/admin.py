from django.contrib import admin
from backend.authuser.models.staff import Staff

from backend.authuser.models.students import Student
from backend.authuser.models.user import CustomUser

# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(CustomUser)
