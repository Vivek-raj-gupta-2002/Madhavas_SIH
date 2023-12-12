from django import forms
from django.contrib.auth.forms import UserCreationForm
from main_app import models


"""
User authentication form
"""

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
        


