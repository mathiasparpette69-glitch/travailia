from fastapi import APIRouter

router = APIRouter()


@router.get("/cv")
def cv():
    return {
        "message": "Gestion du CV candidat JobIA"
    }