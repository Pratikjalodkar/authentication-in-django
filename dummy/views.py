from django.shortcuts import get_object_or_404, redirect, render, HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import InternsForm
from .models import Interns


# @login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        # fm = InternsForm()
        if request.method == 'POST':
            fm=InternsForm(request.POST)
            
            if fm.is_valid():
                fm.save()
                messages.success(request,"Task added Successfully!!")  
                return render(request,'home.html',{'form':fm})
            else:
                fm=InternsForm()
                messages.error(request,"Please out all the task!!")  
                return render(request,'home.html',{'from':fm})

        else:
            fm=InternsForm()
            return render(request,'home.html',{'form':fm})
    else:
        messages.error(request, "login required!!")
        return redirect('login')

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
                messages.error(request,"Invalid Credential!!")
                return redirect('login') 
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

def viewTask(request):
    tasks = Interns.objects.all() 
    return render(request,'viewtask.html',{'tasks':tasks})
    
def delete(request):
    project_name = request.GET.get('project_name')
    if project_name:
        Interns.objects.filter(project_name=project_name).delete()
    return redirect('viewTask')
    
def edit(request, pn):
    if not request.user.is_authenticated:
        return redirect('login')
    ins = get_object_or_404(Interns, pk=pn)
    # ins=Interns.objects.get(project_name=pn)
    if request.method == 'POST':
        fm=InternsForm(request.POST,instance=ins)
        
        if fm.is_valid():
            fm.save()
            messages.success(request,"Task updated Successfully!!")  
            return redirect('viewTask')
    else:
        # ins = Interns.objects.filter(project_name=pn).values()
        fm=InternsForm(instance=ins)
        return render(request,'editTask.html',{'form':fm})


