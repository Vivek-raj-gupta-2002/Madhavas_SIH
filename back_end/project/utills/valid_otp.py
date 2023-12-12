from main_app import models
from django.conf import Settings
from datetime import datetime

otp_time = 300

def check_otp(username, otp):
    try:
        data = models.OneTimePass.objects.get(aadhar_no=username)
    except:
        data = None

    if data:
        if data.otp == otp:# validate otp

            # print(data.sending_time.strftime('%Y-%m-%d %H:%M:%S'), datetime.now()

            models.OneTimePass.objects.filter(aadhar_no=username).delete()


            return True

    return False
