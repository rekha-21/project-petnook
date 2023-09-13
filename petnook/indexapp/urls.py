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

]