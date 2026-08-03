from fastapi import APIRouter

router = APIRouter()


@router.get("/analyse-cv")
def analyse_cv():
    return {
        "message": "Analyse du CV par l'intelligence artificielle en préparation"
    }


@router.get("/suggestions")
def suggestions():
    return {
        "message": "Recherche de métiers et d'entreprises adaptée au profil"
    }