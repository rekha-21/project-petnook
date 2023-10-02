from django.contrib import admin
from .models import UserProfile,PetCategory,ProductSubcategory,ProductCategory,Product,Wishlist1,Cart
# Register your models here.
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Wishlist1)
admin.site.register(PetCategory)
admin.site.register(ProductSubcategory)
admin.site.register(ProductCategory)
admin.site.register(Cart)