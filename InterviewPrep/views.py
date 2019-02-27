from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.



def  indexip(request):
    return render(request,'InterviewDashboard.html')
def mail(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ziyamohd123@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    print("hye")
    return redirect('/InterviewPrep/index')