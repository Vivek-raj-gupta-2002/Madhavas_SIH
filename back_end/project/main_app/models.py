from django.db import models
from django.contrib.auth.models import AbstractUser

gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),

)

cast_choice = (
    ('g', 'General'),
    ('sc', 'Scheduled Caste'),
    ('st', 'Scheduled Tribe'),
    ('obc', 'Other Backward Class'),
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
    
    # identifiers
    username = models.CharField(max_length=100, primary_key=True)
    phone_number = models.CharField(max_length=10, unique=True)
    aadhar_number = models.CharField(max_length=12, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)

    #personal Details
    Name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=gender_choices)
    dob = models.DateField()

    #not null
    institute = models.CharField(max_length=100, null=True, blank=True)
    caste = models.CharField(max_length=20, null=True, blank=True, choices=cast_choice)

    is_institute = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    #image field
    profile_pic = models.ImageField(upload_to='profile')

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = [
        'phone_number',
        'Name',
        'dob',
        'gender',
        'email'
    ]
    
