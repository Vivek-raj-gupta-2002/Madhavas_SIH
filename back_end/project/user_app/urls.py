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
    path("faq", views.FAQ, name='faq'),
    path("opportunity", views.oportunity_view, name='opportunities'),
    path("issued_doc", views.issued_view, name='issuedDocs'),
    path("scolar", views.scholar_view, name='scolar'),

    path("scolarShip/<int:number>", views.scholarShip, name='scolarShip'),
    

]