from django.db import models

class Category(models.Model):
  category_name= models.CharField(max_length= 56)
  
class Status(models.Model):
  status_name= models.CharField(max_length= 56)
  
class Product(models.Model):
  product_name= models.CharField(max_length= 256)
  product_price= models.IntegerField()
  status= models.ForeignKey(Status, on_delete= models.CASCADE)
  category= models.ForeignKey(Category, on_delete= models.CASCADE)