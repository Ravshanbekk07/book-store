from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    
class Book(models.Model):
    title=models.CharField(max_length=255)
    #author=models.CharField(max_length=255)
    #author = models.ManyToManyField(Authors, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    price=models.FloatField(max_length=10)
    description=models.CharField(max_length=250)
    picture =models.ImageField(upload_to='uploads/')
    e_version=models.FileField(upload_to='documents/', max_length=150)
   
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title 

    

class Category(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    email=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
   
    STATUS = (
        
        ('Done','Done'), 
        ('New', 'New'),
        ('In Progress','In Progress')
       
    )
    order_date=models.DateField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    status = models.CharField(max_length = 100, choices = STATUS, default="New")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.status


class Category_book(models.Model):
    book_id=models.ForeignKey(Book, on_delete=models.CASCADE)   
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE) 
    
