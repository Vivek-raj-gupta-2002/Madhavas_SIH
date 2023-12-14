from django.db import models

# Create your models here.

class InternJob_model(models.Model):
    org_name = models.CharField(max_length=255, unique=True)

    du_to = models.DateField()

    du_from = models.DateField()

    skill_req = models.CharField(max_length=255) 

    no_openning = models.IntegerField()

    max_pay = models.IntegerField()

    min_pay = models.IntegerField()

    short_des = models.TextField()


class Hackathon_model(models.Model):
    orga_name = models.CharField(max_length=255, unique=True)

    da_to = models.DateField()

    da_from = models.DateField()

    max_members = models.IntegerField() 

    link_to = models.URLField()

    on_mode = models.BooleanField(default=False)

    off_mode = models.BooleanField(default=False)

    short_desc = models.TextField()

class Scholarship_model(models.Model):
    orga_name = models.CharField(max_length=255, unique=True)

    da_to = models.DateField()

    da_from = models.DateField()

    min_percent = models.IntegerField() 

    amount_given = models.IntegerField()

    on_mode = models.BooleanField(default=False)

    off_mode = models.BooleanField(default=False)

    short_desc = models.TextField()


