from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Utilisateur(BaseModel):
    nom: str
    email: str


utilisateur_actuel = {}


@router.post("/utilisateur")
def creer_utilisateur(utilisateur: Utilisateur):

    global utilisateur_actuel

    utilisateur_actuel = utilisateur.dict()

    return {
        "message": "Utilisateur créé avec succès ✅",
        "utilisateur": utilisateur_actuel
    }


@router.get("/utilisateur")
def voir_utilisateur():

    return utilisateur_actuel