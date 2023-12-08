from django.db import models
from django.contrib.auth.models import AbstractUser

gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),

)

# Create your models here.


# the custom user model
"""
Having different values according to roles such as:-
is_staff = Backend team
is_superuser = Admin
is_active = Active user
is_student = main user
is_institute = Institutations

"""
class CustomUser(AbstractUser):
    # unique Fields
    username = models.CharField(max_length=100, null=False, unique=True, primary_key=True)
    
    # unique but can null
    aadhar = models.CharField(max_length=12, null=True, unique=True, blank=True)
    email = models.EmailField(max_length=100, unique=False, null=True)
    
    # not unique and null
    profile_pic = models.ImageField(upload_to='profile', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, null=True)
    date_of_birth = models.DateField(null=True)

    # not unique not null
    is_student = models.BooleanField(default=True)
    is_institute = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = [
        'email'
    ]
