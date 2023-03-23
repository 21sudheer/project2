from django.shortcuts import render, redirect
from django.http import HttpResponse
from risers.forms import Empform
from .models import Emp
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def sign_up(request):
    print("hi")
    form=Empform()
    if request.method == "POST":
        form=Empform(request.POST)
        print("errors")
        if form.is_valid():
            form.save()
            return HttpResponse("data inserted")
    return render(request, 'signup.html',{'form':form})


@login_required(login_url="/login")
def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def mylogin(request):
    if request.method=="POST":
        print(request.POST)
        emp = Emp.objects.get(email=request.POST["email"])
        # user = User.objects.filter(email="sudheervarmap1999@gmail.com").last()
        # authenticate(user.email,user.password)
        
        return redirect(request.GET["next"])
        return HttpResponse("hello")
    
    return render(request,template_name="login.html")
    

