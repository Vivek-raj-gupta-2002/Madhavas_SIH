from django.core.mail import send_mail
from django.conf import settings


def send_email_to_client(subject, message, *recipient_list):
    from_email =settings.EMAIL_HOST_USER
    
    send_mail(subject, message, from_email, list(recipient_list))