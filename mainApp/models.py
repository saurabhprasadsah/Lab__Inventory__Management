from django.db import models
from datetime import date
import uuid

class ChainOfCustody(models.Model):
    id=models.AutoField(primary_key=True)
    COC_UUID =models.UUIDField(max_length=100, unique=True, default=uuid.uuid4, editable = False)
    Client_ID = models.CharField(max_length=60, verbose_name='Client ID')
    Date = models.DateField(default=date.today, verbose_name= 'Date')
    Order_of_the_Form = models.PositiveIntegerField(verbose_name='Order of the Form cronology')
    # file will be uploaded to MEDIA_ROOT/uploads/day/month/year
    #COC_File_Upload = models.FileField(upload_to="COC Files/%d/%m/%Y/",verbose_name= 'COC File Upload')
    COC_File_Upload = models.FileField(upload_to ="COC Files/%d/%m/%Y/",verbose_name= 'COC File Upload')

    COC_ID = models.CharField(max_length=1000, verbose_name='COC Form ID')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Client_ID

    def save(self, *args, **kwargs):
        super(ChainOfCustody, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Chain of Custody (FO-063)'  


class SampleIntakeForm(models.Model):
    id = models.AutoField(primary_key=True) 
    SIF_UUID=models.UUIDField(max_length=100, unique=True, default=uuid.uuid4, editable = False)
    Date = models.DateField(default=date.today, verbose_name= 'Date')
    Sample_ID = models.CharField(max_length=40, unique=False)
    Sample_Name = models.CharField(max_length=300, unique=False, verbose_name='Sample Name')
    Matrix = models.CharField(max_length=300, unique=False, verbose_name='Matrix')
    Batch_Number = models.CharField(max_length=300, unique=False, verbose_name='Batch Number')
    Sample_Size = models.PositiveIntegerField(verbose_name='Sample Size')
    Batch_Size = models.PositiveIntegerField(verbose_name='Batch Size')
    Distributor_Micro_business_Name = models.CharField(max_length=300, unique=False, verbose_name='Distributor / Micro business Name')
    Distributor_Micro_business_License_No = models.CharField(max_length=300, unique=False, verbose_name='Distributor / Micro business License No')
    Chain_of_Custody_Number = models.CharField(max_length=300, unique=False, verbose_name='Chain of Custody Number')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Client_ID
    
    def save(self, *args, **kwargs):
        super(SampleIntakeForm, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Sample Intake Log (FO-043)'  
        

class SampleTrackingForm(models.Model):
    Analysis_Status = (
    ('Null','NA'),
    ('Pending','Pending'),
    ('Completed','Completed'),
    )
    
    id = models.AutoField(primary_key=True) 
    STF_UUID = models.UUIDField(max_length=100, unique=True, default=uuid.uuid4, editable = False)    
    Sample_ID = models.CharField(max_length=40, unique=False)
    SIF_Id = models.CharField(max_length=40, unique=False, editable=False)
    Cannabinoids = models.BooleanField("Cannabinoids", default=False)
    Cannabinoids_Workgroup_ID = models.CharField(max_length=300, unique=False, verbose_name='Cannabinoids Workgroup ID')
    Cannabinoids_Sample_weight = models.DecimalField( default=0, blank = True, null = True, max_digits = 30, decimal_places = 10 , verbose_name='Cannabinoids Sample weight')
    Cannabinoids_Analysis_Status = models.CharField(max_length=100, choices=Analysis_Status, default='NA')
    Water_Activity = models.BooleanField("Water Activity", default=False)
    Water_Activity_Workgroup_ID = models.CharField(max_length=300, unique=False, verbose_name='Water Activity Workgroup ID')
    Water_Activity_Sample_weight = models.DecimalField( default=0, blank = True, null = True, max_digits = 30, decimal_places = 10 , verbose_name='Water Activity Sample weight')
    Water_Activity_Analysis_Status = models.CharField(max_length=100, choices=Analysis_Status, default='NA')
    Micro = models.BooleanField("Micro", default=False)
    Micro_Workgroup_ID = models.CharField(max_length=300, unique=False, verbose_name='Micro Workgroup ID')
    Micro_Sample_weight = models.DecimalField( default=0, blank = True, null = True, max_digits = 30, decimal_places = 10 , verbose_name='Micro Sample weight')
    Micro_Analysis_Status = models.CharField(max_length=100, choices=Analysis_Status, default='NA')
    Pesticides_and_Mycotoxins = models.BooleanField("Pesticides and Mycotoxins", default=False)
    Pesticides_and_Mycotoxins_Workgroup_ID = models.CharField(max_length=300, unique=False, verbose_name='Pesticides and Mycotoxins Workgroup ID')
    Pesticides_and_Mycotoxins_Sample_weight = models.DecimalField( default=0, blank = True, null = True, max_digits = 30, decimal_places = 10 , verbose_name='Pesticides and Mycotoxins Sample weight')
    Pesticides_and_Mycotoxins_Analysis_Status = models.CharField(max_length=100, choices=Analysis_Status, default='NA')
    Residual_Solvents = models.BooleanField("Residual Solvents", default=False)
    Residual_Solvents_Workgroup_ID = models.CharField(max_length=300, unique=False, verbose_name='Residual Solvents Workgroup ID')
    Residual_Solvents_Sample_weight = models.DecimalField( default=0, blank = True, null = True, max_digits = 30, decimal_places = 10 , verbose_name='Residual Solvents Sample weight')
    Residual_Solvents_Analysis_Status = models.CharField(max_length=100, choices=Analysis_Status, default='NA')
    Foreign_Material = models.BooleanField("Foreign Material", default=False)
    Foreign_Material_Workgroup_ID = models.CharField(max_length=300, unique=False, verbose_name='Foreign Material Workgroup ID')
    Foreign_Material_Sample_weight = models.DecimalField( default=0, blank = True, null = True, max_digits = 30, decimal_places = 10 , verbose_name='Foreign Material Sample weight')
    Foreign_Material_Analysis_Status = models.CharField(max_length=100, choices=Analysis_Status, default='NA')
    Moisture_Content = models.BooleanField("Moisture Content", default=False)
    Moisture_Content_Workgroup_ID = models.CharField(max_length=300, unique=False, verbose_name='Moisture Content Workgroup ID')
    Moisture_Content_Sample_weight = models.DecimalField( default=0, blank = True, null = True, max_digits = 30, decimal_places = 10 , verbose_name='Moisture Content Sample weight')
    Moisture_Content_Analysis_Status = models.CharField(max_length=100, choices=Analysis_Status, default='NA')
    Heavy_Metals = models.BooleanField("Heavy Metals", default=False)
    Heavy_Metals_Workgroup_ID = models.CharField(max_length=300, unique=False, verbose_name='Heavy Metals Workgroup ID')
    Heavy_Metals_Sample_weight = models.DecimalField( default=0, blank = True, null = True, max_digits = 30, decimal_places = 10 , verbose_name='Heavy Metals Sample weight')
    Heavy_Metals_Analysis_Status = models.CharField(max_length=100, choices=Analysis_Status, default='NA')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super(SampleTrackingForm, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Sample Intake Log (FO-114)' 


class SampleRetainForm(models.Model):
    id = models.AutoField(primary_key=True) 
    SRF_UUID=models.UUIDField(max_length=100, unique=True, default=uuid.uuid4, editable = False)
    Date = models.DateField(default=date.today, verbose_name= 'Date')
    Sample_ID = models.CharField(max_length=40, unique=False, editable=False)
    Sample_Name = models.CharField(max_length=300, unique=False, verbose_name='Sample Name')
    Matrix = models.CharField(max_length=300, unique=False, verbose_name='Matrix')
    Batch_Number = models.CharField(max_length=300, unique=False, verbose_name='Batch Number')
    Sample_Size = models.PositiveIntegerField(verbose_name='Sample Size')
    Batch_Size = models.PositiveIntegerField(verbose_name='Batch Size')
    Distributor_Micro_business_Name = models.CharField(max_length=300, unique=False, verbose_name='Distributor / Micro business Name')
    Distributor_Micro_business_License_No = models.CharField(max_length=300, unique=False, verbose_name='Distributor / Micro business License No')
    Chain_of_Custody_Number = models.CharField(max_length=300, unique=False, verbose_name='Chain of Custody Number')
    Days_Retailed = models.PositiveIntegerField(verbose_name='Days Retailed')
    Disposal_Status = models.CharField(max_length=300, unique=False, verbose_name='Disposal Status')    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super(SampleRetainForm, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Sample Sample Retention Log (FO-044)'  