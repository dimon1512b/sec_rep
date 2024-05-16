"""
- what is django signals? tool for communicate between apps
- what is default signals?
- what is inbuilt signals in drf?
- how to create custom signal?
- how to use it?

Django signals are a core feature of the Django framework that enable certain
senders to notify a set of receivers when specific actions occur
elsewhere in the application.

DEFAULT SIGNALS IS:
For example, when you save an instance of a Django model using its save()
method, the pre_save and post_save signals are automatically sent before and
after the save operation, respectively. Similarly, when you delete a model
instance using its delete() method, the pre_delete and post_delete signals are
triggered before and after the delete operation.

INBUILT SIGNALS USING:
from django.db.models.signals import post_save
from rest_framework.signals import request_started
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework import serializers

# Define receiver function for DRF signal
@receiver(request_started)
def request_started_handler(sender, **kwargs):
    # Custom logic to be executed when a request is started
    print("Request started:", sender)

# Define receiver function for Django signal
@receiver(post_save, sender=User)
def user_post_save_handler(sender, instance, created, **kwargs):
    # Custom logic to be executed after a User object is saved
    if created:
        print("New user created:", instance.username)
    else:
        print("User updated:", instance.username)

# Connect receivers to signals
request_started.connect(request_started_handler)
post_save.connect(user_post_save_handler)

CREATE AND USE CUSTOM SIGNAL:
from django.dispatch import Signal

# Define the custom signal
my_signal = Signal()

# Define receiver function for the custom signal
def my_signal_receiver(sender, **kwargs):
    # Custom logic to be executed when the signal is sent
    print("Custom signal received!")

# Connect receiver function to the custom signal
my_signal.connect(my_signal_receiver)

# Somewhere in your code, send the custom signal
my_signal.send(sender=None)


"""