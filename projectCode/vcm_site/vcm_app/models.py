from django.db import models

from django.core.validators import MinValueValidator

# Create your models here.

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    vendor_email = models.EmailField(max_length=100)# default="test@test.com") #THIS IS A PLACEHOLDER
    

    #NEW FIELDS START HERE
    vendor_phone = models.CharField(max_length=10, blank=True)
    vendor_website = models.URLField(blank=True)
    vendor_notes = models.TextField(blank=True)
    vendor_poc = models.TextField(blank=True)

    """Identification Method Stuff"""
    BIDDING     = 'B'
    REFERRAL   = 'R'
    ADVERTISEMENT   = 'A'
    VENDOR_REFERRAL_CHOICES = [
        (BIDDING, 'Bidding'),
        (REFERRAL, 'Referral'),
        (ADVERTISEMENT, 'Advertisement'),
    ]

    vendor_referral =  models.CharField(
        max_length=1,
        choices=VENDOR_REFERRAL_CHOICES,
        default=ADVERTISEMENT,
    )

    #NEW FIELDS END HERE

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
    #votes = models.IntegerField(default=0)
    #TypeofWorks = models.ManyToManyField(TypeofWork)

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

 
