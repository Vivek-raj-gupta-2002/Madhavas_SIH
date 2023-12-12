# remember their are multiple types of user while authenticating
from django.shortcuts import render, redirect

from main_app.models import OneTimePass, CustomUser, College
from . import forms

from django.views.decorators.http import require_http_methods
from utills import mail, dummy_data, valid_otp
from django.http import HttpResponse
from random import randint

from django.contrib.auth import authenticate, login, logout


# Create your views here.
"""
usertype = student
"""
def logout_view(request):
    logout(request)
    
    return redirect('login')


def dashboard_view(request):
    return HttpResponse("Dashboard")

# authenticate user 
def login_view(request):
    # if user is already authenticated then
    # redirect to dashboard ------------------------------------------>
    if request.user.is_authenticated:
        return redirect('dashboard')

    # initilise a empty form
    my_form = forms.AuthForm()

    # if the request to get loggined
    if request.method == 'POST':
        my_form = forms.AuthForm(request.POST)

        # checking if the form follows all the validation
        if my_form.is_valid():
            
            aadhar = my_form['aadhar'].value()
            otp = my_form['OTP'].value()
            pin = my_form['pin'].value()
            phone = my_form['phone_number'].value()


            # authenticate the user
            my_user = authenticate(request, username=aadhar, password=pin)

            if my_user:
                # authenticated
                
                if valid_otp.check_otp(aadhar, otp):
                    # validating the otp
                    
                    if phone == CustomUser.objects.filter(username=aadhar).first().phone_number:
                    
                        # Logging the user in
                        login(request, my_user)

                        return redirect('dashboard') # redirect to dashboard ------------------------------->
                    
                    else:
                        my_form.add_error("phone_number", 'Incorrect phone')    

                else:
                    my_form.add_error("OTP", 'Incorrect OTP')

                
            
            else:
                my_form.add_error("pin", 'Incorrect PIN')


    return render(request, 'user_app/log-in.html', {'form': my_form})

# creating user
def signup(request):
    # if user is already authenticated then
    # redirect to dashboard ------------------------------------------>
    if request.user.is_authenticated:
        return redirect('dashboard')

    my_form = forms.SignupForm()# created the form
    
    if request.method == 'POST':# if the req is post then

        my_form = forms.SignupForm(request.POST)#get the form data
        
        if my_form.is_valid():# check if all fields are validated
            
            aadhar = my_form['aadhar_number'].value()
            otp = my_form['OTP'].value()

            # validating the otp
            if valid_otp.check_otp(aadhar, otp):

                data = dummy_data.get_aadhar(aadhar_no=aadhar)

                try:

                   
                    user = CustomUser.objects.create_user(
                        username=aadhar,
                        aadhar_number=aadhar,
                        password=my_form['password1'].value(),
                        is_student=True,
                        is_verified=True,
                        gender=my_form['gender'].value(),
                        Name=my_form['Name'].value(),
                        institute=College.objects.get(id=my_form['institute'].value()),
                        dob=my_form['dob'].value(),
                        email=data.email,
                        phone_number = my_form['phone_number'].value()
                    )
                    
                    user.save()
                    return redirect('login')
                except:
                    my_form.add_error("OTP", "Something Went wrong")
        
        else:
            my_form.add_error("OTP", "Invalid Otp")
        
        

    return render(request, 'user_app/sign-up-log-in.html', {'form': my_form})


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
