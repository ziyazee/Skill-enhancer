from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import clasyear
from .models import filest
from .forms import PostForm


def home(request):
    yea=clasyear.objects.order_by('year').values('year').distinct()
    if request.user.is_authenticated:    
        return render(request,'home.html',{'yea':yea,})
    else:
        return redirect("/")

def index(request):
    return render(request,'index.html')

def testing(request):
    return render(request,'testing.html')    


def details(request,name):
    detail=clasyear.objects.filter(name=name)

    contentValue = {'detail':detail}
    if request.user.is_authenticated:    
        return render(request,'details.html',contentValue)
    else:
        return redirect("/")


def subjects(request,year):
    subject=clasyear.objects.filter(year=year)
    if request.user.is_authenticated:    
        return render(request,'subjects.html',{'subject':subject})   
    else:
        return redirect("/")

def files(request,categorie):
    print(categorie)
    usn = None
    if request.user.is_authenticated:
        usn = request.user.username
    file=filest.objects.filter(categorie=categorie).order_by('fname')
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
           
    else:
        form = PostForm( initial = {'categorie':categorie,'usn':usn})
    if request.user.is_authenticated:    
        return render(request,'files.html',{'file':file,'form':form})   
    else:
        return redirect("/")


  

