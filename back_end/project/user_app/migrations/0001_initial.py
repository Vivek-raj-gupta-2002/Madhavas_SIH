# Generated by Django 5.0 on 2023-12-19 23:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarShipFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateOfBirth', models.DateField()),
                ('Fathername', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('Address', models.CharField(max_length=100)),
                ('PinCode', models.IntegerField()),
                ('MobileNUmber', models.CharField(max_length=20)),
                ('EmailAddress', models.EmailField(max_length=254)),
                ('MaritalStatus', models.CharField(max_length=100)),
                ('CasteCertificate', models.CharField(max_length=100)),
                ('CasteCertificateUpload', models.FileField(upload_to='')),
                ('DomicileCertificate', models.CharField(max_length=100)),
                ('DomicileCertificateUpload', models.FileField(upload_to='')),
                ('VOterID', models.CharField(max_length=100)),
                ('PanCard', models.FileField(upload_to='')),
                ('SSmID', models.CharField(max_length=100)),
                ('IncomeCertificate', models.CharField(max_length=100)),
                ('IncomeCertificateUpload', models.FileField(upload_to='')),
                ('is_institute_verify', models.BooleanField(default=False)),
                ('is_state_verify', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('is_money_depo', models.BooleanField(default=False)),
                ('filed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('Aadhar Card', 'Aadhar Card'), ('Pan Card', 'Pan Card'), ('Voter Id', 'Voter Id'), ('Health Card', 'Health Card'), ('ABC', 'ABC'), ('Driving Licience', 'Driving Licience'), ('10th Marksheet', '10th Marksheet'), ('12th Marksheet', '12th Marksheet'), ('Migration', 'Migration'), ('Trancerfer Certificate', 'Trancerfer Certificate'), ('Marksheet', 'Marksheet'), ('GAP Certificate', 'GAP Certificate'), ('Admission Slip', 'Admission Slip'), ('Domacile', 'Domacile'), ('Income', 'Income'), ('Caste', 'Caste'), ('Samagra', 'Samagra'), ('Bank Passbook', 'Bank Passbook')], max_length=100)),
                ('document_number', models.BigIntegerField()),
                ('document', models.FileField(upload_to='documents')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('document_type', 'user')},
            },
        ),
    ]
