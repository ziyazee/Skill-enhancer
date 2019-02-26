from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
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

def  tk(request):
    return render(request,'tk.html')


def  indi(request):
    if request.user.is_authenticated:
        return render(request,'indi.html')
    else:
        return redirect("/")
