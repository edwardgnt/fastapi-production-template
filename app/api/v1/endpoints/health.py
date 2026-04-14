from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def helth_check():
    return {"status": "ok",
            "message": "API is healthy", "service": "fastapi-production-template"}