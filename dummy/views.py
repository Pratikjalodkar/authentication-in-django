from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# @login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        return render( request, 'home.html')
    else:
        messages.error(request, "login required!!")
        return redirect('login')

# @login_required(login_url='login')
# def homePage(request):
#     return render(request,'home.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            # email = request.POST.get('email')
            uname = request.POST.get('username')
            pass1 = request.POST.get('password')

            user= authenticate(request,username=uname,password=pass1)
            if user is None:
                return HttpResponse("Invalid Credential!!") 
            else:
                login(request,user)
                print("User authenticated and logged in") 
                return redirect('home')

        return render(request, "login.html")

def logoutPage(request):
    logout(request)
    return redirect('login')


def signupPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            uname = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')

            user=User.objects.filter(username = uname)
            if user.exists():
                messages.info(request, "Username already taken")
                return redirect('signup')

            if(pass1==pass2):
                my_user = User.objects.create_user(uname,email)
                my_user.set_password(pass1) #to encrypt the password
                my_user.save()
                messages.success(request, "Account created successfully")
                return redirect('login')
            else: 
                # return HttpResponse('your password and confirm password are not same')
                messages.error(request, "password and confirm password are not same")
                
    return render(request,'signup.html')