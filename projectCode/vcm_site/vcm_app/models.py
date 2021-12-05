from django.db import models

# Create your models here.

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    vendor_email = models.EmailField(max_length=100) #THIS IS A PLACEHOLDER

    #return this vendor's contracts
    def get_contracts(self):
        return self.contract_set.all()

    #this be a toString
    def __str__(self):
        return self.vendor_name



class Contract(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT) #Does not allow vendor to be deleted
    contract_title = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    """ will need to use FileField
    see https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types
        https://www.geeksforgeeks.org/filefield-django-models/

    """


    #toString
    def __str__(self):
        return self.contract_title