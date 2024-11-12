from django.db import models
# Create your models here.
from typing import List

class Utilisateur:
    id: int
    nom: str
    prenom: str
    email: str
    def afficher_competences -> List[Competence]:

    def indique disponibilite(c: Creneau) -> bool:

class Competence
    id: int
    nom: str
    def afficher(self) -> str:

class Creneau
    id: int
    date: Date
class echange()
    id: int
    competence: Competence
    creneau: Creneau
    def afficher_details() -> str:

