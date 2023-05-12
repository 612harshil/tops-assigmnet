from django.shortcuts import render
from app_buyer.models import *
from django.conf import settings
from django.core.mail import send_mail
import random
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.


# session_user_data=User.objects.get(email=request.session['email'])

def index(request):
    try:
        request.session['email']
        session_user_data=User.objects.get(email=request.session['email'])
        return render(request,"index.html",{"session_user_data":session_user_data})
    except:
        return render(request,"index.html")



def register(request):
    try:
        request.session['email']
        session_user_data=User.objects.get(username=request.session['email'])
        if request.method =="POST":
            try:
                User.objects.get(username=request.POST['email'])
                return render(request,"register.html",{'msg':"user already exist"})
            except:
                if request.POST['password']==request.POST['cpassword']:
                    global votp
                    votp=random.randint(100000,999999)
                    subject = 'OTP VERIFICATION OF EVIB WEBSITE'
                    message = f'Hi your opt is {votp}'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [ request.POST['email'], ]
                    send_mail( subject, message, email_from, recipient_list )
                    global temp
                    temp={
                        'fname':request.POST['fname'],
                        'email':request.POST['email'],
                        'pass':make_password(request.POST['password'])
                    }
                    return render(request,"otp.html",{"session_user_data":session_user_data})
                else:
                    return render(request,"register.html",
                    {'msg':"password and confirm password do not match"},
                    {"session_user_data":session_user_data})    
        else:
            return render(request,"register.html",{"session_user_data":session_user_data})
    except:
        return render(request,"index.html")
        
def otp(request):
    try:
        request.session['email']
        session_user_data=User.objects.get(email=request.session['email'])
        if request.method =="POST":
            if votp==int(request.POST['otp']):
                User.objects.create(
                    fullname=temp['fname'],
                    username=temp['email'],
                    password=temp['pass']
                )
                return render(request,"login.html",{"session_user_data":session_user_data})
            else:
                return render(request,"otp.html",{'msg':"invalid otp"},
                {"session_user_data":session_user_data})
        else:
            return render(request,"otp.html",{"session_user_data":session_user_data}) 
    except:
        return render(request,"index.html")     




def login(request):
    # try:
    #     request.session['email']
    #     session_user_data=User.objects.get(email=request.session['email'])
        if request.method=="POST":
            try:
                user_data=User.objects.get(username=request.POST['email'])
                if check_password(request.POST['pass'],user_data.password):
                    request.session['email']=request.POST['email']
                    request.session['username']=user_data.fullname 
                    session_user_data=User.objects.get(username=request.session['email'])   
                    return render(request,"homepage.html",{"session_user_data":session_user_data})
                else:
                    return render(request,"login.html",{'msg':"invalid password"},)
            except:
                return render(request,"login.html",{'msg':"user does not exists please register"}) 
        else:
            return render(request,"login.html")
    # except:
    #     return render(request,"index.html")



def profile(request):
    try:
        request.session['email']
        session_user_data=User.objects.get(username=request.session['email'])
        if request.method=="POST":
            user_data=User.objects.get(username=request.session['email'])
            if request.POST['pass']:
                if check_password(request.POST['opass'],user_data.password):
                    if request.POST['pass'] == request.POST['cpass']:
                        user_data=User.objects.get(username=request.session['email'])
                        user_data.fullname=request.POST['fname']
                        user_data.password=make_password(request.POST['pass'])
                        try:
                            request.FILES['propic']
                            user_data.profilepic=request.FILES['propic']
                            user_data.save()
                        except:    
                            user_data.save()
                        return render(request,"profile.html", {"user_data":user_data,
                        "msg":"profile updated successfully","session_user_data":session_user_data})
                    else:
                        user_data=User.objects.get(username=request.session['email'])
                        return render(request,"profile.html",{"user_data":user_data,
                        "msg":"profile updated successfully","session_user_data":session_user_data})
                else:
                    return render(request,"profile.html", {"user_data":user_data,
                    "msg":"old password not match","session_user_data":session_user_data})
                
            else:
                user_data=User.objects.get(username=request.session['email'])
                user_data.fullname=request.POST['fname']
                try:
                    request.FILES['propic']
                    user_data.profilepic=request.FILES['propic']
                    user_data.save()
                except:    
                    user_data.save()
                return render(request,"profile.html", {"user_data":user_data,
                "msg":"password and cpassword not match","session_user_data":session_user_data})
        else:
            user_data=User.objects.get(username=request.session['email'])
            return render(request,"profile.html", {"user_data":user_data,
            "session_user_data":session_user_data})  
    except:
        return render(request,"index.html")

def logout(request):
    try:
        request.session['email']
        del request.session['email']
        return render(request,"index.html")
    except:
        return render(request,"index.html")
