from django.contrib import admin

from .models import College
admin.site.register(College)

from .models import Student
admin.site.register(Student)

from .models import MockTest1
admin.site.register(MockTest1)

from .models import Teacher
admin.site.register(Teacher)

# Register your models here.