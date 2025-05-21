# 🚀 FastAPI CRUD App with Alembic & PostgreSQL

This is a simple **FastAPI** project demonstrating **CRUD operations** with a **PostgreSQL** database, using **SQLAlchemy** as ORM and **Alembic** for database migrations.

---

## 📦 Features

- 🔧 FastAPI REST API
- 🧰 SQLAlchemy ORM
- 🔄 Alembic for migrations
- 🐘 PostgreSQL backend
- 📁 Modular, clean project structure

---

## 🏗️ Project Structure

```
fastapi_crud/
├── alembic/
│   └── versions/
├── app/
│   ├── crud.py           # CRUD operations
│   ├── database.py       # DB engine/session setup
│   ├── main.py           # FastAPI app & routes
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
├── alembic.ini           # Alembic configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Requirements

- Python 3.7+
- PostgreSQL (running locally or via Docker)
- Virtual environment (recommended)

---

## 🧪 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fastapi-crud.git
cd fastapi-crud
```

### 2. Setup Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🛠️ Configure Database

Set the database connection string in both:

- `app/database.py`
- `alembic.ini`

Example:

```
DATABASE_URL = "postgresql://postgres:password@localhost/fastapi_db"
```

Create the database manually:

```bash
createdb fastapi_db
```

---

## 🧬 Database Migrations (Alembic)

### 1. Initialize Alembic (only once):

```bash
alembic init alembic
```

### 2. Edit `alembic/env.py`

Import `Base` and models:

```python
from app.database import Base
from app.models import *
target_metadata = Base.metadata
```

### 3. Generate & Apply Migrations

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

---

## 🚀 Run the FastAPI App

```bash
uvicorn app.main:app --reload
```

Visit:

- API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📬 Available Endpoints

| Method | Path            | Description         |
|--------|------------------|---------------------|
| POST   | `/items/`        | Create a new item   |
| GET    | `/items/`        | Get all items       |
| GET    | `/items/{id}`    | Get item by ID      |

---
