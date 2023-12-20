from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.login_view, name='state_login'),
    path('', views.api_dashboard_api, name='state_dashboard'),
    path("scholarForm/", views.scholarView, name='stateScholarForm'),
    path("NewScholar/", views.new_scholar_view, name='stateRegesterForm'),
]