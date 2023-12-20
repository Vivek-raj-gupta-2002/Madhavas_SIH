from django.db import models
from main_app.models import cast_choice, INDIAN_STATE_CHOICES
from user_app.models import CustomUser


# Create your models here.


class StateScholarForm(models.Model):
    
    caste=models.CharField(max_length=100, choices=cast_choice)
    income=models.CharField(max_length=100)
    percentage=models.IntegerField()
    state=models.CharField(max_length=100, choices=INDIAN_STATE_CHOICES)
    attandence=models.IntegerField()

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='intern')
    title = models.CharField(max_length=100)
    description = models.TextField()
    organiser = models.CharField(max_length=100)
    apply = models.URLField()
    amount = models.DecimalField(decimal_places=3, max_digits=10, null=True, blank=True)
    Start_date = models.DateField()
    End_date = models.DateField()
    is_online = models.BooleanField(default=False, null=True, blank=True)
    is_offline = models.BooleanField(default=False, null=True, blank=True)
    openings = models.IntegerField()
    skillsrequired = models.CharField(max_length=100, null=True, blank=True)
    maxpay = models.IntegerField(null=True, blank=True)
    minpay = models.IntegerField(null=True, blank=True)



