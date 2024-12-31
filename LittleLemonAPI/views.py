from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from .models import MenuItem, Category
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import *
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.contrib.auth.models import User, Group
from decimal import Decimal
# from .throttles import !!!!!

# GET OR POST menu items. Only managers can admin can add menu-items
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__icontains=search)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)
        
        paginator = Paginator(items,per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
            
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data, status.HTTP_200_OK)
        
    if request.method ==  'POST':
        if request.user.groups.filter(name='Manager').exists():
                serialized_item = MenuItemSerializer(data=request.data)
                serialized_item.is_valid(raise_exception=True)
                serialized_item.save()
                return Response(serialized_item.data, status.HTTP_201_CREATED)
        else:
            return Response({"message": "You're not authorized"}, 403)


# GET, PUT. PATCH OR DELETE A SINGLE ITEM, done by  manager
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    
    if request.method == 'GET':
        serializer = MenuItemSerializer(item)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        if request.user.groups.filter(name='Manager').exists():
            item.delete()
            return Response({"message": "item deleted"}, status.HTTP_200_OK)
        else:
            return Response({"message": "You're not authorized"}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'PUT' or 'PATCH':
        if request.user.groups.filter(name='Manager').exists():
            serializer = MenuItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "You're not authorized"}, status.HTTP_403_FORBIDDEN)


# Add/delete user to/from the Manager group
@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def Managers(request):
    
    if request.user.groups.filter(name='Manager').exists():
        if request.method == 'GET':
            users = User.objects.filter(groups__name="Manager")
            users_data = UserSerializer(users, many=True)
            return Response(users_data.data)

        username = request.data['username']
        if username:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name="Manager")
            if request.method == 'POST':
                managers.user_set.add(user)
                return Response({"message": "User added to the Manager group"}, status.HTTP_201_CREATED)
            elif request.method == 'DELETE':
                managers.user_set.remove(user)
                return Response({"message": "User deleted from the Manager group"})

        return Response({"message": "error"}, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Message": "You're not authorized"})


# Removes a particular user from the manager group.
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])
def manager_delete(request, id):
    if request.user.groups.filter(name='Manager').exists():
        if request.method != 'DELETE':
            return Response({"message": "This endpoint only supports DELETE."}, status.HTTP_400_BAD_REQUEST) 
        user = get_object_or_404(User, pk=id)
        if user.groups.filter(name='Manager').exists():
            managers = Group.objects.get(name="Manager")
            managers.user_set.remove(user)
            # message = 'User ' + user.get_username + ' ' + 'is not manager now.'
            return Response({"message": "manager removed from the group"}, status.HTTP_200_OK)
        else:
            return Response({"message": "This user is not a manager"}, status.HTTP_400_BAD_REQUEST) 
    else:
        return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN)
    

# URL: /api/category
# allow GET for all users. POST only for Managers
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def category(request):
    if request.method == 'GET':
        items = Category.objects.all()
        serialized_item = CategorySerializer(items, many=True)
        return Response(serialized_item.data, status.HTTP_200_OK)
    if request.method == 'POST' and request.user.groups.filter(name='Manager').exists():
        serialized_item = CategorySerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)
    return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN)


# URL: /api/category/<int:id>
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def single_category(request, id):
    item = get_object_or_404(Category, pk=id)
    if request.method == 'GET':
        serialized_item = CategorySerializer(item)
        return Response(serialized_item.data, status.HTTP_200_OK)
    
    elif request.method == 'POST':
        return Response({"message": "You are not authorized"}, status.HTTP_403_FORBIDDEN)
    
    if not request.user.groups.filter(name='Manager').exists():
        return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN)
    
    if request.method == 'PUT':
        serialized_item = CategorySerializer(item, data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_205_RESET_CONTENT)
    
    if request.method == 'PATCH':
        serialized_item = CategorySerializer(item, data=request.data, partial=True)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_205_RESET_CONTENT)
    
    if request.method == 'DELETE':
        item.delete()
        # message = item.title + ' is deleted.'
        return Response(status.HTTP_204_NO_CONTENT)
    


