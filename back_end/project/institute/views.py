from django.shortcuts import render, redirect
from . import models
from . import forms
from main_app.models import CustomUser
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, Http404
from utills import institute_data
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def faq_view(request):

    if not(request.user.is_authenticated):
        return redirect('api_login')  # Redirect to the login page if user is not logged in

    my_user = CustomUser.objects.filter(username=request.user).first()


    if not(my_user.is_institute):
        return redirect('login')

    return render(request, 'institute/faq.html')
    pass

# Institute_level
def institute_lvl_verification(request):

    if not(request.user.is_authenticated):
        return redirect('api_login')  # Redirect to the login page if user is not logged in

    my_user = CustomUser.objects.filter(username=request.user).first()


    if not(my_user.is_institute):
        return redirect('login')

    return render(request, 'institute/institutelvlverification.html')
    pass

csrf_exempt
@require_http_methods(["GET"])
def college_data_api(request, type: str):

    data = None
    if type == 'all':
        data = institute_data.req_data_clg.to_json(orient='records')

    get_data = institute_data.CollegeData()

    for i in get_data.get_unique_state():
        if str(i).lower() == type.lower():
            data = get_data.get_state_data(str(i)).to_json(orient='records')
            break
    
    if not data:
        return Http404()
    
    return JsonResponse({'res': 'success', 'data': data})

csrf_exempt
@require_http_methods(["GET"])
def school_data_api(request, type: str):
    data = ''
    if type == 'all':
        data = institute_data.req_data_school.to_json(orient='records')

    elif type in institute_data.SchoolData().get_unique_state():
        data = institute_data.SchoolData().get_state_data(type).to_json(orient='records') 
    
    else:
        return Http404
    return JsonResponse({'res': 'success', 'data': data})


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










# Internship Form
@require_http_methods(['GET', 'POST'])    
def form_Internship(request):
    
    if not(request.user.is_authenticated):
        return redirect('api_login')  # Redirect to the login page if user is not logged in

    my_user = CustomUser.objects.filter(username=request.user).first()


    if not(my_user.is_institute):
        return redirect('login')
    
    send_data = {}   
    
    my_form = forms.InternForm()

    if request.method == 'POST':
        my_form = forms.InternForm(request.POST, request.FILES)

        # checking if the form follows all the validation
        if my_form.is_valid():
            instance = my_form.save(commit=False)
            
            instance.user = my_user
            instance.is_intern = True
            instance.save()
            return redirect('institinternForm')


    return render(request, 'institute/internships-jobs.html', {'form': my_form})


# Hackathon Form
@require_http_methods(['GET', 'POST'])
def form_Hackathon(request):
    
    if not(request.user.is_authenticated):
        return redirect('api_login')  # Redirect to the login page if user is not logged in

    my_user = CustomUser.objects.filter(username=request.user).first()

    if not(my_user.is_institute):
        return redirect('login')
    
    my_form = forms.Hackathon()

    if request.method == 'POST':
        my_form = forms.Hackathon(request.POST, request.FILES)

        # checking if the form follows all the validation
        print("Atleast running")
        print(my_form.is_valid())

        if my_form.is_valid():
            instance = my_form.save(commit=False)
            instance.user = my_user
            instance.is_hack = True
            instance.save()
            return redirect('institinternForm')

    return render(request, 'institute/hackathons.html', {'form': my_form})