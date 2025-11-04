#django_signals_answers_1.py

Question : By default are django signals executed synchronously or asynchronously? - the caller waits for signal handler to finish before continuing.

Answer : By default, Django signals are executed synchronously.

Example :

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)
    print("Signal handler finished")



Test 

from django.contrib.auth.models import User
import time

start = time.time()
User.objects.create(username="joydeb")  # Triggers post_save
end = time.time()
print("Elapsed time", end - start)

The thread wait for the signal to finish before print the time taken. So it prove that Django signals run synchronously by default.