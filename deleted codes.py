# class Customer(models.Model):
#     name=models.CharField(max_length=50)
    
#     address=models.CharField(max_length=250)
#     email=models.CharField(max_length=150)

#     def __str__(self) -> str:
#         return self.name


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Customer
#         fields="__all__"



# class CustomerList(APIView):
#     # authentication_classes=[BasicAuthentication]
#     # permission_classes=[IsAuthenticated]

#     def get(self,request):
#         user=request.user
        
       
#         if not user.is_superuser:
#                 return Response({'error':'Forbidden'},status=403)
#         else:
#             customer=Customer.objects.all()
#             serializer=CustomerSerializer(customer,many=True)
#             return Response(serializer.data)
# class CustomerDetail(APIView):
#     # authentication_classes=[BasicAuthentication]
#     # permission_classes=[IsAuthenticated]

#     def get(self,request,pk:int):
#         user=request.user
        
#         # if not user:
#         #         return Response({'error':'unauthorized'},status =401)
#         if not user.is_superuser:
#                 return Response({'error':'Forbidden'},status=403)
#         else:
#                 customer=get_object_or_404(Customer,id=pk)
#                 serializer=CustomerSerializer(customer)
#                 return Response(serializer.data)




# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     # list_display=['id','name','email']
#     search_fields=['name','id']




# path('customer/all/',CustomerList.as_view()),
#     path('customer/<int:pk>/',CustomerDetail.as_view()),