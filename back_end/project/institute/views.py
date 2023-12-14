from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.


def internshipView(requests):
    my_form = forms.InternForm()

    return render(requests, 'institute/internships-jobs.html', {'form': my_form})



def scholarView(requests):
    my_form = forms.ScholarForm()

    return render(requests, 'institute/scholarships.html', {'form': my_form})
