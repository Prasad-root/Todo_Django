from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/Dashboard')
        else:
            messages.error(request,"Invalid Username Password...")
            return redirect("/")
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        try:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            conformPassword = request.POST['conformpassword']

            username_check = User.objects.filter(username = email).exists()
            password_check = (password == conformPassword)

            if not username_check and password_check:
                user = User.objects.create_user(first_name = firstname,last_name = lastname,email = email,username = email,password = password)
                user.save()
                return redirect('/')
            elif username_check:
                messages.error(request,"Username Already Taken")
                return redirect('/register')

            elif not password_check:
                messages.error(request,"Password and Conform Password Not Equal")
                return redirect("/register")

            else:
                messages.error(request,"Somthing Wrong Try again!")
                return redirect("/register")
        except Exception as error_message:
            messages.error(request,error_message)
            return redirect("/register")
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
