from django.shortcuts import render, redirect
from . import models
from . import forms
from main_app.models import CustomUser
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


# Create your views here.

def api_dashboard_api(request):
    
    if not(request.user.is_authenticated):
        return redirect('api-login')  # Redirect to the login page if user is not logged in

    my_user = CustomUser.objects.filter(username=request.user).first()


    if not(my_user.is_institute):
        return redirect('login')
    

    return render(request, 'institute/eziiii-api.html')

# login view for apis
@require_http_methods(['GET', 'POST'])
def api_login_view(request):
    
    if(request.user.is_authenticated):
        # redirecte the user to login page
        return redirect('api_dashboard')

    
    my_form = forms.ApiLoginForm()

    send_data = {}

    if request.method == 'POST':
        my_form = forms.ApiLoginForm(request.POST)

        if my_form.is_valid():
            
            username = my_form['username'].value()
            phone = my_form['phone_number'].value()
            pin = my_form['password'].value()
            
            # returns username if authenticated
            my_user = authenticate(request, username=username, password=pin)


            if my_user:
                 
                my_user_special = CustomUser.objects.filter(username=my_user).first()

                if my_user_special.phone_number == phone:

                    if my_user_special.is_institute:
                        
                        login(request, my_user)

                        return redirect('api_dashboard')
    
    send_data['form'] = my_form


    return render(request, 'institute/login-api.html', send_data)
    

@require_http_methods(["GET"])
def logout_api_view(request):
    logout(request)
    
    return redirect('api_login')



def internshipView(requests):
    my_form = forms.InternForm()

    return render(requests, 'institute/internships-jobs.html', {'form': my_form})



def scholarView(requests):
    my_form = forms.ScholarForm()

    return render(requests, 'institute/scholarships.html', {'form': my_form})

def hackView(requests):
    my_form = forms.Hackathon()

    return render(requests, 'institute/hackathons.html', {'form': my_form})
