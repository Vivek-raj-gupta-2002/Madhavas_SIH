from django.db import models
from main_app.models import CustomUser


# Create your models here.

gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

document_choice = (
    ('Aadhar Card', 'Aadhar Card'),
    ('Pan Card', 'Pan Card'),
    ('Voter Id', 'Voter Id'),
    ('Health Card', 'Health Card'),
    ('ABC', 'ABC'),
    ('Driving Licience', 'Driving Licience'),
    ('10th Marksheet', '10th Marksheet'),
    ('12th Marksheet', '12th Marksheet'),
    ('Migration', 'Migration'),
    ('Trancerfer Certificate', 'Trancerfer Certificate'),
    ('Marksheet', 'Marksheet'),
    ('GAP Certificate', 'GAP Certificate'),
    ('Admission Slip', 'Admission Slip'),
    ('Domacile', 'Domacile'),
    ('Income', 'Income'),
    ('Caste', 'Caste'),
    ('Samagra', 'Samagra'),
    ('Bank Passbook', 'Bank Passbook'),

)


class UploadForm(models.Model):

    document_type = models.CharField(max_length=100, choices=document_choice)

    document_number = models.BigIntegerField()

    document = models.FileField(upload_to='documents')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('document_type', 'user')


class ScholarShipFormModel(models.Model):
    filed_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    Fathername = models.CharField(max_length=100)
    Gender = models.CharField(max_length=1, choices=gender_choices)
    Address = models.CharField(max_length=100)
    PinCode =  models.IntegerField()
    MobileNUmber = models.CharField(max_length=20)
    EmailAddress = models.EmailField()
    institute = models.CharField(max_length=100)
    CasteCertificate = models.CharField(max_length=100)
    CasteCertificateUpload = models.FileField() 
    DomicileCertificate = models.CharField(max_length=100)
    DomicileCertificateUpload = models.FileField()
    VOterID = models.CharField(max_length=100)
    PanCard = models.FileField()
    # inst
    SSmID = models.CharField(max_length=100)
    IncomeCertificate= models.CharField(max_length=100)
    IncomeCertificateUpload = models.FileField()

    is_institute_verify = models.BooleanField(default=False)
    is_state_verify = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    is_money_depo = models.BooleanField(default=False)
 



    