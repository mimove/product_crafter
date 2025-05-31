from fastapi import APIRouter, FastAPI, Request, Response

router = APIRouter()

@router.get("/health")
def read_root():
    return {"detail": "ok"}