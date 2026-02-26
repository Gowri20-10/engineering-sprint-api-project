from fastapi import APIRouter, Depends
from app.services.ai_service import generate_summary
from app.utils.role_checker import require_role

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/summarize")
def summarize(data: dict, user=Depends(require_role("admin"))):
    result = generate_summary(data.get("task_description"))
    return {"summary": result}
