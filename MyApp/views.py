from re import M
import re
from django.db.models import indexes
from django.db.models.deletion import DO_NOTHING
from django.http import response,HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from .models import *
from .serializers import *


#General for both User and Restaurant Owner
class RegisterUser(APIView):
    def get(self,request):
        users = Users.objects.all()
        users_serialized = UserSerializer(users, many = True)
        print(Response(users_serialized))
        return Response(users_serialized.data)
    
    def post(self,request):
        check = request.data.get("password",None)
        if check == None:
            pass
        else:
            request.data["password"] = make_password(request.data["password"])
        users_serialized = UserSerializer(data = request.data)
        
        if users_serialized.is_valid():
            instance = users_serialized.save()
            request.data["userId"] = instance.userId
            type_of_user = request.data.get("type_of_user",None)
            if type_of_user == "customer":
                Customer.objects.create(userId = instance)
            else:
                RestaurantOwner.objects.create(userId = instance)

            city_serialized = CitySerializer(data = request.data)
            
            if city_serialized.is_valid():
                
                city_serialized.save()
                return Response(users_serialized.validated_data,status=status.HTTP_201_CREATED)
            
            return Response(city_serialized.error_messages ,status = status.HTTP_400_BAD_REQUEST)
        return Response(users_serialized.error_messages, status = status.HTTP_400_BAD_REQUEST)

#General for both user and restaurant owner
class LoginUser(APIView):
    def get(self,request):
        user = request.session.get("userName")
        if user != None:
            json = {"data" : "You have already logged in"}
            return Response(json, status = status.HTTP_200_OK)
        
        json = {"data": "Please login to continue"}
        return Response(json ,status= status.HTTP_401_UNAUTHORIZED)

        
    def post(self,request):
        user = request.data["userName"]
        password = request.data["password"]
        user_profile = Users.objects.get(userName = user)

        if check_password(password,user_profile.password):
            request.session["userName"] = user_profile.userName
            request.session["type_of_user"] = user_profile.type_of_user
            json = {"data" : "You have succsessfully logged in "}
            return Response(json,status = status.HTTP_202_ACCEPTED)
        json = {"data" : "Invalid UserName or password"}
        return Response(json, status = status.HTTP_401_UNAUTHORIZED)

class LogoutUser(APIView):
    def get(self,request):
        if request.session.get("userName",None) != None:
            del request.session["userName"]
        if request.session.get("user_type",None) != None:
            del request.session["user_type"]
        
        json = {"data" : "You have successfully logged out"}

        return Response(json,status = status.HTTP_200_OK)

