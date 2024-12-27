from django.db.models.signals import Signal,pre_save,post_save
from django.dispatch import receiver
from .models import Task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .tasks import send_welcome_email


# task_done=Signal()

# @receiver(task_done)
# def task_done_handler(sender, message, user, form,**kwargs):
#     print(f"Task completed for user {user.username}. Sending email...")
#     capitalized_description = form.cleaned_data['description'].capitalize()
#     print(f"Capitalized Description: {capitalized_description}")
#     form.instance.description = capitalized_description 

@receiver(pre_save,sender=Task)
def pre_save_handler(instance,**kwargs):
    instance.title=instance.title.upper()

@receiver(post_save,sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # Only send email for new user creation
       send_welcome_email.delay(instance.email, instance.username)

    





