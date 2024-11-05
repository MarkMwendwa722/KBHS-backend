from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Admissions)
class AdmissionsAdmin(admin.ModelAdmin):
    list_display=('name','admission_number','form','date_of_admission')
    list_filter=('form')
    search_fields=('name','admission_number')
    
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display=('id','name','date','form','file')
    list_filter=('form')
    search_fields=('name','admission_number')
    
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=('name','email','message')
    readonly_fields=('name','email','message')
    
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Assignment)
admin.site.register(Admissions)