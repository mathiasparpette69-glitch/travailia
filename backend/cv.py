from fastapi import APIRouter, UploadFile, File

router = APIRouter()

cv_actuel = {}


@router.post("/cv")
async def ajouter_cv(fichier: UploadFile = File(...)):

    global cv_actuel

    contenu = await fichier.read()

    cv_actuel = {
        "nom_fichier": fichier.filename,
        "taille": len(contenu)
    }

    return {
        "message": "CV reçu avec succès ✅",
        "cv": cv_actuel
    }


@router.get("/cv")
def voir_cv():

    return cv_actuel