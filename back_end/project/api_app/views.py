from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main_app.models import CustomUser
from .serial import UserSerial

# Create your views here.

@api_view(['GET'])
def getUserData(request):
    data = CustomUser.objects.all()
    serial = UserSerial(data, many=True)
    return Response(serial.data)

