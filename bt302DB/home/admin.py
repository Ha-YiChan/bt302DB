from django.contrib import admin
from . models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('stdID','stdName','stdCourse','stdYear')

admin.site.register(Student, StudentAdmin)