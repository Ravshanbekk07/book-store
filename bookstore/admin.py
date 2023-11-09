from django.contrib import admin
from .models import Book,Category,Category_book,Order,Customer,Authors,Likes

# admin.site.register(Book)
# admin.site.register(Category)
# admin.site.register(Category_book)
# admin.site.register(Book_order)
# admin.site.register(Order)
# admin.site.register(Authors)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title','price','active']
    list_filter=['active','created_at','updated_at']
    date_hierarchy='created_at'
    search_fields=['title','author']
    actions=('mark_as_inactive','mark_as_active')

    @admin.action(description='update inactive')
    def mark_as_inactive(self,request,queryset):
        queryset.update(active=False) 

    @admin.action(description='update active')
    def mark_as_active(self,request,queryset):
        queryset.update(active=True)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']
    search_fields=['name']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','name','email']
    search_fields=['name','id']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','status','book','status']
    search_fields=['status','order_date']
    list_filter=['status','order_date']
    date_hierarchy='order_date'
    ordering=['status','order_date']
    actions=('mark_as_done','mark_as_new')

    @admin.action(description='update done')
    def mark_as_done(self,request,queryset):
        queryset.update(status="Done") 

    @admin.action(description='update new')
    def mark_as_new(self,request,queryset):
        queryset.update(status="New")



@admin.register(Category_book)
class CategoryBookAdmin(admin.ModelAdmin):
    list_display=['id','book_id','category_id']
    search_fields=['book_id__title','category_id__name']
     
@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname']

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display=['book_id',"user_id"]