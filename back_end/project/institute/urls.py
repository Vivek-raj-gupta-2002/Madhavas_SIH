from django.urls import path
from . import views

urlpatterns = [
    path("scholarForm", views.scholarView, name='institScholarForm'),
    path("internForm", views.internshipView, name='institinternForm'),

]