from django import forms
from . import models

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
        
        fields = ['orga_name','da_to' , 'da_from' , 'min_percent' , 'amount_given', 'on_mode','off_mode','short_desc']
