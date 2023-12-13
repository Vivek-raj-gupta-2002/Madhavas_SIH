from main_app import models

"""
getting all the data from dummy database 
that we are considering is comming from Digilocker

These function can be replaced with req API's in future
"""

def get_aadhar(aadhar_no):
    return models.AadharInfo.objects.filter(aadhar_no=aadhar_no).first()

def get_income(aadhar_no):
    return models.Income.objects.filter(aadhar_no=get_aadhar(aadhar_no)).first()

def get_domicile(aadhar_no):
    return models.Domicile.objects.filter(aadhar_no=get_aadhar(aadhar_no)).first()

def get_caste(aadhar_no):
    return models.CasteData.objects.filter(aadhar_no=get_aadhar(aadhar_no)).first()

def get_marksheet(aadhar_no):
    return models.Marksheet.objects.filter(aadhar_no=get_aadhar(aadhar_no))
