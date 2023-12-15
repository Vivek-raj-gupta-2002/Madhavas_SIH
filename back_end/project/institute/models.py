from django.db import models

# Create your models here.

class Oppertunities_model(models.Model):
    logo = models.ImageField(upload_to='intern')
    title = models.CharField(max_length=100)
    description = models.TextField()
    organiser = models.CharField(max_length=100)
    apply = models.URLField()
    amount = models.DecimalField(decimal_places=3, max_digits=10)
    Start_date = models.DateField()
    End_date = models.DateField()
    is_online = models.BooleanField(default=False)
    is_offline = models.BooleanField(default=False)
    openings = models.IntegerField(null=True, blank=True)
#    skills required,max pay,min pay
    is_scholarship = models.BooleanField(default=False)
    is_hack = models.BooleanField(default=False)
    is_intern = models.BooleanField(default=False)


