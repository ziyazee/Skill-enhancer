from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import CodingSets


app_name='CodeWars'


def title(request):
     data = CodingSets.objects.all()
     return render(request,'codeindex.html',{'data':data})
def description(request,Title):
    Singledata=CodingSets.objects.get(Title=Title)
    print(Singledata)
    return render(request,'codingDescription.html',{'Singledata':Singledata})
