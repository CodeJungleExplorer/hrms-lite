from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import get_db
from app.routes.employees import router as employee_router
from app.routes.attendance import router as attendance_router

app = FastAPI(title="HRMS Lite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee_router)
app.include_router(attendance_router)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "HRMS Lite backend is running"
    }
@app.get("/db-check")
def db_check():
    try:
        db = get_db()
        collections = db.list_collection_names()
        return {
            "status": "success",
            "message": "MongoDB connected successfully",
            "collections": collections
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }