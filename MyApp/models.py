
from typing import Callable
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Create your models here.
class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length = 100,unique = True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length= 1500,null = False)
    contactNo = models.CharField(max_length=15)
    emailId = models.EmailField(max_length=50)
    type_of_user = models.CharField(max_length=100,choices= (('customer','customer'), ('restaurant_owner','restaurant_owner')))
    def __str__(self) -> str:
        return str(self.userId)

class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users,on_delete= models.CASCADE)

class RestaurantOwner(models.Model):
    ownerId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users,on_delete=models.CASCADE)



class City(models.Model):
    cityId = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=100)
    stateName = models.CharField(max_length= 50)
    userId = models.ForeignKey(Users,on_delete=models.CASCADE)

class Restaurant(models.Model):
    restaurantId = models.AutoField(primary_key= True)
    Address = models.CharField(max_length= 100)
    cityId = models.ForeignKey(City,on_delete= models.CASCADE)
    ownerId = models.ForeignKey(RestaurantOwner,on_delete= models.CASCADE)
    rating = models.IntegerField()

class Address(models.Model):
    addressID = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users,on_delete=models.CASCADE)
    cityId = models.ForeignKey(City,on_delete=models.CASCADE)
    #restaurantId = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=10)
    current_address = models.TextField()

class FoodCategory(models.Model):
    foodCategoryID = models.AutoField(primary_key= True)
    restaurentID = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    categoryName = models.CharField(max_length=100)

#This is menuItem , not menu
class Menu(models.Model):
    menuID = models.AutoField(primary_key= True)
    restaurantId = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    foodCategoryId = models.ForeignKey(FoodCategory,on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField(default=0)



class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users,on_delete=models.CASCADE)
    restaurantId = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    addressID = models.ForeignKey(Address,on_delete=models.CASCADE)
    orderstatus = models.CharField(max_length=100,default= "invalid")
    orderTime = models.DateTimeField(auto_now_add= True)


class ItemsOrdered(models.Model):
    itemOrderId = models.AutoField(primary_key=True)
    orderId = models.ForeignKey(Order,on_delete=models.CASCADE)
    menuID = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    #name this to total_price


class Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users,on_delete=models.CASCADE)
    orderId = models.ForeignKey(Order,on_delete=models.CASCADE)
    amount = models.IntegerField()
    paymentStatus = models.CharField(max_length=100,default= "ongoing")



