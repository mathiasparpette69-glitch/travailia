from fastapi import FastAPI

from users import router as users_router
from profil import router as profil_router
from cv import router as cv_router
from ia import router as ia_router
from candidatures import router as candidatures_router


app = FastAPI(
    title="JobIA",
    description="Assistant IA de recherche d'emploi",
    version="0.1"
)


app.include_router(users_router)
app.include_router(profil_router)
app.include_router(cv_router)
app.include_router(ia_router)
app.include_router(candidatures_router)


@app.get("/")
def accueil():
    return {
        "message": "Bienvenue sur JobIA 🚀"
    }