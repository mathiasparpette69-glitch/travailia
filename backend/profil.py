from fastapi import APIRouter

router = APIRouter()


@router.get("/profil")
def profil():
    return {
        "nom": "Utilisateur",
        "message": "Profil candidat JobIA créé"
    }