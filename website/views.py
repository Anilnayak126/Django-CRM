from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Record
from .form import SignUpForm

#adding comments
def home(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Use .get() to avoid KeyError
        password = request.POST.get('password')  # Use .get() to avoid KeyError

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in!")
                return redirect('home')
            else:
                 messages.error(request, "There was an error logging in. Please try again.")
                 return redirect('/')

        else:
            messages.error(request,"user not found !!")
            return redirect('/')
            
          
    else:
        return render(request, 'home.html', {})
      

def logout_user(request):
    logout(request)
    messages.success(request,'You have been Logged Out!')
    return redirect('home')


def register_user(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('repassword')
        
        print(username,email,password1,first_name,second_name)
        if password1 == password2:
            user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=second_name)
            user.save()
            messages.success(request,"user id created successfully !!")
            return redirect('home')
        else:
            messages.error(request,"password didnt match")

    
    return render(request, 'register.html')


def Records_view(request):
    

    if request.user.is_authenticated:
        users_record = Record.objects.all()


    return render(request,'records.html',{"records" : users_record})


def manage_Records(request):

    if request.user.is_authenticated: 
         users_record = Record.objects.all()


    return render(request, 'm_records.html',{"records" : users_record})



def view_person(request,pk):
     
     print(pk)
     
     user = Record.objects.get(id=pk)
    

     return render(request, "viewRecords.html",{"user_details":user})



def add_records(request): 

    if request.method == "POST":
      firstName = request.POST.get("firstName")
      lastname = request.POST.get("lastname")
      email = request.POST.get("email")
      Phone = request.POST.get("phone")
      adress = request.POST.get("adress")
      City = request.POST.get("city")
      state = request.POST.get("state")
      zip_code = request.POST.get("zip_code")

      if request.user.is_authenticated:
          
          create_record = Record(first_name=firstName,
                                 last_name=lastname,email=email,
                                 phone=Phone,address=adress,
                                 city = City , state= state ,
                                 zipcode= zip_code)
          
          create_record.save()
          messages.success(request, "Record updated ..")
          return redirect("records")
        
    return render(request, "addRecords.html")

def delete_records(request,pk):

    if request.user.is_authenticated: 
         users_record = Record.objects.all()
         users_record_delete = Record.objects.get(id=pk)

         users_record_delete.delete()
         messages.success(request,"successfully deleted the record..")
    
    return render(request, 'records.html',{"records" : users_record})

def edit_records(request, pk):
    user_record = Record.objects.get(id=pk)

    if request.method == "POST":
        user_record.first_name = request.POST.get("firstName")
        user_record.last_name = request.POST.get("lastname")
        user_record.email = request.POST.get("email")
        user_record.phone = request.POST.get("phone")
        user_record.address = request.POST.get("adress")
        user_record.city = request.POST.get("city")
        user_record.state = request.POST.get("state")
        user_record.zipcode = request.POST.get("zip_code")

        if request.user.is_authenticated:
            user_record.save() 
            messages.success(request, "Record updated!")
            return redirect("manage_records")
    
    return render(request, "edit_records.html", {"user_record": user_record})



       


