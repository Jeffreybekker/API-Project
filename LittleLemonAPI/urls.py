from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.menu_items),
    path('menu-items/<int:id>', views.single_item),
    
    path('category/', views.category),
    path('category/<slug:slug>', views.single_category),
    
    path('groups/manager/users/', views.Managers),
    path('groups/manager/users/<int:id>', views.manager_delete),
    
    path('groups/delivery-crew/users/', views.delivery_set),
    path('groups/delivery-crew/<int:id>', views.delivery_delete),
    
    path('cart/menu-items', views.cart), 
    
    path('orders/', views.order),
    path('orders/<int:id>', views.order_single),
]
