from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import hash_password, verify_password, create_token
from app.schemas.user import UserRegister, UserLogin

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", status_code=201)
def register(data: UserRegister, db: Session = Depends(get_db)):
    user = User(
        email=data.email,
        username=data.username,
        password=hash_password(data.password),
        role="admin" # temporary
    )
    db.add(user)
    db.commit()
    return {"msg": "User created"}


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user_id": user.id, "role": user.role})
    return {"access_token": token}