#django_signals_answers_1.py

Question : By default are django signals executed synchronously or asynchronously?

Answer : By default, Django signals are executed synchronously. Caller waits for signal handler to finish before continuing.

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

Output :

Signal handler started
Signal handler finished
Elapsed time: 5.00 seconds

The thread wait for the signal to finish before print the time taken. So it prove that Django signals run synchronously by default.