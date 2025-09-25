# Inventory & Stock Management API

This is a **Django REST Framework** backend for managing products, stock transactions, and reports. It uses **Token Authentication** for secure API access.

---

## **Features**

- User Registration and Login (Token-based authentication)
- Product Management (CRUD)
- Stock Transactions (IN / OUT)
- Reports:
  - Current Stock
  - Low Stock
  - Total Sales
- Admin panel for managing products and transactions
- DRF Browsable API for testing

---

## **Technologies**

- Python 3.x  
- Django 5.x  
- Django REST Framework  
- SQLite (default database)  
- Token Authentication (`rest_framework.authtoken`)

---

## **Installation**

### **Clone the repository**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Create a virtual environment

bash
python -m venv venv
Activate it:

bash
# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Apply migrations

bash
python manage.py migrate
Create a superuser (optional, for admin panel)

bash
python manage.py createsuperuser
Run the server

bash
python manage.py runserver
Server will run at http://127.0.0.1:8000/

       API Endpoints
      Authentication
Endpoint	Method	Description
/api/auth/register/	POST         --- 	Register new user
/api/auth/login/	POST	         ---  Login and get token

         Headers:
Content-Type: application/json
Body Example for Registration/Login:

json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "password123"
}
Token for Postman Testing:
3a705c63942d438295def34edf6edd6d030f6b4e


Authorization Header for all protected endpoints:
Authorization: Token 3a705c63942d438295def34edf6edd6d030f6b4e

       Products
Endpoint	Method	Description
/api/products/	GET	List all products
/api/products/	POST	Create product (Admin only)
/api/products/<id>/	GET	Retrieve product
/api/products/<id>/	PUT/PATCH	Update product (Admin)
/api/products/<id>/	DELETE	Delete product (Admin)

       Stock Transactions
Endpoint	Method	Description
/api/transactions/	GET	List all transactions
/api/transactions/	POST	Create transaction
/api/transactions/<id>/	DELETE	Delete transaction


Body Example for Creating Transaction:
json
Copy code
{
  "product": 1,
  "quantity": 10,
  "transaction_type": "IN",
  "note": "Added stock"
}
transaction_type can be "IN" or "OUT".

        Reports
Endpoint	Method	Description
/api/reports/current-stock/	GET	View current stock levels
/api/reports/low-stock/?threshold=10	GET	Products below threshold
/api/reports/total-sales/	GET	Total quantity and value sold

Landing Page
URL: /
Description: Simple HTML page linking to API endpoints and admin panel.

Admin Panel
URL: /admin/
Manage products and stock transactions visually.

Postman Testing Example
1. List Products
Method: GET

URL: http://127.0.0.1:8000/api/products/

Headers:
Authorization: Token 3a705c63942d438295def34edf6edd6d030f6b4e
Content-Type: application/json

2. Create Product (Admin)
Method: POST
URL: http://127.0.0.1:8000/api/products/

Headers: Same as above

Body Example:

json
{
  "name": "Product B",
  "description": "New product",
  "price": "50.00",
  "stock_quantity": 100
}


3. Create Stock Transaction
Method: POST
URL: http://127.0.0.1:8000/api/transactions/

Headers: Same as above

Body Example:

json

{
  "product": 1,
  "quantity": 20,
  "transaction_type": "OUT",
  "note": "Sold 20 units"
}



License
MIT License © [M.ANBU SELVAN]

yaml
Copy code

---








