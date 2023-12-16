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



class InternForm(forms.ModelForm): 
    organiser = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-72-Mdo'})
    )
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-72-Mdo'})
    )
    logo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'logo-input'})
    )

    Start_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'auto-group-y15p-GPP', 'type': 'date',
        })
    )
    End_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'auto-group-yzch-fgR', 'type': 'date', })
    )
    skillsrequired = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-75-hWd'})
    )
    openings = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-81-XEm'})
    )
    maxpay = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-78-WMb'})
    )
    minpay = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-80-wC1'})
    )
    apply = forms.URLField(
        widget=forms.URLInput(attrs={'class':'rectangle-72-Mdo'})
    ) 
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'shortdiscription-dKj'})
    )
    class Meta:
        model = models.Oppertunities_model
        fields = (
            'organiser', 'title', 'logo', 'Start_date', 'End_date', 'openings',
            'description','apply', 'skillsrequired',
            'maxpay', 'minpay',
        )



class ScholarForm(forms.ModelForm):
    organiser = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-72-9TT'})
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-72-9TT'})
    )

    logo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'logo-input'})
    )


    Start_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'auto-group-juvd-qDo', 'type': 'date', })
    )
    End_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'auto-group-zfup-cds', 'type': 'date', })
    )

    openings = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-72-9TT'})
    )

    amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-78-4Xo'})
    )

    apply = forms.URLField(
        widget=forms.URLInput(attrs={'class':'rectangle-72-9TT'})
    ) 

    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'auto-group-vw2q-95P'})
    )
    class Meta: 
        model = models.Oppertunities_model
        fields = (
            'organiser', 'title', 'logo', 'Start_date', 'End_date', 'openings',
            'description','apply', 'amount'
        )

class Hackathon(forms.ModelForm):
    organiser = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-72-GHT'})
    )
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'rectangle-72-GHT'})
    )
    logo = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'logo-input'})
    )

    Start_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'auto-group-n997-ZQy', 'type': 'date',
        })
    )
    End_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'auto-group-bjgu-4m3', 'type': 'date', })
    )
    openings = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'rectangle-72-GHT'})
    )
    
    onlinemode = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'rectangle-77-gbP'}),
        required=False
    )
    offlinemode = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'rectangle-77-gbP'}),
        required=False
    )
    apply = forms.URLField(
        widget=forms.URLInput(attrs={'class':'rectangle-72-GHT'})
    ) 
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'auto-group-auvu-YtV'})
    )


    class Meta:
        model = models.Oppertunities_model
        fields = (
            'organiser', 'title', 'logo', 'Start_date', 'End_date', 'openings',
            'description','apply', 'onlinemode', 'offlinemode',
        )

