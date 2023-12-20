from django import forms
from .models import StateScholarForm


class StateForm(forms.ModelForm):
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

    caste=forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'rectangle-72-9TT'}
        )
    )


    income=forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'rectangle-72-9TT'}
        )
    )

    percentage=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class':'rectangle-72-9TT'}
        )
    )

    state=forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'rectangle-72-9TT'}
        )
    )

    attandence=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class':'rectangle-72-9TT'}
        )
    )

    class Meta:
        model = StateScholarForm
        fields = '__all__'


