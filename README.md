# Little Lemon API Restaurant

## Table of Contents
* [Little Lemon API Restaurant](#little-lemon-api-restaurant)
    * [Installation](#installation)
    * [Endpoints](#endpoints)
        * [User Endpoints](#user-endpoints)
        * [Restaurant Endpoints](#restaurant-endpoints)
           * [Menu Items](#menu-items)
           * [Single Menu Item](#single-menu-item)
           * [Categories](#categories)
           * [Single Category](#single-category)
           * [Group Managers](#group-managers)
           * [Delete Manager](#delete-manager)
           * [Group Delivery Crew](#group-delivery-crew)
           * [Cart Menu Items](#cart-menu-items)
           * [Orders](#orders)
    * [Admin Panel](#admin-panel)

## Installation
1. Clone the Repository:
```
git clone https://github.com/Jeffreybekker/API-Project.git
```
2. Create a virtual environment:
```
python -m venv env
```
3. Start the virtual environment, depending on your system. You can get more information about this <a href="https://docs.python.org/3/tutorial/venv.html">here</a>.
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Run the server:
```
python manage.py runserver
```
## Endpoints
### User Endpoints

### Restaurant Endpoints
#### Menu Items
```
http://127.0.0.1:8000/api/menu-items/
```
#### Single Menu Item
```
http://127.0.0.1:8000/api/menu-items/{id}
```
#### Categories
```
http://127.0.0.1:8000/api/category/
```
#### Single Category
```
http://127.0.0.1:8000/api/category/{id}
```
#### Group Managers
```
http://127.0.0.1:8000/api/groups/manager/users
```
#### Delete Manager
```
http://127.0.0.1:8000/api/groups/manager/users{id}
```
#### Group Delivery Crew
```
http://127.0.0.1:8000/api/menu-items/
```
#### Cart Menu Items
```
http://127.0.0.1:8000/api/menu-items/
```
#### Orders
```
http://127.0.0.1:8000/api/menu-items/
```

## Admin Panel
        
