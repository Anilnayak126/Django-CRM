from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import SignUpForm

def home(request):
    #check to see iif loging
    if request.method == "POST":
        username = request.POST['first_name']
        password = request.POST['password']

        # authenticate
        user =authenticate(request,username =username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have been logged in !")
            return redirect('home')
        
        else:
            messages.success(request, "There was an erron Logging In!,Please Try  Again ")
            return redirect('home')

    else:        
         return render(request,'home.html',{})



def logout_user(request):
    logout(request)
    messages.success(request,'You have been Logged Out!')
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            passowrd = form.cleaned_data['password1']
            user = authenticate(username=username,passowrd=passowrd)
            login(request, user)
            messages.success(request,"You have succesfully  registered!")
            return redirect ('home')
        
    else:
        form = SignUpForm()
        return render(request,'register.html',{'forn':form})


       


