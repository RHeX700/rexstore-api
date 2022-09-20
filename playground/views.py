from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message= EmailMessage('subject', 'message', 'store@store.com', ['boy@store.com'])
        message.attach_file('playground/static/images/truck-kun.jpg')
        message.send()

    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Adekunle'})


