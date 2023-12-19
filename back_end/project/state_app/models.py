from django.db import models
from main_app.models import cast_choice

# Create your models here.

class ShowForm(models.Model):
    title = models.CharField(max_length=100)
    apply_link = models.URLField(max_length=100)

    # cretria
    caste = models.CharField(choices=cast_choice, max_length=50)
    income = models.IntegerField()
    percentage = models.IntegerField()
    state = models.CharField(max_length=100)


