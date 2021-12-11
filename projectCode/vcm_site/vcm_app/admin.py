from django.contrib import admin

from .models import *

class VendorAdmin(admin.ModelAdmin):
    fieldset = [
        (None,    {'fields': ['vendor_name']}), 
        ('Email', {'fields': ['vendor_email']}),
    ]
admin.site.register(Vendor, VendorAdmin)




admin.site.register(Contract)
admin.site.register(Payment)
admin.site.register(WorkType)
# Register your models here.





