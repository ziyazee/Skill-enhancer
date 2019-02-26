from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.



def  indexip(request):
    return render(request,'InterviewDashboard.html')