# Product API

A simple RESTful Product API built with **Django** and **Django REST Framework (DRF)**.

This project focuses on building a backend API with product management, serializer validation, pagination, and token-based authentication.

## 🚀 Features

* List all products
* Create a new product
* Token-based authentication
* Protected product creation
* Public product listing
* Product data validation
* Pagination
* Ordered product results
* API testing with Postman
* Django REST Framework's generic API views

## 🛠️ Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* Postman
* Token Authentication

## 📁 Project Structure

```text
shop_project/
│
├── manage.py
│
├── shop_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── products/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── tests.py
```

## 📦 Product Model

Each product contains:

| Field         | Type         | Description                          |
| ------------- | ------------ | ------------------------------------ |
| `id`          | AutoField    | Automatically generated product ID   |
| `name`        | CharField    | Product name, maximum 100 characters |
| `description` | TextField    | Product description                  |
| `price`       | DecimalField | Product price with 2 decimal places  |
| `stock`       | IntegerField | Available stock quantity             |

### Validation Rules

* Product name cannot be blank.
* Product price must be greater than `0`.
* Stock cannot be negative.
* Products are ordered by their `id`.

## 🔗 API Endpoint

### Products

```text
/api/products/
```

### GET — List Products

```http
GET /api/products/
```

Product listing is publicly accessible.

Example response:

```json
{
    "count": 6,
    "next": "http://127.0.0.1:8000/api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Laptop",
            "description": "A powerful laptop",
            "price": "75000.00",
            "stock": 10
        }
    ]
}
```

## 📄 Pagination

The API uses pagination with **5 products per page**.

For example:

```http
GET /api/products/?page=2
```

If there are more than five products, the sixth product will appear on page 2.

## ➕ POST — Create Product

Creating a product requires authentication.

```http
POST /api/products/
```

### Authorization

The API uses **DRF Token Authentication**.

Add the following header in Postman:

```http
Authorization: Token YOUR_TOKEN
```

Replace `YOUR_TOKEN` with your valid authentication token.

### Request Body

Use:

```text
Body → raw → JSON
```

Example:

```json
{
    "name": "Mechanical Keyboard",
    "description": "RGB mechanical keyboard",
    "price": "3500.00",
    "stock": 20
}
```

A valid authenticated request will create the product.

## 🔐 Authentication & Permissions

The API uses:

```text
TokenAuthentication
```

and:

```text
IsAuthenticatedOrReadOnly
```

This means:

| Request               | Authentication |
| --------------------- | -------------- |
| `GET /api/products/`  | Not required   |
| `POST /api/products/` | Required       |

Unauthenticated users can read products, but they cannot create products.

## 🧪 Testing with Postman

### 1. Test GET

Send:

```http
GET http://127.0.0.1:8000/api/products/
```

No authentication is required.

### 2. Test POST

Send:

```http
POST http://127.0.0.1:8000/api/products/
```

Add the authentication header:

```http
Authorization: Token YOUR_TOKEN
```

Then select:

```text
Body → raw → JSON
```

and send:

```json
{
    "name": "Mechanical Keyboard",
    "description": "RGB mechanical keyboard",
    "price": "3500.00",
    "stock": 20
}
```

### 3. Test Pagination

Create more than five products and request:

```http
GET http://127.0.0.1:8000/api/products/?page=2
```

The second page should contain the remaining products.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd shop_project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an authentication token

Create a user:

```bash
python manage.py createsuperuser
```

Then generate/retrieve the user's DRF token through the configured token authentication system.

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/api/products/
```

## 🔑 Authentication Flow

The basic authentication flow is:

```text
User
  ↓
Login / Token
  ↓
Receive Authentication Token
  ↓
Add Token to Request Header
  ↓
POST /api/products/
  ↓
Django REST Framework
  ↓
Permission Check
  ↓
Serializer Validation
  ↓
Product Created
```

## 📌 API Summary

| Method | Endpoint         | Authentication | Purpose        |
| ------ | ---------------- | -------------- | -------------- |
| `GET`  | `/api/products/` | ❌ No           | List products  |
| `POST` | `/api/products/` | ✅ Token        | Create product |

## 🎯 Project Scope

This project is intentionally focused on the fundamentals of building a REST API.

### Included

* Product model
* REST API
* Serializers
* Validation
* Authentication
* Permissions
* Pagination
* Postman API testing

### Not Included

* Frontend
* Product editing
* Product deletion
* Shopping cart
* Payment system
* Order management

## 📚 What I Learned

Through this project, I practiced:

* Building REST APIs with Django REST Framework
* Working with serializers
* Model validation
* Generic API views
* Authentication and permissions
* Token authentication
* API pagination
* HTTP methods
* Testing APIs using Postman
* Understanding the difference between public and protected API operations

## 👨‍💻 Author

**Rahimur Rahman Showrav**

B.Sc. in Computer Science & Engineering

---

⭐ If you find this project useful, feel free to explore the repository and try the API yourself.
