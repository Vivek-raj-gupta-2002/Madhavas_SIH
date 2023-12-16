from django.shortcuts import render, redirect
from . import models
from . import forms
from main_app.models import CustomUser
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, Http404
from utills import institute_data



# Create your views here.

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
    
    return JsonResponse(data)



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


def api_dashboard_api(request):
    
    if not(request.user.is_authenticated):
        return redirect('api-login')  # Redirect to the login page if user is not logged in

    my_user = CustomUser.objects.filter(username=request.user).first()


    if not(my_user.is_institute):
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



    return render(request, 'institute/eziiii-api.html', send_data)

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
