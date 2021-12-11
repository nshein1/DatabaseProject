from django.db import models

from django.core.validators import MinValueValidator

# Create your models here.

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    vendor_email = models.EmailField(max_length=100)# default="test@test.com") #THIS IS A PLACEHOLDER
    #TypeofWorks = models.ManyToManyField(TypeofWork)

    class Meta:
        ordering =['vendor_name']



    #return this vendor's contracts
    def get_contracts(self):
        return self.contract_set.all()

   

    #this be a toString
    def __str__(self):
        return self.vendor_name



class Contract(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT) #Does not allow vendor to be deleted
    contract_title = models.CharField(max_length=200)
    
    """Contract Status stuff"""
    CURRENT     = 'CR'
    COMPLETED   = 'CP'
    POTENTIAL   = 'PT'
    CANCELED    = 'CN'
    FUTURE      = 'FT'
    CONTRACT_STATUS_CHOICES = [
        (CURRENT, 'Current'),
        (COMPLETED, 'Completed'),
        (POTENTIAL, 'Potential'),
        (CANCELED, 'Canceled'), 
        (FUTURE, 'Future'),
    ]

    contract_status =  models.CharField(
        max_length=2,
        choices=CONTRACT_STATUS_CHOICES,
        default=POTENTIAL,
    )
    class Meta:
            ordering =['contract_title']
    
    #toString
    def __str__(self):
        return self.contract_title



    contract_pdf = models.FileField(upload_to='contract_pdfs/', blank=True) #this will store files in MEDIA_ROOT/contract_pdfs

    

class Payment(models.Model):
    payment_date = models.DateField()
    payment_checkNumber = models.IntegerField(validators=[MinValueValidator(1)])
    payment_checkAmount = models.DecimalField(max_digits=9,decimal_places=2)
    payment_memo = models.CharField(max_length=500)

    contract = models.ForeignKey(Contract, on_delete=models.PROTECT, default=1)



    #this be a toString
    def __str__(self):
        return str(self.payment_memo)


class WorkType(models.Model):
    work = models.CharField(max_length=100)
    vendors= models.ManyToManyField(Vendor, blank=True)
    contracts= models.ManyToManyField(Contract, blank=True)
    class Meta:
        ordering = ['work']

    def __str__(self):
        return self.work




class FileUpload(models.Model):
    uploadName = models.CharField(max_length=100)
    file = models.FileField(upload_to='testFiles\\')