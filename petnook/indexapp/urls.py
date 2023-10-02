from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from.import views
from django.conf import settings
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    
    path('seller/',views.seller,name='seller'),
    path('sellerpage/',views.sellerpage,name='sellerpage'),
    # path('addproductadmin/',views.addproductadmin,name='addproductadmin'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),

    
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('profile/',views.profile,name='profile'),
    path('customerproduct/',views.customerproduct,name='customerproduct'),
    path('pro/',views.pro,name='pro'),

    path('displayDog/',views.displayDog,name='displayDog'),
    path('displayCat/',views.displayCat,name='displayCat'),
    path('displayBird/',views.displayBird,name='displayBird'),

    
    # path('product-list/', views.product_list, name='product_list'),
    # path('addcategory/', views.addcategory, name='addcategory'),
    # path('viewcategory/', views.viewcategory, name='viewcategory'),
    path('updateproduct/<int:stid2>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:stid2>/', views.deleteproduct, name='deleteproduct'),
    path('productdescription/<int:product_id>/',views.productdescription,name='productdescription'),
    path('wishlist',views.wishlist,name="wishlist"),
    path('add_wishlist/<int:bookid2>/', views.add_wishlist, name='add_wishlist'),
    path('delete_wishlist/<int:bookid2>/', views.delete_wishlist, name='delete_wishlist'),


   
    path('get_product_categories/', views.get_product_categories, name='get_product_categories'),
    path('category_management/', views.category_management, name='category_management'),
    path('getSubcategory/<int:pet_id>', views.getSubcategory, name='getSubcategory'),

    path('add_product/', views.add_product, name='add_product'),

    
    path('indexadmin',views.indexadmin,name='indexadmin'),

    path('add_cart/<int:bookid2>/', views.add_cart, name='add_cart'),


    path('cart/',views.cart,name='cart'),
    path('increase_item/<int:item_id>/', views.increase_item, name='increase_item'),
    path('decrease_item/<int:item_id>/', views.decrease_item, name='decrease_item'),
    path('delete_cart/<int:bookid2>/',views.delete_cart, name='delete_cart'),

]
