from django.contrib import admin

# Register your models here.
from .models import student

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['name','roll','email','password']
