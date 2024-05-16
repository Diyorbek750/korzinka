from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    price = models.BigIntegerField()
    image = models.ImageField(upload_to='products_images')
    
    def __str__(self):
        return self.name
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    
    @property
    def get_total_weight(self):
        total_weight = self.product.weight*self.quantity
        return total_weight
    
    @property
    def get_total_price(self):
        total_price = self.get_total_weight*self.product.price
        return total_price
    
    
    
