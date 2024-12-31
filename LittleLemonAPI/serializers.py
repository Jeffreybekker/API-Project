from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
        
class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
class CartSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Cart
        fields = ['user', 'user_id', 'menuitem', 'menuitem_id', 'quantity', 'unit_price', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    menuitem = MenuItemSerializer(read_only=True)
    menuitem_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = OrderItem
        fields = ['user_id', 'menuitem', 'menuitem_id', 'quantity', 'unit_price', 'price']

class OrderSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    orderitem = OrderItemSerializer(read_only=True)
    orderitem_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user_id', 'delivery_crew','status', 'total', 'date', 'orderitem', 'orderitem_id',]