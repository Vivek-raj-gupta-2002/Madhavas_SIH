from django import forms
from . import models

class ApiLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-45-pdb'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'rectangle-45-pdb'}),  # this makes the input field for password to be hidden by default

    )
    
    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-45-pdb'})
    )



class InternForm(forms.Form):
    organizationname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-72-Mdo'})
    )
    duration = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'auto-group-y15p-GPP', 'type': 'date',
        })
    )
    duration1 = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'auto-group-yzch-fgR', 'type': 'date', })
    )
    skillsrequired = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-75-hWd'})
    )
    noofopening = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-81-XEm'})
    )
    maxpay = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-78-WMb'})
    )
    minpay = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-80-wC1'})
    )
    shortdiscription = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'shortdiscription-dKj'})
    )
    class Meta:
        
        fields = ['orga_name','da_to' , 'da_from' , 'skill_req' , 'no_openning', 'max_pay',' min_pay','short_desc']
    



class ScholarForm(forms.Form):
    organizationname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-72-9TT'})
    )

    dateforthetest = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'auto-group-juvd-qDo', 'type': 'date', })
    )
    dateforthetest1 = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'auto-group-zfup-cds', 'type': 'date', })
    )

    minpercentagerequired = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-75-fkZ'})
    )

    amounttobegiven = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-78-4Xo'})
    )

    onlinemode = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'auto-group-gmqw-j89P'})
    )
    offlinemode = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'rectangle-77-uB3'})
    )
    shortdescription = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'auto-group-vw2q-95P'})
    )
    class Meta: 
        
        fields = ['orga_name','da_to' , 'da_from' , 'min_percent' , 'amount_given', 'on_mode','off_mode','short_desc']