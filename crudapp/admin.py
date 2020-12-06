from django.contrib import admin
from crudapp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno','sname','sage','splace']

admin.site.register(Student)
