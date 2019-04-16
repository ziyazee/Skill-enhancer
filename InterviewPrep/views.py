from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .models   import *
from MainBoard.models   import *

from .forms import *

def indexip(request):
    return render(request,'InterviewDashboard.html')

def subjectCatgories(request):
    yea=Subject.objects.order_by('subjectName').values('subjectName').distinct()
    # userName=None
    # if request.user.is_authenticated:
        # userName = request.user.username
    # print(userName)

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        userName=None
        if request.user.is_authenticated:
            userName = request.user.username
        if form.is_valid():
            form.save()
            s=Profile.objects.filter(user=request.user)
            points=5
            for i in s:
                i.usersScore+=points
                print(i.usersScore)
                i.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = SubjectForm()
    if request.user.is_authenticated:    
        return render(request,'subjectName.html',{'yea':yea,})
    else:
        return redirect("/")

def topicName(request,subjectName):
    subject=Subject.objects.filter(subjectName=subjectName)
    
    if request.user.is_authenticated:    
        return render(request,'topicName.html',{'subject':subject,'subjectName':subjectName})   
    else:
        return redirect("/")

def topicDescription(request,topicName):
    subject=Subjects.objects.filter(topicName=topicName)
    if request.user.is_authenticated:    
        return render(request,'topicName.html',{'subject':subject})   
    else:
        return redirect("/")



#popularCodingQuestions

def codingTopic(request):
    yea=popularCodingProblem.objects.order_by('topicHeading').values('topicHeading').distinct()
    if request.method == 'POST':
        form = CodingForm(request.POST)
        userName=None
        if request.user.is_authenticated:
            userName = request.user.username
        if form.is_valid():
            form.save()
            s=Profile.objects.filter(user=request.user)
            points=10
            for i in s:
                i.usersScore+=points
                print(i.usersScore)
                i.save()
            return HttpResponseRedirect(request.path_info)
           
    else:
        form = CodingForm()
    if request.user.is_authenticated:    
        return render(request,'codingTopicName.html',{'yea':yea,})
    else:
        return redirect("/")

def codingDescription(request,topicHeading):
    subject=popularCodingProblem.objects.filter(topicHeading=topicHeading)
    if request.user.is_authenticated:    
        return render(request,'codingTopicDescription.html',{'subject':subject,'topicHeading':topicHeading})   
    else:
        return redirect("/")


#aptitude

def aptitudeTopic(request):
    yea=Aptitud.objects.order_by('topicName').values('topicName').distinct()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        userName=None
        if request.user.is_authenticated:
            userName = request.user.username
        if form.is_valid():
            form.save()
            s=Profile.objects.filter(user=request.user)
            points=5
            for i in s:
                i.usersScore+=points
                print(i.usersScore)
                i.save()
            return HttpResponseRedirect(request.path_info)
           
    else:
        form = PostForm()
    
    if request.user.is_authenticated:    
        return render(request,'aptitudeTopic.html',{'yea':yea,})
    else:
        return redirect("/")

def aptitudeDescription(request,topicName):
    subject=Aptitud.objects.filter(topicName=topicName)
    if request.user.is_authenticated:    
        return render(request,'aptitudeDescription.html',{'subject':subject,'topicName':topicName})   
    else:
        return redirect("/")

#interview experience


def interviewTopic(request):
    yea=InterviewExperiences.objects.order_by('companyName').values('companyName').distinct()
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        userName=None
        if request.user.is_authenticated:
            userName = request.user.username
        if form.is_valid():
            form.save()
            s=Profile.objects.filter(user=request.user)
            points=20
            for i in s:
                i.usersScore+=points
                print(i.usersScore)
                i.save()
        
            return HttpResponseRedirect(request.path_info)
           
    else:
        form = InterviewForm()
    if request.user.is_authenticated:    
        return render(request,'companyName.html',{'yea':yea,})
    else:
        return redirect("/")

def companyExperience(request,companyName):
    subject=InterviewExperiences.objects.filter(companyName=companyName)
    if request.user.is_authenticated:    
        return render(request,'companyDescription.html',{'subject':subject,'companyName':companyName})   
    else:
        return redirect("/")


