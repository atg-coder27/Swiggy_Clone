from rest_framework import serializers
from .models import *
from .models import Users,City,Model 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['userId','name','contactNo','emailId','password','userName','type_of_user']
    
    def create(self, validated_data):
        # data = {}
        # data["name"] = validated_data.pop("name")
        # data["contactNo"] = validated_data.pop("contactNo")
        # data["emailId"]  = validated_data.pop("emailId")
        user = Users(**validated_data)
        user.save()
        return user
        

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['cityId','cityName','stateName','userId']
    
    def create(self, validated_data):
        # user = validated_data.pop("userId")
        # cityName = validated_data["cityName"]
        # stateName = validated_data["stateName"]
        #city = City(userId = user ,cityName = cityName, stateName = stateName)
        city = City(**validated_data)
        city.save()
        return city
    
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['restaurantId','Address','cityId','ownerId','rating']
    
    def create(self, validated_data):
        restaurant = Restaurant(**validated_data)
        restaurant.save()
        return restaurant

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['addressId','userId','cityId','zipcode','current_address']
    
    def create(self, validated_data):
        address = Address(**validated_data)
        address.save()
        return address

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ['foodCategoryID','restaurentID','categoryName']
    
    def create(self, validated_data):
        food_category = FoodCategory(**validated_data)
        food_category.save()
        return food_category

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ItemsOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsOrdered
        fields = '__all__'
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsOrdered
        fields = '__all__'
        
    
    def create(self, validated_data):
        items_ordered = ItemsOrdered(**validated_data)
        items_ordered.price = items_ordered.menuID.price*items_ordered.quantity
        items_ordered.save()
        return items_ordered


    
    


    
        
        

    
    
    

    
    
