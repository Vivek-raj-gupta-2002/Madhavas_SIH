from django.urls import path
from . import views

urlpatterns = [
    # path("scholarForm", views.scholarView, name='institScholarForm'),
    # path("internForm", views.form_Internship, name='institinternForm'),
    path("api-login", views.api_login_view, name='api_login'),
    path("api-logout", views.logout_api_view, name='api_logout'),
    # path("", views.api_dashboard_api, name='api_dashboard'),
    # path("hackathonForm", views.form_Hackathon, name='instithackathonForm'), 

    path("api/getClg/<str:type>", views.college_data_api, name='college_data'),
    path("api/getScl/<str:type>", views.school_data_api, name='school_data'),
    path("faq", views.faq_view, name='institute_faq'),

]