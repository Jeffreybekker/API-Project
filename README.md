# Little Lemon API Restaurant

## Table of Contents
* [Little Lemon API Restaurant](#little-lemon-api-restaurant)
    * [Installation](#installation)
    * [Endpoints](#endpoints)
        * [User Endpoints](#user-endpoints)
           * [Users](#users)
           * [User Auth Token](#user-auth-token)
           * [User Management](#user-management)
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
*Note: only the admin can retrieve all the users. The others can retrieve only themselves.*
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Auth Token</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Retrieve user based on token</td>
			<td>Yes</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Create a user</td>
			<td>No</td>
			<td>"username",<br>"email",<br>"password"</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>

*Example of creating a user:*
![image](https://github.com/user-attachments/assets/e64a7fa0-939e-4251-bbc6-a4422d8c4067)

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
			<th>Required Fields</th>
			<th>Status code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>POST</td>
			<td>Retrieve Auth Token</td>
			<td>No</td>
			<td>"username",<br>"password"</td>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>

![image](https://github.com/user-attachments/assets/15e1f94c-e61b-404c-a85c-5e7a1c9ed16b)

#### User Management
```
http://127.0.0.1:8000/auth/users/me/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Auth Token</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Retrieve user based on token</td>
			<td>Yes</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>DELETE</td>
			<td>Deletes a user</td>
			<td>Yes</td>
			<td>"current_password"</td>
			<td>204 No Content</td>
		</tr>
	</tbody>
</table>

*Example of how to delete a user. It takes a current_password and auth token:*
![image](https://github.com/user-attachments/assets/06f1183c-37a4-4889-9bda-1461d72d318a)

#### User Logout
```
http://127.0.0.1:8000/auth/token/logout/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Auth token</th>
			<th>Required Fields</th>
			<th>Status code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>POST</td>
			<td>User logout</td>
			<td>Yes</td>
			<th>-</th>
			<td>204 No Content</td>
		</tr>
	</tbody>
</table>

![image](https://github.com/user-attachments/assets/b2c09e07-68eb-42d0-99fd-e88775625f7d)

### API Endpoints
#### Menu Items
```
http://127.0.0.1:8000/api/menu-items/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Get all menu items</td>
			<td>Customers<br>Delivery Crew<br>Managers</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Add menu item</td>
			<td>Managers</td>
			<td>"title",<br>"price",<br>"featured" (true, false),<br>"category_id"</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>

*Example of a POST request for adding a menu item, authorized as a manager:*
![image](https://github.com/user-attachments/assets/b2d06c5f-8a9f-44cf-bf64-eb5040a9c7fa)

#### Single Menu Item
```
http://127.0.0.1:8000/api/menu-items/{id}
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Get menu item</td>
			<td>Customers<br>Delivery Crew<br>Managers</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>PUT</td>
			<td>Update menu item</td>
			<td>Managers</td>
			<td>"title",<br>"price",<br>"featured",<br>"category_id"</td>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>PATCH</td>
			<td>Update menu item</td>
			<td>Managers</td>
			<td>"title",<br>"price",<br>"featured",<br>"category_id"</td>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>DELETE</td>
			<td>Delete menu item</td>
			<td>Managers</td>
			<th>-</th>
			<td>204 No Content</td>
		</tr>
	</tbody>
</table>

*Example of a PUT request with the required request fields:*
![image](https://github.com/user-attachments/assets/7d77388a-1d03-455d-82f7-f61c0228fccc)

#### Categories
```
http://127.0.0.1:8000/api/category/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Get all categories</td>
			<td>Customers<br>Delivery Crew<br>Managers</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Add category</td>
			<td>Managers</td>
			<td>"slug",<br>"title"</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>

*Example of a POST request for adding a category:*
![image](https://github.com/user-attachments/assets/1a64cda6-2eb2-4ebd-ac46-90dfbc74706f)

#### Single Category
```
http://127.0.0.1:8000/api/category/{slug}
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Get category</td>
			<td>Customers<br>Delivery Crew<br>Manangers</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Forbidden</td>
			<th>-</th>
			<th>-</th>
			<td>403 Forbidden</td>
		</tr>
		<tr>
			<td>PUT</td>
			<td>Update category</td>
			<td>Managers</td>
			<td>"slug",<br>"title"</td>
			<td>205 Reset Content</td>
		</tr>
		<tr>
			<td>PATCH</td>
			<td>Partially update category</td>
			<td>Managers</td>
			<td>"slug",<br>AND/OR:<br>"title"</td>
			<td>205 Reset Content</td>
		</tr>
		<tr>
			<td>DELETE</td>
			<td>Delete category</td>
			<td>Managers</td>
			<th>-</th>
			<td>204 No Content</td>
		</tr>
	</tbody>
</table>

*Example of a PUT request for renaming the category:*
<br>
*URL was http://127.0.0.1:8000/api/category/Fruits*
![image](https://github.com/user-attachments/assets/f70f0fd8-5f4a-479c-ad3f-1ab4b13daf70)

*After the category update, the URL is now http://127.0.0.1:8000/api/category/Fruit-Smoothie*

#### Managers
```
http://127.0.0.1:8000/api/groups/manager/users/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Get all managers</td>
			<td>Managers</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Add user to manager group</td>
			<td>Managers</td>
			<td>"username"</td>
			<td>201 Created</td>
		</tr>
		<tr>
			<td>DELETE</td>
			<td>Forbidden</td>
			<th>-</th>
			<th>-</th>
			<td>403 Forbidden</td>
		</tr>
	</tbody>
</table>

*Example of adding a user to the manager group:*
![image](https://github.com/user-attachments/assets/ef874669-4cbd-45c2-96fc-9d5808cca83b)


#### Delete Manager
```
http://127.0.0.1:8000/api/groups/manager/users/{id}
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>DELETE</td>
			<td>Delete user from the manager group</td>
			<td>Managers</td>
			<td>"username"</dh>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>

*Example of deleting a user from the manager group:*
![image](https://github.com/user-attachments/assets/49f587e9-64b8-4d30-90fa-4750e45295eb)

#### Delivery Crew
```
http://127.0.0.1:8000/api/groups/delivery-crew/users/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Get all delivery members</td>
			<td>Managers</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Add user to delivery crew</td>
			<td>Managers</td>
			<td>"username"</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>

*Example of adding a user to the delivery crew:*
![image](https://github.com/user-attachments/assets/339ddf88-ee17-4922-8e77-822a219a0561)

#### Delete Delivery Member
```
http://127.0.0.1:8000/api/groups/delivery-crew/users/{id}
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>DELETE</td>
			<td>Delete user from the delivery crew</td>
			<td>Managers</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>

*Example of deleting a user from the delivery crew:*
![image](https://github.com/user-attachments/assets/71b133c4-db9c-4140-bb8a-188b5af045af)

#### Cart Menu Items
```
http://127.0.0.1:8000/api/cart/menu-items/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Get user, menu item and cart information</td>
			<td>Current customer</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Create a cart</td>
			<td>Customer</td>
			<td>"menuitem", (id item)<br>"quantity"</td>
			<td>201 Created</td>
		</tr>
		<tr>
			<td>DELETE</td>
			<td>Delete cart</td>
			<td>Customer</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>

*Example of a GET request to retrieve the cart:* <br>
*Note: you can only get the cart items if you made a POST request before:*
![image](https://github.com/user-attachments/assets/069f0f6a-782f-4bf2-bdce-a4935bab9490)

#### Orders
```
http://127.0.0.1:8000/api/orders/
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Retrieve user based on token</td>
			<td>Yes</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Create a user</td>
			<td>No</td>
			<td>- username<br>- email<br>- password</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>

#### Single Order
```
http://127.0.0.1:8000/api/orders/{id}
```
<table>
	<thead>
		<tr>
			<th>HTTP Method</th>
			<th>Action</th>
			<th>Role</th>
			<th>Required Fields</th>
			<th>Status Code</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>GET</td>
			<td>Retrieve user based on token</td>
			<td>Yes</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>PUT</td>
			<td>Create a user</td>
			<td>No</td>
			<td>- username<br>- email<br>- password</td>
			<td>201 Created</td>
		</tr>
		<tr>
			<td>PATCH</td>
			<td>Create a user</td>
			<td>No</td>
			<td>- username<br>- email<br>- password</td>
			<td>201 Created</td>
		</tr>
		<tr>
			<td>DELETE</td>
			<td>Create a user</td>
			<td>No</td>
			<td>- username<br>- email<br>- password</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>

## Admin Panel
        
