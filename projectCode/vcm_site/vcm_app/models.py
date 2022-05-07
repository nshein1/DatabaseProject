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
    contract_notes = models.TextField(blank=True)

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

 #beginning of 457 Database models
class Building(models.Model):
    Address = models.CharField(max_length=30)
    Owner_Company = models.CharField(max_length=20)
    Zip_Code = models.CharField(max_length=10)
    PO_Box = models.IntegerField
    Building_ID = models.CharField(max_length=7, primary_key=True, unique=True)

class Unit(models.Model):
    Unit_ID = models.CharField(max_length=7, primary_key=True, unique=True)
    Unit_Number = models.IntegerField
    Unit_Floor = models.IntegerField
    Unit_Type = models.CharField(max_length=20)
    Num_of_Bedrooms = models.IntegerField
    Num_of_Bathrooms = models.IntegerField
    Balcony = models.BooleanField
    Availability = models.BooleanField
    Building_ID = models.ForeignKey(Building, on_delete=models.PROTECT)

    def get_Availability(self):
        return self.Availability

    class Meta:
        ordering = ['Unit_Number']

class Person(models.Model):
    Person_Name = models.CharField(max_length=22)
    SSN = models.IntegerField(max_length=10, unique=True)
    Permanent_Address = models.CharField(max_length=30)
    ID = models.CharField(max_length=7, primary_key=True, unique=True)

    #seems redundant, but for argument ordering it isn't
    Tenant = 'Tenant'
    Staff = 'Staff'

    Person_Types = [
        (Tenant, 'Tenant'),
        (Staff, 'Staff')
    ]

    Person_Type = models.CharField(max_length=6, choices=Person_Types, default=Tenant)

    def is_Tenant(self):
        return self.Person_Type in {self.Tenant}

    class Meta:
        ordering = ['Person_Name']

class Lease(models.Model):
    Direct_or_Guarantor = models.CharField(max_length=1) #D will mean Direct, G will mean Guarantor; figure out ChoiceField later
    Lease_ID = models.CharField(max_length=7, primary_key=True, unique=True)
    Renter_ID = models.CharField(max_length=7)
    Rent_Amount = models.DecimalField(max_digits=7, decimal_places=2)

    Application = 'Lease Application'
    Active_Lease = 'Active Lease'

    Lease_Types = [
        (Application, 'Application'),
        (Active_Lease, 'Active Lease')
    ]

    Lease_Type = models.CharField(max_length=20, choices=Lease_Types, default=Active_Lease)

    def is_Active(self):
        return self.Lease_Type in {self.Active_Lease}

class Parking(models.Model):
    Permit_Number = models.IntegerField
    License_Plate = models.CharField(max_length=8) #weird fractional plates
    Govt_ID = models.ForeignKey(Person, on_delete=models.CASCADE)
    Allowed_Floor = models.IntegerField
    Parking_Permit_ID = models.CharField(max_length=7, primary_key=True, unique=True)

class Maintenance_Request(models.Model):
    Issue = models.CharField(max_length=30)
    Work_Order_ID = models.CharField(max_length=7, primary_key=True, unique=True)
    Unit_ID = models.ForeignKey(Unit, on_delete=models.CASCADE)

class Payment_Ledger(models.Model):
    Unit_ID = models.ForeignKey(Unit, on_delete=models.CASCADE, primary_key=True)
    Lease_ID = models.ForeignKey(Lease, on_delete=models.CASCADE, primary_key=True)
    Renter_ID = models.ForeignKey(Person, on_delete=models.CASCADE, primary_key=True)
    Parking_Permit_ID = models.ForeignKey(Parking, on_delete=models.CASCADE)
    Work_Order_ID = models.ForeignKey(Maintenance_Request, on_delete=models.CASCADE)

class Inspection(models.Model):
    Inspection_Date_Time = models.DateTimeField
    Unit_ID = models.ForeignKey(Unit, on_delete=models.CASCADE)
    Building_ID = models.ForeignKey(Building, on_delete=models.CASCADE)
    Inspection_ID = models.CharField(max_length=7, primary_key=True, unique=True)
    Reason = models.TextField(blank=True, max_length=255)
    Performed_By = models.ForeignKey(Person, on_delete=models.CASCADE)

class Rent_Payment(models.Model):
    Payment_Deadline = models.DateTimeField
    Payment_Date = models.DateTimeField
    Amount_Paid = models.DecimalField(max_digits=7, decimal_places=2)
    Payment_ID = models.CharField(max_length=7, primary_key=True, unique=True)
    Unit_ID = models.ForeignKey(Unit, on_delete=models.CASCADE)

    class Meta:
        ordering = ['Payment_Deadline']

class Amenities(models.Model):
    Amenities_Type = models.CharField(max_length=20)
    Amenities_Location = models.CharField(max_length=20)
