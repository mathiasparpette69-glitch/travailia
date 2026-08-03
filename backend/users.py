from fastapi import APIRouter

router = APIRouter()


@router.post("/utilisateur")
def creer_utilisateur(
    nom: str,
    email: str
):
    return {
        "message": "Utilisateur créé avec succès",
        "nom": nom,
        "email": email
    }


@router.get("/utilisateur")
def voir_utilisateur():
    return {
        "message": "Liste des utilisateurs JobIA"
    }