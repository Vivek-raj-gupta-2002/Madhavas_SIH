from django.urls import path
from . import views

urlpatterns = [
    path("scholarForm", views.scholarView, name='institScholarForm'),
    path("internForm", views.internshipView, name='institinternForm'),
    path("api-login", views.api_login_view, name='api_login'),
    path("api-logout", views.logout_api_view, name='api_logout'),
    path("", views.api_dashboard_api, name='api_dashboard'),

    path("getState/<str:type>", views.state_name_view, name='getState'),


]