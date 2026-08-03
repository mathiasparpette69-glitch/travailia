from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/cv")
def ajouter_cv(
    fichier: UploadFile = File(...)
):
    return {
        "message": "CV reçu avec succès",
        "nom_fichier": fichier.filename
    }


@router.get("/cv")
def voir_cv():
    return {
        "message": "CV du candidat JobIA"
    }