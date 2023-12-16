from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path("userData/", views.api_view)
]

urlpatterns = format_suffix_patterns(urlpatterns)
