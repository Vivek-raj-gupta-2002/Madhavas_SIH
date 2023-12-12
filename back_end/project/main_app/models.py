from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

classes = (
    ('1', '10th'),
    ('2', '12th'),
)

cast_choice = (
    ('G', 'General'),
    ('SC', 'Scheduled Caste'),
    ('ST', 'Scheduled Tribe'),
    ('OBC', 'Other Backward Class'),
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
    is_verified = models.BooleanField(default=False)

    #image field
    profile_pic = models.ImageField(upload_to='profile', blank=True, null=True)

    # objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = [
        'phone_number',
        'Name',
        'dob',
        'gender',
        'email'
    ]
    
# all dummy database defination
class AadharInfo(models.Model):
    aadhar_no = models.CharField(max_length=12, primary_key=True)
    holder_name = models.CharField(max_length=45)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=45)

    def __str__(self) -> str:
        return str(self.aadhar_no)
    
    def formatted_date(self):
        return self.your_date_field.strftime('%m-%d-%y')


class CasteData(models.Model):
    aadhar_no = models.OneToOneField(AadharInfo, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=100)
    caste = models.CharField(max_length=20, choices=cast_choice)

    def __str__(self) -> str:
        return str(self.aadhar_no)
    
class Domicile(models.Model):
    aadhar_no = models.OneToOneField(AadharInfo, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.aadhar_no)
    
class Income(models.Model):
    aadhar_no = models.OneToOneField(AadharInfo, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

    def __str__(self) -> str:
        return str(self.aadhar_no)
    
class Marksheet(models.Model):
    aadhar_no = models.ForeignKey(AadharInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    marks = models.CharField(max_length=5)
    standard = models.CharField(max_length=1, choices=classes)


    def __str__(self) -> str:
        return str(self.aadhar_no)
    
    class Meta:
        # Specify the unique constraint for a combination of field1 and field2
        unique_together = ('aadhar_no', 'standard')


class OneTimePass(models.Model):
    aadhar_no = models.CharField(max_length=100, primary_key=True)
    otp = models.CharField(max_length=6)
    sending_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.aadhar_no) + str(self.sending_time)