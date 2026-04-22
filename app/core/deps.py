from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
from app.db.session import SessionLocal
from app.models.user import User

security = HTTPBearer()
SECRET_KEY = "supersecret"


def get_current_user(token=Depends(security)):
    db = SessionLocal()
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=["HS256"])
        user = db.query(User).get(payload["user_id"])
        return user
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    
def get_current_admin(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail ="Admin only")