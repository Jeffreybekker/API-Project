# Little Lemon API Restaurant

## Table of Contents
* [Little Lemon API Restaurant](#little-lemon-api-restaurant)
    * [Installation](#installation)
    * [Endpoints](#endpoints)
        * [User Endpoints](#user-endpoints)
           * [Users](#users)
           * [User Auth Token](#user-auth-token)
           * [User Information](#user-information)
           * [User Logout](#user-logout)
        * [API Endpoints](#api-endpoints)
           * [Menu Items](#menu-items)
           * [Single Menu Item](#single-menu-item)
           * [Categories](#categories)
           * [Single Category](#single-category)
           * [Managers](#managers)
           * [Delete Manager](#delete-manager)
           * [Delivery Crew](#delivery-crew)
           * [Delete Delivery Member](#delete-delivery-member)
           * [Cart Menu Items](#cart-menu-items)
           * [Orders](#orders)
           * [Single Order](#single-order)
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
#### Users
```
http://127.0.0.1:8000/auth/users/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Auth token</th>
			<th>Required</th>
			<th>Status code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Retrieve user based on token</td>
			<td>Yes</td>
			<td>-</td>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Create a user</td>
			<td>No</td>
			<td>- username<br>- email<br>- password</td>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>

#### User Auth Token
```
http://127.0.0.1:8000/auth/token/login/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Auth token</th>
			<th>Status code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>POST</td>
			<td>Retrieve Auth Token</td>
			<td>No</td>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>

![image](https://github.com/user-attachments/assets/15e1f94c-e61b-404c-a85c-5e7a1c9ed16b)

#### User Information
```
http://127.0.0.1:8000/auth/users/me/
```
#### User Logout
```
http://127.0.0.1:8000/auth/token/logout/
```
### API Endpoints
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
#### Managers
```
http://127.0.0.1:8000/api/groups/manager/users/
```
#### Delete Manager
```
http://127.0.0.1:8000/api/groups/manager/users{id}
```
#### Delivery Crew
```
http://127.0.0.1:8000/api/groups/delivery-crew/users/
```
#### Delete Delivery Member
```
http://127.0.0.1:8000/api/groups/delivery-crew/users/{id}
```
#### Cart Menu Items
```
http://127.0.0.1:8000/api/cart/menu-items/
```
#### Orders
```
http://127.0.0.1:8000/api/orders/
```
#### Single Order
```
http://127.0.0.1:8000/api/orders/{id}
```
## Admin Panel
        
