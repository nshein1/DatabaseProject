import unittest
from django.contrib import admin

from projectCode.vcm_site.vcm_app.models import Amenities, Building, Inspection, Lease, Maintenance_Request, Parking, Payment_Ledger, Rent_Payment

from .models import *

class VendorAdmin(admin.ModelAdmin):
    fieldset = [
        (None,    {'fields': ['vendor_name']}), 
        ('Email', {'fields': ['vendor_email']}),
    ]
admin.site.register(Vendor, VendorAdmin)

class BuildingAdmin(admin.ModelAdmin):
    fieldset = [
        (None,    {'fields': ['vendor_name']}), 
        ('Email', {'fields': ['vendor_email']}),
    ]


admin.site.register(Building, BuildingAdmin)
admin.site.register(Unit)
admin.site.register(Person)
admin.site.register(Lease)
admin.site.register(Parking)
admin.site.register(Maintenance_Request)
admin.site.register(Payment_Ledger)
admin.site.register(Inspection)
admin.site.register(Rent_Payment)
admin.site.register(Amenities)

# Register your models here.





