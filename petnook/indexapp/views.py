from django.shortcuts import get_object_or_404, render,redirect
from .models import  UserProfile,PetCategory, ProductCategory, ProductSubcategory,Product
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def seller(request):
    return render(request,'seller.html')
def sellerpage(request):
    return render(request,'sellerpage.html')



# def addproductadmin(request):
    # user = request.user
    # userid = user.id
    # stdata = Category.objects.all()
    # if request.method == 'POST':
    #     # Create a new Category instance and assign values
    #     newproduct = Product(
    #     product_name = request.POST.get('product_name'),
    #     product_description = request.POST.get('product_description'),
    #     price = request.POST.get('price'),
    #     product_images1 = request.FILES.get('product_images1'),
    #     product_images2 = request.FILES.get('product_images2'),
    #     product_images3 = request.FILES.get('product_images3'),
    #     category = request.POST.get('category'),
    #     brand_name = request.POST.get('brand_name'),
    #     sizeQuantity = request.POST.get('sizeQuantity'),
    #     petCompatibility = request.POST.get('petCompatibility'),
    #     agesizesuitability = request.POST.get('agesizesuitability'),
    #     colorsVariations = request.POST.get('colorsVariations'),
    #     user_id=userid
    #     )
    #     newproduct.save()   
        
    #     return redirect("viewproduct")
    # return render(request, "addproductadmin.html")




def admindashboard(request):
    return render(request,'admindashboard.html')
# def viewproduct(request):
#     stdata = Product.objects.filter(status=False)
#     return render(request, "viewproduct.html", {'stdata': stdata})

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
        user_profile.pincode = request.POST.get('pincode')
        
        user_profile.save()

        return redirect('profile') 
    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)

def customerproduct(request):
    # stdata = Product.objects.filter(status=False)
    return render(request, "customerproduct.html")


def displayDog(request):
    return render(request,'displayDog.html')

def displayCat(request):
    return render(request,'displayCat.html')

def displayBird(request):
    return render(request,'displayBird.html')


# def product_list(request):
#     # Filter products where the 'category' field is "bed"
#     products = Product.objects.filter(category='food')
    
#     return render(request, "product_list.html", {'products': products})








# def updateproduct(request, stid2):
#     print(stid2)
#     stid=Product.objects.get(id=stid2)
#     stdata = Category.objects.all()
#     stid1=Product.objects.filter(id=stid2)
#     if request.method == 'POST':
        
#         stid.product_name = request.POST.get('product_name')
#         stid.brand_name = request.POST.get('brand_name')
#         stid.product_description = request.POST.get('product_description')
#         stid.material_description = request.POST.get('material_description')
#         stid.price = request.POST.get('price')
#         stid.quantity = request.POST.get('quantity')
#         stid.category = request.POST.get('category')
#         stid.subcategory = request.POST.get('subcategory')

#         stid.save()
#         return redirect("viewproduct")

#     return render(request, 'updateproduct.html', {'stid1': stid1,'stdata':stdata})

# def deleteproduct(request, stid2):
#     dele=Product.objects.get(id=stid2)
#     dele.status=True
#     dele.save()
#     return redirect('viewproduct')


# def productdescription(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'productdescription.html', {'product': product})


# def wishlist(request):
#     # Get the user's wishlist or create one if it doesn't exist
#     wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    
#     # Retrieve the products in the user's wishlist
#     wishlist_products = wishlist.products.all()
    
#     context = {
#         'wishlist_products': wishlist_products,
#     }
    
#     return render(request, 'wishlist.html', context)


# def add_to_wishlist(request, product_id):
#     if request.user.is_authenticated:
#         product = get_object_or_404(Product, pk=product_id)
#         user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
#         user_wishlist.products.add(product)
#         return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False})
    

# def remove_from_wishlist(request, product_id):
#     if request.user.is_authenticated:
#         product = get_object_or_404(Product, pk=product_id)
#         user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
#         user_wishlist.products.remove(product)
#         return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False})
    


def get_product_categories(request):
    # Get the pet_type_id from the query parameters
    pet_type_id = request.GET.get('pet_type_id')

    # Fetch product categories based on the pet_type_id
    product_categories = ProductCategory.objects.filter(pet_category_id=pet_type_id)

    # Create a list of product category names
    category_names = [category.category for category in product_categories]

    # Return the category names as JSON data
    return JsonResponse({'product_categories': category_names})

def category_management(request):
    if request.method == 'POST':
        pet_type = request.POST.get('petType')
        selected_product_category_name = request.POST.get('subcategory')
        new_subcategory = request.POST.get('addSubcategory')
        print(pet_type)
        print(selected_product_category_name)
        print(new_subcategory)

        if pet_type and selected_product_category_name:
            # Get the selected pet category
            pet_category = PetCategory.objects.get(id=pet_type)

            # Get the selected product category based on its name
            selected_product_category = ProductCategory.objects.get(id=selected_product_category_name)

            # Create a new ProductSubcategory
            ProductSubcategory.objects.create(
                pet_category=pet_category,
                product_category=selected_product_category,
                sub_category=new_subcategory
            )

    # Fetch the list of pet categories and product categories for the template
    pet_categories = PetCategory.objects.all()
    product_categories = ProductCategory.objects.all()

    context = {
        'pet_categories': pet_categories,
        'product_categories': product_categories,
    }

    return render(request, 'categoryadmin.html', context)

from django.core import serializers
def getSubcategory(request,pet_id):
    print(pet_id)
    data=ProductCategory.objects.filter(pet_category_id=pet_id)
    print(data)
    data=serializers.serialize('json',data)
    return JsonResponse({'data':data})



def add_product(request):
    # Fetch pet categories from the database
    pet_categories = PetCategory.objects.all()
    # Fetch product categories from the database
    product_categories = ProductCategory.objects.all()
    # Fetch product subcategories from the database
    product_subcategories = ProductSubcategory.objects.all()


    category_name=request.POST.get('category')
    print("cat",category_name)
    
    sub=request.POST.get('productSubcategory')
    print(sub)
    
    type=request.POST.get('petType')
    print(type)
    

    if request.method == 'POST':
        # Get the form data submitted by the user
        
        name = request.POST.get('productName')
        description = request.POST.get('productDescription')
        brand_name = request.POST.get('brandName')
        num_items = request.POST.get('numItems')
        quantity_value = request.POST.get('quantityValue')
        price = request.POST.get('price')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')

        # Create a new product instance and save it to the database
        product = Product(
            pet_type_id=type,
            product_category_id=category_name,
            product_subcategory_id=sub,
            name=name,
            description=description,
            brand_name=brand_name,
            num_items=num_items,
            quantity_value=quantity_value,
            price=price,
            image1 = image1,
            image2 = image2,
            image3 = image3,
        )
        product.save()

        # Redirect to a success page or perform other actions as needed
        return redirect('landing')  # Change to your success URL

    context = {
        'pet_categories': pet_categories,
        'product_categories': product_categories,
        'product_subcategories': product_subcategories,
    }

    return render(request, 'addproductadmin.html', context)