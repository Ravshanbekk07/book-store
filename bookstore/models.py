from django.db import models


class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    price=models.FloatField(max_length=10)
    description=models.CharField(max_length=250)
    picture =models.ImageField(upload_to='uploads/')

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
    order_date=models.DateField(auto_now=True)
    total_price=models.FloatField(max_length=250)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)


    
class Book_order(models.Model):
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    book_id=models.ForeignKey(Book,on_delete=models.CASCADE)

class Category_book(models.Model):
    book_id=models.ForeignKey(Book, on_delete=models.CASCADE)   
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE) 
    
