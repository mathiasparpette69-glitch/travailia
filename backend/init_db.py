from database import engine, Base
import models


print("Création de la base de données JobIA...")


Base.metadata.create_all(bind=engine)


print("Base de données créée avec succès 🚀")