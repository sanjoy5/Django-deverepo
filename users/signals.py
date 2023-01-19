from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from .models import *
from django.core.mail import send_mail
from django.conf import settings



def createProfile(sender,instance,created,**kwargs):
    # print("Signals Triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = 'Welcome to DevRepo World'
        message = 'We are glad you are here! Thanks for chooseing our site. We are happy to see you there. Best of luck and always stay with us.'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

def updateUser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteProfile(sender,instance,**kwargs):
    user = instance.user
    user.delete()
    # print('Profile Deleted Successfully')

post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteProfile,sender=Profile)