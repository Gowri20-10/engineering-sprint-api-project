from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def require_role(required_role: str):
    def role_dependency(token: str = Depends(oauth2_scheme)):
        payload = decode_token(token)
        if payload.get("role") != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return payload
    return role_dependency
