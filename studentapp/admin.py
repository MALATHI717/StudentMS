from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course')  # Fields to show in admin list view
    search_fields = ('name', 'email', 'course')  # Optional: adds search bar
    list_filter = ('course',)  # Optional: adds filter sidebar by course

admin.site.register(Student, StudentAdmin)
