from django.urls import path
from . import views

# continuing the url from the mainurls to here
urlpatterns = [

    # the endpoint for sending otp
    # universal used
    path("send_mail/<str:aadhar>", views.send_otp, name='otp'),
    path("logout", views.logout_view, name='logout'),
    
    # for user_app only
    path("createUser", views.signup, name='signup'),
    path("loginUser", views.login_view, name='login'),
    path("", views.dashboard_view, name='dashboard'),
    path("scholar", views.scholar, name='scholar'),
    path("scholarShip", views.scholarShip, name='scholar'),

]