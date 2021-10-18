from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterUser.as_view()),
    path('login/',views.LoginUser.as_view()),
    path('logout/',views.LogoutUser.as_view()),
    path('addRestaurant/',views.AddRestaurant.as_view()),
    path('addRestaurant/<int:id>/',views.AddRestaurant.as_view()),
    path('addAddress/',views.AddAdress.as_view()),
    path('addAddress/<int:id>/',views.AddAdress.as_view()),
    path('addFoodCategory/',views.AddFoodCategory.as_view()),
    path('addFoodCategory/<int:id>',views.AddFoodCategory.as_view()),
    path('requestOrder/',views.RequestOrder.as_view()),
    path('acceptOrder/',views.AcceptOrder.as_view()),
]
