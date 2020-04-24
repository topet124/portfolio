from django.shortcuts import render
from django.views import View

from django.core.mail import send_mail

# Create your views here.


def home(request):
    if request.method== 'POST':
        message_name= request.POST['message-name']
        message_email=request.POST['message-email']
        message=request.POST['message']

        send_mail(message_name,#subject
                message,#message
                message_email, #from emqil and to email
                ['suletemitope@gmail.com'],
                fail_silently=False,
                )
        return render(request, 'response.html', {'message_name':message_name})
    else:

     return render(request, 'home.html', {})

def response(request):
    return render(request, 'response.html', {})
