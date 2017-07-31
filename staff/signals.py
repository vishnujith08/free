from django.core.signals import request_finished
from django.db.models.signals import pre_save
from models import User
from django.core.mail import EmailMessage, send_mail
from django.dispatch import Signal, receiver

@receiver(pre_save, sender=User)
def send_email(sender, instance, **kwargs):
    print "ddddddddddd"
    if instance.first_name:
        message = "your profile is cretaed"
        subject = "ethooo... oru vasundaraaa...."
        send_mail(subject, message,
            [instance.email,])
    return sender

