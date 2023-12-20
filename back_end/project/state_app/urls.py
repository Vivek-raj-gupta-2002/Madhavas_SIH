from django.urls import path
from . import views


urlpatterns = [

    path('login/', views.login_view, name='state_login'),
    path('', views.api_dashboard_api, name='state_dashboard'),
    path("scholarForm/", views.scholarView, name='stateScholarForm'),
<<<<<<< HEAD
    path("NewScholar/", views.new_scholar_view, name='stateScholarForm'),
=======
    path("ScholarGen/", views.scholarRegisterView, name='ScholarRegisterForm'),
>>>>>>> a73e315c560f26b5310bbed027d08e4f59bc6f62

]