#django_signals_answers_3.py
Question : Do Django signals run in the same database transaction as the caller?

Answer : Yes, by default, Django signals run in the same database transaction as the caller.

Example :

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction
from django.db import models

class Log(models.Model):
    message = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_log(sender, instance, **kwargs):
    Log.objects.create(message=f"Created user: {instance.username}")


Test : 
from django.contrib.auth.models import User
from django.db import transaction
from myapp.models import Log

try:
    with transaction.atomic():
        User.objects.create(username="joydeb")
        raise Exception("Force rollback!")
except:
    pass

print("Logs:", list(Log.objects.values_list("message", flat=True)))

Output :

Logs: []

Even though the signal created a Log, but after rolback logs in printing empty
  
