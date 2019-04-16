from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from InterviewPrep.models import *
from FileManager.models import *

from .models import *

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("/indi/")
    else:
        form=AuthenticationForm()
    return render(request,'login.html', {'form': form})
def logout_view(request):

    if request.method=='POST':
        print("hello")
        logout(request)
        return redirect('/')
def tk(request):
    pass
def  profile(request,username):
    print(username)
    s=Profile.objects.filter(user=request.user)
    
    score=0
    for i in s:
        score=i.usersScore
    aptitude=Aptitud.objects.filter(userName=username)
    popularCodingProblems=popularCodingProblem.objects.filter(userName=username)
    InterviewExperience=InterviewExperiences.objects.filter(userName=username)
    subject=Subject.objects.filter(userName=username)
    files=filest.objects.filter(usn=username)
    return render(request,'profile.html',{'score':score,'aptitude':aptitude,'popularCodingProblems':popularCodingProblems,'InterviewExperience':InterviewExperience,'subject':subject,'files':files})


def  indi(request):
    if request.user.is_authenticated:
        return render(request,'indi.html')
    else:
        return redirect("/")


def rank(request):
    res=Profile.objects.all().order_by('-usersScore')
    print(res)
    return render(request,'ranklist.html',{'res':res})