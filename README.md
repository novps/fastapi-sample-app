## 🧾 NoVPS To-Do Demo Application

This is a **demo project** built to showcase how easily you can deploy a **FastAPI** application connected to a **managed PostgreSQL database** using **NoVPS Cloud Platform**.

It demonstrates a real-world backend with async database access, REST API endpoints, and a simple **Tailwind-based** web interface — all running seamlessly on the NoVPS platform.

---

### 🚀 Features

* 🧠 **FastAPI (async)** — modern, high-performance Python web framework
* 🗄 **PostgreSQL (managed by NoVPS)** — persistent database layer
* ⚙️ **SQLAlchemy 2.0 (async)** — clean ORM and async queries
* 🎨 **Tailwind CSS frontend** — minimalistic and responsive UI
* 🔄 **Docker-ready** — easy to build and deploy anywhere
* 🌩 **Fully compatible with NoVPS** — ready for one-click deployment

---

### 🧱 Tech Stack

| Component            | Description                           |
| -------------------- | ------------------------------------- |
| **Backend**          | FastAPI (Python 3.12)                 |
| **Database**         | PostgreSQL (asyncpg + SQLAlchemy 2.0) |
| **Frontend**         | HTML + Tailwind CSS                   |
| **Containerization** | Docker                                |
| **Deployment**       | NoVPS Cloud Platform                  |

---

### 📁 Project Structure

```
app/
 ├── main.py          # FastAPI entry point (with lifespan events)
 ├── database.py      # Async SQLAlchemy setup
 ├── models.py        # Database models
 ├── schemas.py       # Pydantic schemas
 ├── crud.py          # Database operations
 └── templates/
      └── index.html  # Simple Tailwind-based UI
.env
requirements.txt
Dockerfile
README.md
```

---

### ⚙️ Environment Variables

Pass environment variable `DATABASE_URL` with your database connection string:

```bash
DATABASE_URL=postgresql+asyncpg://user:password@host:5432/todo
```

When deployed on NoVPS, use the connection string from your **managed PostgreSQL instance**.

---

### 🧩 Local Setup

**1. Clone the repository:**

```bash
git clone https://github.com/novps/fastapi-sample-app.git
cd fastapi-sample-app
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

**3. Run the app:**

```bash
uvicorn app.main:app --reload
```

**4. Open in browser:**

```
http://localhost:8000
```

Swagger API docs are available at:

```
http://localhost:8000/docs
```

---

### 🐳 Docker Setup

**Build and run locally:**

```bash
docker build -t novps-fastapi-sample-app .
docker run -p 8080:8080 --env-file .env novps-fastapi-sample-app
```

App will be available at `http://localhost:8080`.

---

### 🌩 Deployment on NoVPS

1. Create a **new project** in your NoVPS dashboard.
2. Add a **managed PostgreSQL database**.
3. Create a new **application**:

   * **Container image:** `ghcr.io/novps/fastapi-sample-app:latest`
   * **Environment variables:** `DATABASE_URL` (from your managed DB)
   * **Shell command (optional):**

     ```
     uvicorn app.main:app --host 0.0.0.0 --port 8080
     ```
   * **HTTP port:** `8080`
4. Deploy — and your app will be live in seconds.

---

### 🧠 What This Demo Shows

* How to run **FastAPI** apps on NoVPS
* How to connect to a **managed PostgreSQL** instance
* How to **persist and retrieve** data through async SQLAlchemy
* How to use **environment variables** for configuration
* How to **containerize and deploy** an app using Docker

---

### 🧑‍💻 API Endpoints Overview

| Method   | Endpoint      | Description       |
| -------- | ------------- | ----------------- |
| `GET`    | `/todos`      | List all tasks    |
| `POST`   | `/todos`      | Create new task   |
| `PATCH`  | `/todos/{id}` | Toggle completion |
| `DELETE` | `/todos/{id}` | Delete task       |

---

### 🎨 Frontend Overview

The application includes a minimal **Tailwind CSS** UI available at `/`, featuring:

* A form to add new tasks
* Real-time updates using `fetch()`
* Buttons to mark as done or delete
* Clean responsive layout

---

### 📄 License

This project is released under the **MIT License**.
You’re free to modify and use it as a template for your own NoVPS applications.
