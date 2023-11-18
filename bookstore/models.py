from django.db import models
from django.contrib.auth.models import User

class Authors(models.Model):
    
    name = models.CharField(max_length=100,unique=True)
   
    description=models.CharField(max_length=400,blank=True,null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    


class Category(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=250,null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=255)
    author = models.ManyToManyField(Authors,related_name='books')
    category = models.ManyToManyField(Category,related_name='categories')
    price=models.FloatField(max_length=10,null=True,blank=True)
    description=models.CharField(max_length=400,blank=True,null=True)
    picture =models.ImageField(upload_to='uploads/',null=True,blank=True)
    e_version=models.FileField(upload_to='documents/', max_length=150,blank=True,null=True)
   
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title 

 

    
class Order(models.Model):
   
    STATUS = (
        
        ('Done','Done'), 
        ('New', 'New'),
        ('In Progress','In Progress'),
        ('cancelled','cancelled')
       
    )
    order_date=models.DateField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer_id=models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length = 100, choices = STATUS, default="New")

    def __str__(self) -> str:
        return self.status


class Likes(models.Model):
    book_id=models.ForeignKey(Book, on_delete=models.CASCADE)  
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateField(auto_now=True)
