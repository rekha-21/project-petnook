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
    path('addproductadmin/',views.addproductadmin,name='addproductadmin'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('profile/',views.profile,name='profile'),
    path('customerproduct/',views.customerproduct,name='customerproduct'),
    path('displayDog/',views.displayDog,name='displayDog'),
    # path('displayCat/',views.displayCat,name='displayCat'),
    #path('displayBird/',views.displayBird,name='displayBird'),

    
    path('product-list/', views.product_list, name='product_list'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('viewcategory/', views.viewcategory, name='viewcategory'),
    path('updateproduct/<int:stid2>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:stid2>/', views.deleteproduct, name='deleteproduct'),
    path('productdescription/<int:stid2>/', views.productdescription, name='productdescription'),

]