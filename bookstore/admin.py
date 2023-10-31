from django.contrib import admin
from .models import Book,Category,Category_book,Book_order,Order,Customer

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Category_book)
admin.site.register(Book_order)
admin.site.register(Order)
admin.site.register(Customer)