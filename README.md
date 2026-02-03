# Django Projects

This repository contains all the projects I built while learning **Django and Django REST Framework (DRF)**.  
The focus of these projects is to understand **Django internals, RESTful API design, and CRUD operations**.

---

##  Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: MySQL
- **API Style**: REST
- **Language**: Python
- **Tools**: Postman (for API testing)

---

##  Project Categories

###  Basics (Django MVT)

These projects helped me understand Django’s **MVT (Model–View–Template)** architecture and request–response lifecycle.

- **Project-1-tutorial**  
   Covers:
  - Django project & app structure
  - Models and ORM
  - Views and URL routing
  - Templates and context data

- **Project_2**  
   Covers:
  - Form handling
  - Database operations using ORM
  - Dynamic rendering using templates

 Folder:
- [`Project-1-tutorial`](https://github.com/Cherry013/Django/tree/master/Project-1-tutorial)
- [`Project_2`](https://github.com/Cherry013/Django/tree/master/Project_2)

---

###  APIs (Django REST Framework)

These projects focus on **building RESTful APIs** using Django REST Framework.

####  Creating_API
- Introduction to API development using DRF
- Understanding:
  - Serializers
  - APIView
  - Request and Response objects

####  Student_Api
- Complete CRUD-based REST API
- Implemented using **Generic Views**
- Supports:
  - `GET` (List & Retrieve)
  - `POST` (Create)
  - `PUT` (Full Update)
  - `PATCH` (Partial Update)
  - `DELETE` (Remove)

 Key DRF concepts used:
- ModelSerializer
- GenericAPIView
- Mixins
- Proper HTTP status codes
- JSON-based request/response handling

---

##  API Operations Covered

| HTTP Method | Operation |
|------------|----------|
| GET | Retrieve all records / specific record |
| POST | Create a new record |
| PUT | Update an entire record |
| PATCH | Partial update |
| DELETE | Delete a record |

---

##  Key Concepts Learned

- Django ORM & database interactions (MySQL)
- REST architecture principles
- Serializer validation and data transformation
- URL routing and request lifecycle
- Handling JSON data
- HTTP status codes and API responses
- Difference between APIView and Generic Views

