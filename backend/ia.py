from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class DemandeAnalyse(BaseModel):
    metier: str
    ville: str
    competences: str


@router.post("/analyse")
def analyser_profil(demande: DemandeAnalyse):

    resultat = {
        "metier_recommande": demande.metier,
        "ville": demande.ville,
        "analyse": f"Votre profil correspond à des opportunités dans le domaine {demande.metier}.",
        "conseil": f"Mettez en avant vos compétences : {demande.competences}",
        "lettre_motivation": f"""
Madame, Monsieur,

Je souhaite vous proposer ma candidature dans le domaine de {demande.metier}.
Mes compétences en {demande.competences} correspondent aux besoins de votre entreprise.

Je serais ravi de pouvoir échanger avec vous.

Cordialement.
"""
    }

    return resultat