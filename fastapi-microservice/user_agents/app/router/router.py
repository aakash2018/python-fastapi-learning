from fastapi import APIRouter


router = APIRouter(prefix="/useragent", tags=["User-agent"])


@router.get("/")
def get_agents():
    return {"useragents": ["wheater app", "baby name generator"]}
