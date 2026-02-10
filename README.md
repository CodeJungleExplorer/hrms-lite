# HRMS Lite – Full Stack Application

HRMS Lite is a lightweight, production-ready Human Resource Management System built as a full-stack web application.  
The system allows an admin to manage employee records and track daily attendance through a clean, professional interface.

This project was developed as part of a full-stack coding assessment, focusing on clean architecture, usability, and deployment readiness rather than excessive features.

---

## 🔹 Features

### Employee Management
- Add new employees
- View all employees
- Delete employees
- Duplicate employee ID and email validation

### Attendance Management
- Mark daily attendance (Present / Absent)
- View attendance records per employee
- Prevent duplicate attendance for the same date

### Dashboard
- System health check
- Total employee count
- Module status overview

---

## 🛠 Tech Stack

### Frontend
- React (Vite)
- Tailwind CSS (v3 – stable)
- Axios
- React Router DOM

### Backend
- Python
- FastAPI
- MongoDB (PyMongo)

### Database
- MongoDB (Local / MongoDB Atlas)

### Deployment
- Backend: Render
- Frontend: Vercel

---


---

## 📌 Why Some Folders Are Currently Empty

This project intentionally avoids over-engineering.  
Certain folders are included to demonstrate **scalability and clean architecture**, even though the current scope does not require them.

### Backend
- `utils/`: Designed for reusable helpers (error handling, validation logic).
- `tests/`: Contains basic API tests; can be expanded for full coverage.
- `models/`: Keeps MongoDB collection references isolated from logic.

### Frontend
- `components/employees/` & `components/attendance/`  
  Reserved for breaking large pages into smaller reusable components as the UI grows.
- `context/`  
  Can be used in future for authentication, global user state, or shared app state.
- `hooks/`  
  Intended for custom hooks such as data fetching or reusable logic.
- `styles/`  
  Reserved for shared styles if the project expands beyond utility-first Tailwind usage.

Keeping these folders minimal ensures clarity while still following production-ready structure.

---

## ⚙️ Running the Project Locally


```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
Backend runs at:
http://127.0.0.1:8000

### Frontend
```bash
cd frontend
npm install
npm run dev
Frontend runs at:
http://localhost:5173
