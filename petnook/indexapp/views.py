from django.shortcuts import render,redirect
from .models import Product, UserProfile
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def seller(request):
    return render(request,'seller.html')
def sellerpage(request):
    return render(request,'sellerpage.html')



def addproductadmin(request):
    user = request.user
    userid = user.id
    if request.method == 'POST':
        # Create a new Category instance and assign values
        newproduct = Product(
        product_name = request.POST.get('product_name'),
        product_description = request.POST.get('product_description'),
        price = request.POST.get('price'),
        product_images1 = request.FILES.get('product_images1'),
        product_images2 = request.FILES.get('product_images2'),
        product_images3 = request.FILES.get('product_images3'),
        category = request.POST.get('category'),
        brand_name = request.POST.get('brand_name'),
        sizeQuantity = request.POST.get('sizeQuantity'),
        petCompatibility = request.POST.get('petCompatibility'),
        agesizesuitability = request.POST.get('agesizesuitability'),
        colorsVariations = request.POST.get('colorsVariations'),
        user_id=userid
        )
        newproduct.save()   
        
        return redirect("viewproduct")
    return render(request, "addproductadmin.html")




def admindashboard(request):
    return render(request,'admindashboard.html')
def viewproduct(request):
    stdata = Product.objects.filter(status=False)
    return render(request, "viewproduct.html", {'stdata': stdata})

def profile(request):
    # user = request.user
    # user_profile = UserProfile.objects.get(user=user)
    # if request.method == 'POST':
    #     # Update user fields
    #     user.first_name = request.POST.get('first_name')
    #     user.last_name = request.POST.get('last_name')
    #     user.save()

    #     # Update user profile fields
    #     user_profile.state = request.POST.get('state')
    #     user_profile.city = request.POST.get('city')
    #     user_profile.district = request.POST.get('district')
        
    #     # user_profile.gender = request.POST.get('gender')
    #     user_profile.phone_no = request.POST.get('phone_no')
    #     user_profile.addressline1 = request.POST.get('addressline1')
    #     user_profile.addressline2 = request.POST.get('addressline2')
    #     user_profile.pin_code = request.POST.get('pin_code')
        
    #     user_profile.save()

    #     return redirect('profile') 
    # context = {
    #     'user': user,
    #     'user_profile': user_profile
    # }, context
    return render(request, 'profile.html')

def customerproduct(request):
    stdata = Product.objects.filter(status=False)
    return render(request, "customerproduct.html", {'stdata': stdata})
