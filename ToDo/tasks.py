from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(user_email, username):
    subject = 'Welcome to Our App!'
    message = f'Hi {username},\n\nThank you for signing up! We are excited to have you on board.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
