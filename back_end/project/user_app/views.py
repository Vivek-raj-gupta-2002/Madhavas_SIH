# remember their are multiple types of user while authenticating
from django.shortcuts import render, redirect

from main_app.models import OneTimePass, CustomUser, College
from . import models
from . import forms

from django.views.decorators.http import require_http_methods
from utills import mail, dummy_data, valid_otp
from django.http import HttpResponse, Http404
from random import randint

from django.contrib.auth import authenticate, login, logout


links = {
    'scholar': 'https://cdn.s3waas.gov.in/s31385974ed5904a438616ff7bdb3f7439/uploads/2019/06/2019062152.jpg'
}

# Create your views here.
@require_http_methods(["GET", "POST"])
def scholar(request):
    my_form = forms.ScolarShipForm()

    
    return render(request, "main.html", {'form': my_form})
    

#ScholarshipForm

@require_http_methods(["GET", "POST"])
def scholarShip(request, number):
    my_form = forms.ScolarShipForm()

    if number == 1:
    
        return render(request, "Scholarship/scholarshipform4.html", {'form': my_form})


    elif number == 2:
        
        return render(request, "Scholarship/scholarshipform.html", {'form': my_form})
    
    elif number == 3:
        
        return render(request, "Scholarship/scholarship-form2.html", {'form': my_form})
    
    elif number == 4:
        
        return render(request, "Scholarship/scholarship-form3.html", {'form': my_form})

    else:
        
        return Http404()


    


"""
usertype = student
"""
def logout_view(request):
    logout(request)
    
    return redirect('login')

# the dashboard

# to show up all the data
@require_http_methods(["GET"])
def dashboard_view(request):
    
    #if user is not authenticated
    if not(request.user.is_authenticated):

        # redirecte the user to login page
        return redirect('login')
    
    # now if user is authenticated
    my_user = CustomUser.objects.filter(username = request.user.username).first()

    if not my_user:
        # if user not found
        return Http404()

    #if not student
    
    if not(my_user.is_student):
        return HttpResponse("institute user")
    
    # the correct user:

    # aadhar data and marks data

    marks = dummy_data.get_marksheet(aadhar_no=my_user.aadhar_number)
    
    data = dummy_data.get_aadhar(aadhar_no=my_user.aadhar_number)

    
    send_data = {}

    # alligned them correctly
    
    if data:
        send_data['aadhar']: data
    
    for i in marks:
        if i.standard == '1':
            send_data['10'] = i
        else:
            send_data['12'] = i

    caste = dummy_data.get_caste(my_user.aadhar_number)
    domacile = dummy_data.get_domicile(my_user.aadhar_number)
    income = dummy_data.get_income(my_user.aadhar_number)


    send_data['scolar'] = {}

    if caste:
        send_data['scolar']['caste'] = caste

    if domacile:
        send_data['scolar']['domacile'] = domacile
    if income:
        send_data['scolar']['income'] = income


    upload_docs = models.UploadForm.objects.filter(user=my_user)

    send_data['edu'] = []
    send_data['sco'] = []

    for i in upload_docs:
        if i.document_type in ('10th Marksheet', '12th Marksheet', 'Migration', 'Trancerfer Certificate', 'Marksheet', 'GAP Certificate', 'Admission Slip'):
            send_data['edu'].append(i)
            continue

        if i.document_type in ('Domacile', 'Income', 'Caste', 'Samagra', 'Bank Passbook'):
            send_data['sco'].append(i)
            continue

    

    send_data['upload'] = upload_docs
    
    return render(request, 'user_app/eziiii.html', send_data)




# authenticate user 
@require_http_methods(["GET", 'POST'])
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
@require_http_methods(["GET", "POST"])
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
