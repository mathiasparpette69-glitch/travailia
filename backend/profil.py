from fastapi import APIRouter

router = APIRouter()


@router.post("/profil")
def creer_profil(
    metier: str,
    ville: str,
    competences: str
):
    return {
        "message": "Profil candidat enregistré",
        "metier": metier,
        "ville": ville,
        "competences": competences
    }


@router.get("/profil")
def voir_profil():
    return {
        "message": "Profil candidat JobIA"
    }