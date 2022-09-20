from .tasks import notify_customers
from django.shortcuts import render


def say_hello(request):
    notify_customers.delay('Yo, you good?')
    return render(request, 'hello.html', {'name': 'Adekunle'})