# URL: api/group/delivery-crew/users
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def delivery_set(request):
    if not request.user.groups.filter(name='Manager').exists():
        return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN)
    
    if request.method == 'POST':
        username = request.data['username']
        if username:
            user = get_object_or_404(User, username=username)
        else:
            return Response({"message": "Username incorrect or doesn't exist."}, status.HTTP_400_BAD_REQUEST)
        crew = Group.objects.get(name="Delivery crew")
        crew.user_set.add(user)
        return Response({"message": "User added to the delivery crew"}, status.HTTP_201_CREATED) 
    elif request.method == 'GET':
        crew = User.objects.filter(groups = Group.objects.get(name="Delivery crew"))
        serialized_item = UserSerializer(crew, many=True)
        return Response(serialized_item.data)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def delivery_delete(request, id):
    if request.method != 'DELETE':
            return Response({"message": "Only DELETE requests accepted"}, status.HTTP_400_BAD_REQUEST) 
    if request.user.groups.filter(name='Manager').exists():
        user = get_object_or_404(User, id=id)
        if user.groups.filter(name='Delivery crew').exists():
            crews = Group.objects.get(name='Delivery crew')
            crews.user_set.remove(user)
            return Response({"message": "User removed from the delivery crew"}, status.HTTP_200_OK)
        else:
            return Response({"message": "This user is not a delivery crew"}, status.HTTP_404_NOT_FOUND) 
    else:
        return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN)
    


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def cart(request):
    if request.method == 'GET':
        try:
            cart = Cart.objects.get(user=request.user)
        except:
            return Response({"message": "The cart is empty"})
        serialized_item = CartSerializer(cart)
        return Response(serialized_item.data, status.HTTP_200_OK)
    
    if request.method == 'POST':
        if Cart.objects.filter(user=request.user).exists():
            return Response({"message": "The user has already a cart."}, status.HTTP_400_BAD_REQUEST)
        menuitem = request.data["menuitem"]
        quantity = request.data["quantity"]
        unit_price = MenuItem.objects.get(pk=menuitem).price
        price = Decimal(quantity) * unit_price
        data = {"menuitem_id": menuitem, 
                "quantity": quantity,
                "unit_price": unit_price,
                "price": price,
                "user_id": request.user.id,
        }
        serialized_item = CartSerializer(data=data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response({"message": 'Cart is created'}, status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        cart = get_object_or_404(Cart, user=request.user)
        cart.delete()
        return Response({"message": "Cart is deleted"}, status.HTTP_200_OK)
    
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def order(request):
    if request.method == 'GET':
        if request.user.groups.filter(name='Manager').exists():
            orders = Order.objects.all()
            serialized_order = OrderSerializer(orders, many=True)
            return Response(serialized_order.data, status.HTTP_200_OK)
    
        elif request.user.groups.filter(name='Delivery crew').exists():
            orders = Order.objects.filter(delivery_crew=request.user)
            serialized_order = OrderSerializer(orders, many=True)
            return Response(serialized_order.data, status.HTTP_200_OK)

        else:
            if Order.objects.filter(user=request.user).exists():
                orders = Order.objects.filter(user=request.user)
                serialized_order = OrderSerializer(orders)
                return Response(serialized_order.data, status.HTTP_200_OK)
            else:
                return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        
        orderitem_data = {
            "user_id": cart.user_id,
            "menuitem_id": cart.menuitem_id,
            "quantity": cart.quantity,
            "unit_price": cart.unit_price,
            "price": cart.price
        }
        serialized_orderitem = OrderItemSerializer(data=orderitem_data)
        serialized_orderitem.is_valid(raise_exception=True)
        serialized_orderitem.save()
        
        orderitem = OrderItem.objects.get(user=request.user, menuitem=cart.menuitem)
        order_data = {
            "user_id": cart.user_id,
            "total": cart.price,
            "orderitem_id": orderitem.id,
        }
        serialized_order = OrderSerializer(data=order_data)
        serialized_order.is_valid(raise_exception=True)
        serialized_order.save()
        
        cart.delete()
        return Response({"message": "Order is created."}, status.HTTP_201_CREATED)
    return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN) 


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def order_single(request, id):
    order = get_object_or_404(Order, pk=id)
    if request.method == 'GET':
        if order.user != request.user:
            return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN)
        serialized_order = OrderSerializer(order)
        return Response(serialized_order.data, status.HTTP_200_OK)
    
    if request.method == 'PUT':
        if not request.user.groups.filter(name='Manager').exists():
            return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN) 
        serialized_item = OrderSerializer(order, data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_205_RESET_CONTENT)
    
    if request.method == 'PATCH':
        if request.user.groups.filter(name='Delivery crew').exists(): 
            
            if order.delivery_crew != request.user:
                return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN)
            
            deliverystatus = request.data["status"]
            status_data = {"status": deliverystatus}
            serialized_item = OrderSerializer(order, data=status_data, partial=True)
            serialized_item.is_valid(raise_exception=True)
            serialized_item.save()
            return Response(serialized_item.data, status.HTTP_205_RESET_CONTENT)
        if request.user.groups.filter(name='Manager').exists():
            serialized_item = OrderSerializer(order, data=request.data, partial=True)
            serialized_item.is_valid(raise_exception=True)
            serialized_item.save()
            return Response(serialized_item.data, status.HTTP_205_RESET_CONTENT)
        return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN) 
    
    if request.method == 'DELETE':
        if not request.user.groups.filter(name='Manager').exists():
            return Response({"message": "You are not authorized."}, status.HTTP_403_FORBIDDEN)
        order.delete()
        return Response(status.HTTP_204_NO_CONTENT)