from django.db import models
from loginapp.models import CustomUser
class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=255, null=True)
    product_description = models.TextField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    product_images1 = models.FileField(upload_to='sample/', null=True, blank=True, max_length=255)
    product_images2 = models.FileField(upload_to='sample/', null=True, blank=True, max_length=255)
    product_images3 = models.FileField(upload_to='sample/', null=True, blank=True, max_length=255)
    category = models.CharField(max_length=255, null=True)
    brand_name = models.CharField(max_length=255, null=True)
    sizeQuantity = models.CharField(max_length=255, null=True)
    petCompatibility = models.CharField(max_length=255, null=True)
    agesizesuitability = models.CharField(max_length=255, null=True)
    colorsVariations = models.CharField(max_length=255, null=True)
      # You can create a separate Category model if needed
   
    status=models.BooleanField(default=False)

    def str(self):
        return self.product_name
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    addressline1= models.CharField(max_length=100)
    addressline2= models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    city= models.CharField(max_length=15)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
