from sqlalchemy import Column, Integer, String
from database import Base


class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String, unique=True)
    mot_de_passe = Column(String)


class Profil(Base):
    __tablename__ = "profils"

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer)
    metier = Column(String)
    ville = Column(String)
    competences = Column(String)
    cv = Column(String)


class Candidature(Base):
    __tablename__ = "candidatures"

    id = Column(Integer, primary_key=True)
    entreprise = Column(String)
    poste = Column(String)
    statut = Column(String)