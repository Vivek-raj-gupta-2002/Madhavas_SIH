from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from main_app.models import CustomUser
from institute import forms
from django.http import HttpResponse
from utills import institute_data
from django.views.decorators.http import require_http_methods


# Scholarship Form
@require_http_methods(['GET', 'POST'])
def scholarView(request):
    
    if not(request.user.is_authenticated):
        return redirect('api_login')  # Redirect to the login page if user is not logged in

    my_user = CustomUser.objects.filter(username=request.user).first()


    if not(my_user.is_state):
        return redirect('login')
    
    send_data = {}

    my_form = forms.ScholarForm()

    if request.method == 'POST':
        my_form = forms.ScholarForm(request.POST, request.FILES)

        # checking if the form follows all the validation
        if my_form.is_valid():
            instance = my_form.save(commit=False)
            instance.user = my_user
            instance.is_scholarship = True
            instance.save()
            return redirect('institScholarForm')

    return render(request, 'state/scholarships.html', {'form': my_form})





def login_view(request):
    
    if(request.user.is_authenticated):
        # redirecte the user to login page
        my_user = CustomUser.objects.filter(username=request.user).first()
        if my_user.is_state:
            return redirect('state_dashboard')
        return redirect('login')

    
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

                    if my_user_special.is_state:
                        
                        login(request, my_user)

                        return redirect('state_dashboard')
    
    send_data['form'] = my_form


    return render(request, 'state/login-api.html', send_data)


@login_required(login_url='state_login')
def api_dashboard_api(request):

    my_user = CustomUser.objects.filter(username=request.user).first()


    if not(my_user.is_state):
        return redirect('login')
    
    send_data = {}

    scl_data = institute_data.SchoolData()

    send_data['state'] = scl_data.get_unique_state()

    
    if 'type' in request.GET:


        if request.GET['type'] == 'school':
            # check for state
            
            formState = request.GET['state']

            send_data['api'] = f'127.0.0.1:8000/institute/api/getScl/{formState}'

        if request.GET['type'] == 'college':
            formState = request.GET['state']

            send_data['api'] = f'127.0.0.1:8000/institute/api/getClg/{formState}'



    return render(request, 'state/eziiii-api.html', send_data)






