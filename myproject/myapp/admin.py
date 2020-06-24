from django.contrib import admin
from myapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','rollno','name','address','course']

admin.site.register(Student,StudentAdmin)
