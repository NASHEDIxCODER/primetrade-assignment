# 🚀 Primetrade Backend Assignment

## 📌 Overview

This project is a scalable backend system built using **FastAPI**, implementing authentication, role-based access control (RBAC), and CRUD operations for task management. A simple frontend UI is included to demonstrate API interaction.

---

## ⚙️ Tech Stack

* **Backend:** FastAPI, Python
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Authentication:** JWT (JSON Web Tokens)
* **Validation:** Pydantic
* **Frontend:** Vanilla JavaScript (HTML, CSS)

---

## 🔐 Features

### Authentication

* User Registration
* User Login
* Password hashing (pbkdf2_sha256)
* JWT-based authentication

### Authorization

* Role-Based Access Control (User/Admin)
* Admin-only endpoints
* Protected routes

### Task Management

* Create Task
* Get Tasks
* Update Task
* Delete Task

### API Design

* RESTful endpoints
* Proper status codes
* Versioned API (`/api/v1`)
* Swagger documentation

---

## 🌐 API Endpoints

### Auth

* `POST /api/v1/auth/register`
* `POST /api/v1/auth/login`

### Tasks

* `GET /api/v1/tasks/`
* `POST /api/v1/tasks/`
* `PUT /api/v1/tasks/{id}`
* `DELETE /api/v1/tasks/{id}`

### Admin

* `GET /api/v1/tasks/admin/all`

---

## 🖥️ Frontend

A simple UI built with Vanilla JS:

* Register & Login users
* Store JWT in localStorage
* Access protected dashboard
* Create, view, and delete tasks
* Display API responses

---

## ▶️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/NASHEDIxCODER/primetrade-assignment.git
cd primetrade-assignment
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Update:

```
app/db/session.py
```

```python
DATABASE_URL = "postgresql://samrat:password@localhost/primetrade"
```

---

### 5. Run Server

```bash
uvicorn app.main:app --reload
```

---

### 6. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

### 7. Run Frontend

Open:

```
frontend/index.html
```

---

## 🔑 Authentication Flow

1. Register a user
2. Login to receive JWT token
3. Use token in requests:

```
Authorization: Bearer <token>
```

---

## 📊 Database Schema

### Users Table

* id
* email
* username
* password (hashed)
* role

### Tasks Table

* id
* title
* description
* is_done
* owner_id (FK → users)

---

## 📈 Scalability & Design

* Modular architecture (routers, models, schemas)
* Stateless JWT authentication (horizontal scaling)
* PostgreSQL for production-grade storage
* Easily extendable for microservices
* Can integrate:

  * Redis (caching)
  * Docker (containerization)
  * Load balancing

---

## 🧪 Testing

* Tested via Swagger UI
* Tested via frontend integration
* All CRUD operations verified

---

## 📁 Project Structure

```
app/
├── api/
├── core/
├── db/
├── models/
├── schemas/
├── main.py
```

---

## ✅ Status

✔ Backend Complete
✔ Frontend Integrated
✔ PostgreSQL Integrated
✔ Authentication & RBAC Working
✔ Fully Tested

---

## 👨‍💻 Author

Samrat
Backend Developer | Security Enthusiast
