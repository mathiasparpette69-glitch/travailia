from fastapi import APIRouter

router = APIRouter()


@router.post("/candidature")
def creer_candidature(
    entreprise: str,
    poste: str
):
    return {
        "message": "Candidature créée",
        "entreprise": entreprise,
        "poste": poste,
        "statut": "En préparation"
    }


@router.get("/candidatures")
def liste_candidatures():
    return {
        "candidatures": [
            {
                "entreprise": "Exemple Entreprise",
                "statut": "En attente"
            }
        ]
    }


@router.post("/generer-email")
def generer_email(
    entreprise: str,
    poste: str
):
    return {
        "objet": f"Candidature pour le poste de {poste}",
        "message": f"Bonjour {entreprise}, je vous contacte pour proposer ma candidature."
    }