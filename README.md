# employee-management-api
A secure and RESTful Employee Management API built using **Django Rest Framework**.  
This project supports full **CRUD operations**, **JWT authentication**, **filtering**, **pagination**, and **unit testing**.

---

## 🚀 Project Objective

To build a backend REST API for managing employees in a company while following:
- RESTful principles
- Proper authentication & authorization
- Clean and modular code
- Validation and error handling
- Automated testing

---

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT Authentication
- SQLite (default database)
- Postman (for API testing)

---

## 🔐 Authentication

This API uses **JWT (JSON Web Token)** authentication.

### Obtain Token
**POST** `/api/token/`

```json
{
  "username": "your_username",
  "password": "your_password"
}
Response

json
Copy code
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
Use the access token in Postman:

Authorization → Bearer Token

Paste the access token

📌 API Endpoints
Create Employee
POST /api/employees/

json
Copy code
{
  "name": "Rahul Sharma",
  "email": "rahul@gmail.com",
  "department": "HR",
  "role": "Manager"
}
Response: 201 Created

List Employees
GET /api/employees/

Supports:

Pagination (10 per page)

Filtering

Example:

bash
Copy code
/api/employees/?department=HR
/api/employees/?role=Manager
/api/employees/?page=2
Retrieve Single Employee
GET /api/employees/{id}/

200 OK if found

404 Not Found if invalid ID

Update Employee
PUT /api/employees/{id}/

json
Copy code
{
  "name": "Updated Name",
  "department": "Engineering"
}
Delete Employee
DELETE /api/employees/{id}/

204 No Content

✅ Validations & Error Handling
Email must be unique

Name cannot be empty

Proper HTTP status codes:

201 Created

400 Bad Request

401 Unauthorized

404 Not Found

204 No Content

🧪 Testing
Unit tests are written using Django’s test framework.

Run Tests
bash
Copy code
python manage.py test
All API endpoints are covered including:

Create employee

Duplicate email validation

List employees

Retrieve single employee

Delete employee

⚙️ Setup Instructions
1. Clone Repository
bash
Copy code
git clone https://github.com/<your-username>/employee-management-api.git
cd employee-management-api
2. Create Virtual Environment
bash
Copy code
python -m venv env
env\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5. Create Superuser
bash
Copy code
python manage.py createsuperuser
6. Run Server
bash
Copy code
python manage.py runserver
Server will start at:

cpp
Copy code
http://127.0.0.1:8000/
📄 Project Status
✅ Completed
✅ Fully tested
✅ Ready for production-level review

👤 Author
Utsav Patil
Python Backend Developer

---

## ✅ After this (VERY IMPORTANT)

Make sure your repository contains:
- ✔ `README.md` (this one)
- ✔ `employees/` app
- ✔ `tests.py`
- ✔ `requirements.txt`
- ✔ Clean commit history

---
