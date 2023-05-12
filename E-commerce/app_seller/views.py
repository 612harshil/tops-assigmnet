from django.shortcuts import render
from app_seller.models import *
from django.conf import settings
from django.core.mail import send_mail
import random
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def indexseller(request):
    return render(request,"indexseller.html")

def register1(request):
    if request.method =="POST":
        try:
            User_seller.objects.get(username=request.POST['email'])
            return render(request,"register1.html",{'msg':"user already exist"})
        except:
            if request.POST['password']==request.POST['cpassword']:
                global votp1
                votp1=random.randint(100000,999999)
                subject = 'otp1 VERIFICATION OF EVIB WEBSITE'
                message = f'Hi your opt is {votp1}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [ request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                global temp
                temp={
                    'fname':request.POST['fname'],
                    'email':request.POST['email'],
                    'pass':make_password(request.POST['password'])
                }
                return render(request,"otp1.html")
            else:
                return render(request,"register1.html",{'msg':"password and confirm password do not match"})    
    else:
        return render(request,"register1.html")
    


def otp1(request):
    if request.method =="POST":
        if votp1==int(request.POST['otp1']):
            User_seller.objects.create(
                fullname=temp['fname'],
                username=temp['email'],
                password=temp['pass']
            )
            return render(request,"login1.html")
        else:
            return render(request,"otp1.html",{'msg':"invalid otp1"})
    else:
        return render(request,"otp1.html")  


def login1(request):
    if request.method=="POST":
        try:
            user_data=User_seller.objects.get(username=request.POST['email'])
            if check_password(request.POST['pass'],user_data.password):
                return render(request,"homepage.html")
            else:
                return render(request,"login1.html",{'msg':"invalid password"})
        except:
               return render(request,"login1.html",{'msg':"user does not exists please register1"}) 
    else:
        return render(request,"login1.html")