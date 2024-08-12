from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from . tasks import sleeptime, send_email_task

def index(request):
    # sleeptime(15) # fifteen seconds
    # sleeptime.delay(15) # .delay() invocate celery
    send_email_task.delay()
    # return HttpResponse('Hello, world')
    return HttpResponse('The email was sent successfully!')