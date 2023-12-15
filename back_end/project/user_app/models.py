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

    class Meta:
        unique_together = ('document_type', 'user')