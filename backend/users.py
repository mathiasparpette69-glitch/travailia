from fastapi import APIRouter

router = APIRouter()


@router.get("/utilisateur")
def utilisateur():
    return {
        "message": "Gestion des utilisateurs JobIA"
    }