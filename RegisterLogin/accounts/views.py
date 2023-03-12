from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('login')


def index(request):
    return render(request,'index.html')



def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request,"Wrong credentials")
            return render(request,'login.html')
    else:
        return render(request,'login.html')



def Register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username already taken")

            if User.objects.filter(email = email).exists():
                messages.error(request,"Email already exist")

            else:
                user = User.objects.create(username = username , first_name = fname , last_name = lname , email = email , password = pass1)
                user.save()
                if user is not None:
                    auth.login(request,user)
                    # return HttpResponse(" Registered Sucessfully and Logged in ! ")
                    return render(request,'index.html')


        else:
            messages.error(request,"Both Password are not Matching")
    else:
        return render(request,'login.html')
