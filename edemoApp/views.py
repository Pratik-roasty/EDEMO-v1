from django.shortcuts import render,HttpResponse
from edemoApp import fileOperations as fo
# Create your views here.
def home(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def loginCheck(request):
    user=request.POST['ID']
    pas=request.POST['password']
    if user=="Pratik" and pas=="1234":
        val1=1
        return render(request,"welcomePage.html",{"Username":user})
    else:
        return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def addInfo(request):
    Name=request.POST['name']
    Lname=request.POST['lname']
    Gender=request.POST['gender']
    user=request.POST['username']
    pswd1=request.POST['pwd1']
    pswd2=request.POST['pwd2']
    if pswd1==pswd2 and fo.fileRead(user):
        fo.fileWrite([Name,Lname,Gender,user,pswd1])
        return render(request,"login.html")
    else:
        return render(request,"register.html")
