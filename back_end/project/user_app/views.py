# remember their are multiple types of user while authenticating
from django.shortcuts import render

from main_app.models import OneTimePass
from . import forms

from django.views.decorators.http import require_http_methods
from utills import mail, dummy_data
from django.http import HttpResponse
from random import randint


# Create your views here.


#end point to get otp
@require_http_methods(["GET"])
def send_otp(request, aadhar):

    # get data from dummy database

    data = dummy_data.get_aadhar(aadhar_no=aadhar)

    if data:

        # create and send OTP
        otp = randint(1000, 9999)
        mail.send_email_to_client(
            "OTP for verification",
            f"Your Verification Code for aadhar {aadhar} is {otp}",
            data.email
        )

        # create new object

        obj, created = OneTimePass.objects.update_or_create(
            aadhar_no=aadhar
        )

        # add otp and save it

        obj.otp = otp
        obj.save()

        return HttpResponse("Done")
    
    else:
        return HttpResponse("Invalid Aadhar")
