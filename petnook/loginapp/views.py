from django.shortcuts import render,redirect
from .models import CustomUser
from indexapp.models import UserProfile
from django.contrib.auth.models import User,auth
from django.contrib import messages

def landing(request):
    return render(request,'landing.html')
# Create your views here.
def customer_register(request):
    #return render (request,'registration.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        roles=request.POST.get('role',None)
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,"Email is already registered.")
        elif password!=confirm_password:
            messages.error(request,"password not match")
        elif email and password and roles:
            
           
                # return redirect('login')
            user = CustomUser(name=name, email=email) 
            user.set_password(password) 
             
            if roles == 'customer': 
                user.is_customer = True 
            user.save() 

            user_profile=UserProfile(user=user) 
            user_profile.save()

            messages.success(request, "Registered as a customer successfully") 
            return redirect('login')  # Redirect to homepage or thank-you page 
         
        else: 

            messages.error(request, "Missing required fields") 
     
    return render(request, 'registration.html') 


def seller_register(request): 

    if request.method == 'POST':
        name = request.POST.get('name') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        print(name,email,password)
         
        if email and password: 
            print('Entered')

            if CustomUser.objects.filter(email=email).exists(): 
                # messages.error(request, "Email already exists") 
                return redirect('seller_register') 
             
            user = CustomUser(name=name, email=email) 
            user.set_password(password) 
            user.is_seller = True 
            user.save()
           
            messages.success(request, "Registered as a seller successfully") 
            return redirect('login')  # Redirect to homepage or thank-you page 
         
        else: 
            messages.error(request, "Missing required fields") 
     
    return render(request, 'sellerreg.html') 
            
        
    

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user=auth.authenticate(email=email,password=password)
        print(user)
        if user is not None:
            if user.is_customer==True:
                auth.login(request,user)
                print(user.is_customer)
                return redirect('http://127.0.0.1:8000/registration/landing/')
            elif user.is_seller==True:
                auth.login(request,user)
                return redirect('http://127.0.0.1:8000/sellerpage/')
            else:
                auth.login(request,user)
                return redirect('http://127.0.0.1:8000/indexadmin')

    return render (request,'login.html')
def logout(request):
    auth.logout(request)
    if request.user.is_authenticated and request.user.is_seller:
        return redirect('sellerhttp://127.0.0.1:8000/seller/')
    else:
        return redirect('/')

def about(request):
    return render(request,'about.html')