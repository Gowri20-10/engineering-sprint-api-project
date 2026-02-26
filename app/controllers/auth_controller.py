from fastapi import APIRouter
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login():
    token = create_access_token({
        "user_id": 1,
        "role": "admin"
    })
    return {"access_token": token}
