from django.urls import path
from . import views

# continuing the url from the mainurls to here
urlpatterns = [

    # the endpoint for sending otp
    path("send_mail/<str:aadhar>", views.send_otp, name='otp'),


    
]