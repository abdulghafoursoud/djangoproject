
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Admin)