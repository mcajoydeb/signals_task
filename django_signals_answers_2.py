#django_signals_answers_2.py

Question : Do Django signals run in the same thread as the caller?

Answer : Yes, by default, Django signals run in the same thread that triggered them.


Example :

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def check_thread(sender, instance, **kwargs):
    print("Signal handler thread:", threading.get_ident())



Test :
from django.contrib.auth.models import User
import threading

print("Caller thread:", threading.get_ident())
User.objects.create(username="joydeb")

Output : 

Caller thread: 140557329950464
Signal handler thread: 140557329950464

Both the caller and signal handler print the same id