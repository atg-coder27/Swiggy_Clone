from django.contrib import admin
from rest_framework.compat import LONG_SEPARATORS
from .models import *


# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['userId','name','contactNo','emailId']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['cityId','cityName','stateName','userId']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customerId','userId']

@admin.register(RestaurantOwner)
class RestaurantOwnerAdmin(admin.ModelAdmin):
    list_display = ['ownerId', 'userId']

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurantId','Address','cityId','ownerId','rating']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['addressID','cityId','userId','zipcode','current_address']

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['foodCategoryID','restaurentID','categoryName']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['menuID','restaurantId','foodCategoryId','description','price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderId','userId','restaurantId','addressID','orderstatus','orderTime']

@admin.register(ItemsOrdered)
class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ['itemOrderId','orderId','menuID','quantity','price']


