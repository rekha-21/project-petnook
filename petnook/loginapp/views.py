from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def customer_register(request):
    #return render (request,'registration.html')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        roles=request.POST.get('role',None)

        if email and password and roles:
            
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request,"Email is already registered.")
                return redirect('login')
            user = CustomUser(name=name, email=email) 
            user.set_password(password) 
             
            if roles == 'customer': 
                user.is_customer = True 
            user.save() 
            messages.success(request, "Registered as a customer successfully") 
            return redirect('/')  # Redirect to homepage or thank-you page 
         
        else: 

            messages.error(request, "Missing required fields") 
     
    return render(request, 'registration.html') 


def seller_register(request): 
    if request.method == 'POST': 
        name = request.POST.get('name') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        roles = request.POST.get('role', None) 
         
        if email and password and roles: 
            if CustomUser.objects.filter(email=email).exists(): 
                messages.error(request, "Email already exists") 
                return redirect('seller_register') 
             
            user = CustomUser(name=name, email=email) 
            user.set_password(password) 
             
            if roles == 'seller': 
                user.is_seller = True 
            user.save() 
            messages.success(request, "Registered as a seller successfully") 
            return redirect('/')  # Redirect to homepage or thank-you page 
         
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
            auth.login(request,user)
            return redirect('/')
    return render (request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
