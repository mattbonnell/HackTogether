from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Language)
admin.site.register(Tool)
admin.site.register(Tag)
admin.site.register(Domain)
admin.site.register(Speciality)
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Complexity)