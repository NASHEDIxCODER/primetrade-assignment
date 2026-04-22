from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.tasks import router as tasks_router


from app.db.session import Base, engine
from app.models import user, task

from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Primetrade Assignment API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(tasks_router, prefix="/api/v1/tasks", tags=["Tasks"])


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"msg": "API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error"}
    )