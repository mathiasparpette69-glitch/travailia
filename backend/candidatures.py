from fastapi import APIRouter

router = APIRouter()


@router.get("/candidatures")
def candidatures():
    return {
        "message": "Gestion des candidatures JobIA"
    }


@router.get("/email")
def email_candidature():
    return {
        "message": "Création d'un email de candidature personnalisé"
    }