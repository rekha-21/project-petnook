from django.shortcuts import render,redirect
from .models import Product, UserProfile,Category
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
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        # Update user fields
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        # Update user profile fields
        user_profile.state = request.POST.get('state')
        user_profile.city = request.POST.get('city')
        user_profile.district = request.POST.get('district')
        
        # user_profile.gender = request.POST.get('gender')
        user_profile.phone_number = request.POST.get('phone_number')
        user_profile.addressline1 = request.POST.get('addressline1')
        user_profile.addressline2 = request.POST.get('addressline2')
        user_profile.pin_code = request.POST.get('pin_code')
        
        user_profile.save()

        return redirect('profile') 
    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)

def customerproduct(request):
    stdata = Product.objects.filter(status=False)
    return render(request, "customerproduct.html", {'stdata': stdata})


def displayDog(request):
    return render(request,'displayDog.html')

# def displayCat(request):
#     return render(request,'displayCat.html')

# def displayBird(request):
#     return render(request,'displayBird.html')


def product_list(request):
    # Filter products where the 'category' field is "bed"
    products = Product.objects.filter(category='food')
    
    return render(request, "product_list.html", {'products': products})



def addcategory(request):

    error_message = ''
    add_category = Category.objects.all()

    if request.method == 'POST':
        # Create a new Category instance and assign values
        add_category = Category()
        add_category.pet = request.POST.get('pet')
        add_category.category_name = request.POST.get('category_name')
        add_category.subcategory1 = request.POST.get('subcategory1')
        add_category.subcategory2 = request.POST.get('subcategory2')
        add_category.subcategory3 = request.POST.get('subcategory3')
        add_category.subcategory4 = request.POST.get('subcategory4')
       
        add_category.save()
        
        return redirect("admindashboard")
    
    context = {
        'add_category': add_category
        
        
    }
    return render(request, "addcategory.html", context)


# def delete_category(request, bookid2):
#     remove=category.objects.filter(product_id=bookid2)
#     remove.delete()

def viewcategory(request):
    stdata = Category.objects.all()
    return render(request, "viewcategory.html", {'stdata': stdata})

def updateproduct(request, stid2):
    stid=Product.objects.get(id=stid2)
    stdata = Category.objects.all()
    stid1=Product.objects.filter(id=stid2)
    if request.method == 'POST':
        
        stid.product_name = request.POST.get('product_name')
        stid.brand_name = request.POST.get('brand_name')
        stid.product_description = request.POST.get('product_description')
        stid.material_description = request.POST.get('material_description')
        stid.price = request.POST.get('price')
        stid.quantity = request.POST.get('quantity')
        stid.category = request.POST.get('category')
        stid.subcategory = request.POST.get('subcategory')

        stid.save()
        return redirect("product")

    return render(request, 'updateproduct.html', {'stid1': stid1,'stdata':stdata})

def deleteproduct(request, stid2):
    dele=Product.objects.get(id=stid2)
    dele.status=True
    dele.save()
    return redirect('viewproduct')


def productdescription(request,stid2):
    stid=Product.objects.get(id=stid2)
    stdata = Category.objects.all()
    stid1=Product.objects.filter(id=stid2)
    return render(request,'productdescription.html',{'stid1': stid1,'stdata':stdata})
