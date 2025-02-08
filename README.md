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

*Note: Example of how to delete a user. It takes a current_password and auth token:*
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
			<td>Retrieve all menu items</td>
			<td>Customers<br>Managers<br>Admin</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Add a menu item</td>
			<td>Managers<br>Admin</td>
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
			<td>Get a menu item</td>
			<td>Customers<br>Managers<br>Admin</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>PUT</td>
			<td>Update menu item</td>
			<td>Managers<br>Admin</td>
			<td>"title",<br>"price",<br>"featured",<br>"category_id"</td>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>PATCH</td>
			<td>Partially update menu item</td>
			<td>No</td>
			<td>"title",<br>"price",<br>"featured",<br>"category_id"</td>
			<td>201 Created</td>
		</tr>
		<tr>
			<td>DELETE</td>
			<td>Delete menu item</td>
			<td>Managers<br>Admin</td>
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
			<td>Retrieve all categories</td>
			<td>Customers<br>Managers<br>Admin</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
		<tr>
			<td>POST</td>
			<td>Add a category</td>
			<td>Managers</td>
			<td>- username<br>- email<br>- password</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>

#### Single Category
```
http://127.0.0.1:8000/api/category/{id}
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
			<td>Retrieve category</td>
			<td>Customers<br>Manangers<br>Admin</td>
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
		<tr>
			<td>DELETE</td>
			<td>Create a user</td>
			<td>No</td>
			<td>- username<br>- email<br>- password</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>

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
			<td>Retrieve user based on token</td>
			<td>Yes</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>

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
			<td>Retrieve user based on token</td>
			<td>Yes</td>
			<th>-</th>
			<td>200 OK</td>
		</tr>
	</tbody>
</table>

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
		<tr>
			<td>DELETE</td>
			<td>Create a user</td>
			<td>No</td>
			<td>- username<br>- email<br>- password</td>
			<td>201 Created</td>
		</tr>
	</tbody>
</table>

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
        