#View for Restaurant Owner to add Restaurant
class AddRestaurant(APIView):
    def get(self,request,id=None):
        if id != None:
            restaurant = Restaurant.objects.get(restaurantId = id)
            restaurant_serializer = RestaurantSerializer(restaurant)
            return Response(restaurant_serializer.data, status= status.HTTP_202_ACCEPTED)
        restaurants = Restaurant.objects.all()
        restaurant_serializer = RestaurantSerializer(restaurants,many = True)
        return Response(restaurant_serializer.data,status= status.HTTP_202_ACCEPTED)

    def post(self,request):
        restaurant_serializer = RestaurantSerializer(data = request.data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            json = {"data" : "Restaurant successfully added"}
            return Response(json,status = status.HTTP_201_CREATED)
        
        return Response(restaurant_serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)
    
# General for both user and restaurant owner
class AddAdress(APIView):
    def get(self,request,id=None):
        if id != None:
            address = Address.objects.get(addressID = id)
            address_serializer = AddressSerializer(address)
            return Response(address_serializer.data,status = status.HTTP_202_ACCEPTED)
        address = Address.objects.all()
        address_serializer = AddressSerializer(address,many = True)
        return Response(address_serializer.data, status = status.HTTP_200_OK)

    def post(self,request):
        address_serializer = AddressSerializer(data = request.data)
        if address_serializer.is_valid():
            address_serializer.save()
            json = {"data" : "Address successfully added"}
            return Response(json, status = status.HTTP_201_CREATED)
        
        return Response(address_serializer.error_messages,status = status.HTTP_400_BAD_REQUEST)

#For Restuarant Owner
class AddFoodCategory(APIView):
    def get(self,request,id=None):
        if id != None:
            food_category = FoodCategory.objects.get(foodCategoryID = id)
            food_category_serializer = FoodCategorySerializer(FoodCategory)
            return Response(food_category_serializer.data, status = status.HTTP_202_ACCEPTED)
        food_category = FoodCategory.objects.all()
        food_category_serializer = FoodCategorySerializer(food_category)
        return Response(food_category_serializer.data, status = status.HTTP_200_OK)
    
    def post(self,request):
        food_category_serializer = FoodCategorySerializer(data = request.data)
        if food_category_serializer.is_valid():
            food_category_serializer.save()
            json = {"data" : "Address successfully added"}
            return Response(json , status = status.HTTP_201_CREATED)
        
        return Response(food_category_serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)

#For restaurant owner
class AddItemMenu(APIView):
    def get(self,request,id = None):
        if id != None:
            menu_items = Menu.objects.get(menuID = id)
            menu_items_serializer = MenuSerializer(menu_items)
            return Response(menu_items_serializer.data,status = status.HTTP_202_ACCEPTED)
        menu_items = Menu.objects.all()
        menu_items_serializer = MenuSerializer(menu_items)
        return Response(menu_items_serializer.data, status = status.HTTP_200_OK)

    def post(self,request):
        menu_items_serializer = MenuSerializer(data = request.data)
        if menu_items_serializer.is_valid():
            menu_items_serializer.save()
            json = {"data" : "Item successfully added in the menu"}
            return Response(json , status = status.HTTP_201_CREATED)

        return Response(menu_items_serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)
    
#For general user
class RequestOrder(APIView):
    def get(self,request):
        if request.session.get("userName") == None:
            json = {"data" : "You don't have access to request order"}
            return Response(json, status = status.HTTP_401_UNAUTHORIZED)
        userName = request.session.get("userName")

        userId = Users.objects.get(userName = userName)
        #return Response(userId)
        pending_orders = Order.objects.filter(orderstatus = "invalid",userId = userId)
        pending_orders_serializer = OrderSerializer(pending_orders,many = True)
        return Response(pending_orders_serializer.data , status = status.HTTP_202_ACCEPTED)
    
    def post(self,request):
        items_ordered = request.data.pop("items_ordered")
        order_serializer = OrderSerializer(data = request.data)
        
        if order_serializer.is_valid():
            instance = order_serializer.save()

            for items in items_ordered:
                items["orderId"] = instance.orderId
                item_order_serializer = ItemOrderSerializer(data = items)
                if item_order_serializer.is_valid():
                    item_order_serializer.save()
                else:
                    return Response(item_order_serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)
            

            json = {"data" : "Record succssfully updated"}
            return Response(json, status = status.HTTP_202_ACCEPTED)
        
        return Response(order_serializer.error_messages,status= status.HTTP_404_NOT_FOUND)

#Post request for abovde function
    # {
    #     "orderstatus": "invalid",
    #     "orderTime": "2021-10-18T19:28:44.594274Z",
    #     "userId": 5,
    #     "restaurantId": 1,
    #     "addressID": 1,
    #     "items_ordered" : [
    #             {
    #                    "menuID" : 1,
    #                    "quantity" : 3
    #             }
    #      ]
    # }  

class AcceptOrder(APIView):
    def get(self,request):
        if request.session.get("type_of_user") != "restaurant_owner":
            json = {"data" : "You don't have access to request order"}
            return Response(json, status = status.HTTP_401_UNAUTHORIZED)
        json = {"data": "Send a post request to that orderId to accept order"}
        return Response(json, status = status.HTTP_200_OK)

    def post(self,request):
        order_id = request.data.get("orderId")
        if order_id == None:
            json = {"data" : "No user found with that orderId"}
            return Response(json , status= status.HTTP_404_NOT_FOUND)
        
        data = Order.objects.filter(orderId = order_id)
        if len(data) == 0:
            json = {"data" : "No order found with the given order id "}
            return Response(json , status = status.HTTP_404_NOT_FOUND)
        
        for order in data:
            order.orderstatus = "inProgress"
            order.save()
        
        json = {"data" : "Order is Accepted by the restaurant"}
        return Response(json ,status = status.HTTP_202_ACCEPTED)
        


        


        




        

        

        


    








