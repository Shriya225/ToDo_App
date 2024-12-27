from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from ToDo.forms import loginForm,signupForm
# Create your views here.
def home(request):
    return render(request,'Base.html',{"username":request.user.username})

def user_login(req):
    if req.method =="POST":
        form=loginForm(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            pwd=form.cleaned_data['pwd']
            user=authenticate(username=name,password=pwd)
            if user:
                login(req,user)
                return redirect("/ToDo/")
            else:
                return HttpResponse("invalid user!!")
        else:
            print("invalid data")
    else:
        form=loginForm()
    return render(req,"login.html",{"form":form})



def user_logout(request):
    logout(request)
    return redirect("home")

def signup(request):
    if request.method=="POST":
        form=signupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("/ToDo/")
        else:
            print("invalid")
    else:
        form=signupForm()
    return render(request,"signup.html",{"form":form})
