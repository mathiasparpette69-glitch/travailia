from fastapi import FastAPI

app = FastAPI(
    title="JobIA",
    description="Assistant IA de recherche d'emploi",
    version="0.1"
)

@app.get("/")
def accueil():
    return {
        "message": "Bienvenue sur JobIA 🚀"
    }