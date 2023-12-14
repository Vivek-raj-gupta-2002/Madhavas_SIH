from django.db import models
from main_app.models import CustomUser

# Create your models here.


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


class InternJob(models.Model):
    org_name = models.CharField(max_length=255, unique=True)

    du_to = models.DateField()

    du_from = models.DateField()

    skill_req = models.CharField(max_length=255) 

    no_openning = models.IntegerField()

    max_pay = models.IntegerField()

    min_pay = models.IntegerField()

    short_des = models.TextField()


class Hackathon(models.Model):
    orga_name = models.CharField(max_length=255, unique=True)

    da_to = models.DateField()

    da_from = models.DateField()

    max_members = models.IntegerField() 

    link_to = models.URLField()

    on_mode = models.BooleanField(default=False)

    off_mode = models.BooleanField(default=False)

    short_desc = models.TextField()

class Scholarship(models.Model):
    orga_name = models.CharField(max_length=255, unique=True)

    da_to = models.DateField()

    da_from = models.DateField()

    min_percent = models.IntegerField() 

    amount_given = models.ImageField()

    on_mode = models.BooleanField(default=False)

    off_mode = models.BooleanField(default=False)

    short_desc = models.TextField()


