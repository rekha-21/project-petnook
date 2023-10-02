from django.shortcuts import get_object_or_404, render,redirect
from .models import  UserProfile,PetCategory, ProductCategory, ProductSubcategory,Product,Wishlist1,Cart
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseNotFound, JsonResponse
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
def admindashboard(request):
    return render(request,'admindashboard.html')

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
    display = Product.objects.all()
    user_wishlist = Wishlist1.objects.filter(user=request.user)
    user_wishlist_ids = [item.product.id for item in user_wishlist]
    context = {
        'display': display,
        'user_wishlist_ids': user_wishlist_ids,
       
       
    }
    return render(request, 'customerproduct.html',context)


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








def updateproduct(request, stid2):
    print(stid2)
    stid=Product.objects.get(id=stid2)
    
    stid1=Product.objects.filter(id=stid2)
    if request.method == 'POST':
        
        stid.name = request.POST.get('productName')
        stid.brand_name = request.POST.get('brandName')
        stid.description = request.POST.get('productDescription')
        stid.num_items = request.POST.get('numItems')
 
        stid.price = request.POST.get('price')
        stid.quantity = request.POST.get('quantityValue')
 
        stid.save()
        return redirect("viewproduct")

    return render(request, 'updateproduct.html', {'stid1': stid1})

def deleteproduct(request, stid2):
    dele=Product.objects.get(id=stid2)
    dele.m=False
    dele.save()
    return redirect('viewproduct')


def productdescription(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_cart = Cart.objects.filter(user=request.user)
    user_cart_ids = [item.product.id for item in user_cart]
    return render(request, 'productdescription.html', {'product': product,'user_cart_ids': user_cart_ids})





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
    categories1 = ProductSubcategory.objects.all()


    context = {
        'pet_categories': pet_categories,
        'product_categories': product_categories,
        'categories1':categories1,
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
        unit = request.POST.get('unit')
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
            unit=unit,
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

def viewproduct(request):
    display = Product.objects.filter(m=True)
    context = {
        'display': display,
       
    }
    return render(request, 'viewproduct.html',context)

def wishlist(request):
    
    # Assuming you have the user object for the currently logged-in user
    user_id = request.user.id  # Replace with your user retrieval logic if needed
# Retrieve books in the user's cart
    books_in_cart = Wishlist1.objects.filter(user_id=user_id)
# Retrieve book details for the books in the cart
    book_details = Product.objects.filter(id__in=books_in_cart.values_list('product_id', flat=True))
    return render(request,"wishlist.html",{'display':book_details})

def add_wishlist(request, bookid2):
    userid=request.user.id
    book = Wishlist1(
        user_id=userid,
        product_id=bookid2        
    )
    book.save()
    return redirect('wishlist')
def delete_wishlist(request, bookid2):
    remove=Wishlist1.objects.filter(product_id=bookid2)
    remove.delete()
    return redirect('wishlist')

def indexadmin(request):
    return render(request,'admin1/indexadmin.html')

def add_cart(request, bookid2):
    try:
        # Ensure that bookid2 is a valid integer
        bookid2 = int(bookid2)

        # Create a BookCart object (assuming your model fields match)
        userid = request.user.id
        book = Cart(
            user_id=userid,
            product_id=bookid2
        )
        book.save()
        bookid=bookid2

        # Redirect to 'singleview' with the 'bookid' parameter
        return redirect('productdescription',bookid)
    except ValueError:
        # Handle the case where bookid2 is not a valid integer
        return HttpResponseNotFound("Invalid book ID")
        

def cart(request):
    # Assuming you have the user object for the currently logged-in user
    user_id = request.user.id  # Replace with your user retrieval logic if needed
# Retrieve books in the user's cart
    books_in_cart = Cart.objects.filter(user_id=user_id)
# Retrieve book details for the books in the cart
    book_details = Product.objects.filter(id__in=books_in_cart.values_list('product_id', flat=True))
    print(book_details)
    print("hai")
    total_price = sum(books_in_cart.product.price * books_in_cart.quantity for books_in_cart in books_in_cart)

    #product_id=BookCart.request.get(product_id=product_id)
    st = Cart.objects.filter(user_id=user_id)
    return render(request,"cart.html",{'cart_books':book_details,'st':st,'total_price':total_price})


def decrease_item(request, item_id): 
    try: 
        print(item_id)
        cart_item = Cart.objects.get(product_id=item_id) 
        print(cart_item.product)
        print(cart_item.quantity)
        cart_item.quantity = str(int(cart_item.quantity)-1)
        print(cart_item.quantity)
        cart_item.save() 
    except Cart.DoesNotExist: 
        pass  # Handle the case when the item does not exist in the cart 
    return redirect('cart')

def increase_item(request, item_id): 
    try: 
        print(item_id)
        cart_item = Cart.objects.get(product_id=item_id) 
        print(cart_item.product)
        print(cart_item.quantity)
        cart_item.quantity = str(int(cart_item.quantity) + 1)
        print(cart_item.quantity) 
        cart_item.save() 
    except Cart.DoesNotExist: 
        pass  # Handle the case when the item does not exist in the cart 
    return redirect('cart')

def delete_cart(request, bookid2):
    remove=Cart.objects.filter(product_id=bookid2)
    remove.delete()
    return redirect('cart')


def pro(request):
    display = Product.objects.all()
    user_wishlist = Wishlist1.objects.filter(user=request.user)
    user_wishlist_ids = [item.product.id for item in user_wishlist]
    context = {
        'display': display,
        'user_wishlist_ids': user_wishlist_ids,
       
       
    }
    return render(request, 'pro.html',context)