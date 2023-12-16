from rest_framework import serializers
from main_app.models import CustomUser


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'aadhar_number', 'email', 
                  'Name', 'gender', 'dob', 'institute', 'caste',
                  ]

