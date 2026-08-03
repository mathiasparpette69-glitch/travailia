from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Candidature(BaseModel):
    entreprise: str
    poste: str


candidatures = []


@router.post("/candidature")
def creer_candidature(candidature: Candidature):

    nouvelle = {
        "entreprise": candidature.entreprise,
        "poste": candidature.poste,
        "statut": "En préparation"
    }

    candidatures.append(nouvelle)

    return {
        "message": "Candidature créée ✅",
        "candidature": nouvelle
    }


@router.get("/candidatures")
def liste_candidatures():

    return {
        "candidatures": candidatures
    }


@router.post("/generer-email")
def generer_email(candidature: Candidature):

    return {
        "objet": f"Candidature pour le poste de {candidature.poste}",
        "message": f"""Bonjour,

Je souhaite vous proposer ma candidature pour le poste de {candidature.poste} au sein de votre entreprise {candidature.entreprise}.

Je reste à votre disposition pour un entretien.

Cordialement."""
    }