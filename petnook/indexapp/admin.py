from django.contrib import admin
from .models import Product,UserProfile,Wishlist,PetCategory,ProductSubcategory,ProductCategory
# Register your models here.
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Wishlist)
admin.site.register(PetCategory)
admin.site.register(ProductSubcategory)
admin.site.register(ProductCategory)