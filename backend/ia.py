from fastapi import APIRouter

router = APIRouter()


@router.post("/analyse-cv")
def analyser_cv(
    texte_cv: str
):
    return {
        "message": "Analyse du CV terminée",
        "competences_detectees": [
            "Communication",
            "Travail en équipe"
        ],
        "profil": texte_cv
    }


@router.get("/recommandations")
def recommandations():
    return {
        "metiers": [
            "Technicien",
            "Employé polyvalent",
            "Assistant"
        ],
        "message": "Métiers suggérés selon le profil"
    }