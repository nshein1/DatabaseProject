from django.contrib import admin

from .models import *

admin.site.register(Vendor)
admin.site.register(Contract)
admin.site.register(Payment)
admin.site.register(WorkType)
# Register your models here.


admin.site.register(FileUpload)



