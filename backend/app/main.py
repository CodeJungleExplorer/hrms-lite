from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.employees import router as employee_router
from app.routes.attendance import router as attendance_router

app = FastAPI(
    title="HRMS Lite API",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# ✅ CORS – production safe (Vercel + Render)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
