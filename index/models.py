from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Saved(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
