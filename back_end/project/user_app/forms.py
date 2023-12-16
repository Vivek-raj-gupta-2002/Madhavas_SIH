from django import forms
from django.contrib.auth.forms import UserCreationForm
from main_app import models
from user_app.models import UploadForm,document_choice


"""
User authentication form
"""

class UploadFormDoc(forms.ModelForm):

    document_type = forms.ChoiceField(
        choices=document_choice,
        widget=forms.Select(attrs={

            'class': "rectangle-46-CLu"

        })
    )


    document_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': "rectangle-45-acM"
        })
    )

    document = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': "rectangle-45-1bB",
            'type': 'file'
        })
    )

    class Meta:
        model = UploadForm
        fields = ('document_type', 'document_number', 'document')





class ScolarShipForm(forms.Form):
    highersecondarypercentage = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'rectangle-55-gPw'
        })
    )
    transfercertificate = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'group-25-hdo'
        })
    )
    gapcertificate = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'group-24-emK'
        })
    )
    secondaryclasspercentage = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'rectangle-55-iAq'
        })
    )
    lastyearmarksheet = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'group-25-jxR'
        })
    )
    accountholdername = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-69-ccm'
        })
    )
    accountnumber = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'rectangle-70-qdw'
        })
    )
    isfcnumber = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-71-3tR'
        })
    )
    
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-55-f49 '
        })
    )
    dateOfBirth = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'rectangle-55-sQR','type': 'date',
        })
    )
    Fathername = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-56-24M '
        })
    )
    Gender = forms.ChoiceField(
        choices=models.gender_choices,
        widget=forms.Select(attrs={
            'class': 'rectangle-56-1iu '
        })
    )
    Address = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-57-suX'
        })
    )
    PinCode = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'rectangle-58-Wb7'
        })
    )
    MobileNUmber = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'rectangle-60-umf '
        })
    )
    EmailAddress = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'rectangle-59-gR3 '
        })
    )   
    MaritalStatus = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-61-x9b'
        })
    )
      
    CasteCertificate = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-55-Y7f'
        })
    )
    CasteCertificateUpload = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'rectangle-55-Fy7'
        })
    )
    DomicileCertificate = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-56-qrm'
        })
    )
    DomicileCertificateUpload = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'rectangle-56-JXP'
        })
    ) 
    VOterID = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-57-aFw'
        })
    )
    PanCard = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-58-XKb'
        })
    )
    SSmID = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-60-3qf'
        })
    )
    IncomeCertificate = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rectangle-59-PwT'
        })
    )
    IncomeCertificateUpload = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'rectangle-61-Nyj'
        })
    )      







class AuthForm(forms.Form):
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "rectangle-46-Rws"})
    )

    aadhar = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "auto-group-qstq-DMw"})
    )

    OTP = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "rectangle-46-tMb"})
    )

    pin = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "rectangle-45-cgu"})
    )


"""
User Creation Form
"""
class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        del self.fields['password2']


    OTP = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "rectangle-46-vwP"})
    )

    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "rectangle-46-LwF"})
    )

    state = forms.ChoiceField(
        choices=models.INDIAN_STATE_CHOICES,
        widget=forms.Select(attrs={"class": "rectangle-45-2ey"})
    )

    Name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': "rectangle-45-KmF"}
        )

    )


    aadhar_number = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': "auto-group-r3sd-Ev9"}
        )
    )

    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': "rectangle-45-GNy"}),
        input_formats=['%Y-%m-%d']  # This is the format we want to accept.
    )
    
    gender = forms.ChoiceField(
        choices=models.gender_choices,
        widget=forms.Select(attrs={"class": "rectangle-45-5bK"})
    )
    
    institute = forms.ModelChoiceField(
            queryset=models.College.objects.all().order_by('name'),
            widget=forms.Select(attrs={"class":"rectangle-45-5Fs"})
        )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'rectangle-45-5NM'}
        )
    )
    
    
    class Meta:
        model = models.CustomUser
        fields = ['Name', 'phone_number', 'aadhar_number', 'dob', 'gender', 'institute']
        exclude=('password2',)
        


