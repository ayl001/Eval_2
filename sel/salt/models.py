from django.db import models
from django.contrib.auth.models import User
from typing import List, Optional


class Competence(models.Model):
    nom: str = models.CharField(max_length=100, unique=True)

    def afficher(self) -> str:
        return self.nom

    def __str__(self) -> str:
        return self.nom


class Creneau(models.Model):
    date: str = models.DateField()
    disponible: bool = models.BooleanField(default=True)

    def reserver(self) -> bool:
        if self.disponible:
            self.disponible = False
            self.save()
            return True
        return False

    def __str__(self) -> str:
        return f"Créneau du {self.date} - {'Disponible' if self.disponible else 'Réservé'}"


class Utilisateur(models.Model):
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    nom: str = models.CharField(max_length=50)
    prenom: str = models.CharField(max_length=50)
    email: str = models.EmailField(unique=True)

    competences = models.ManyToManyField(Competence, related_name="utilisateurs", blank=True)
    creneaux = models.ManyToManyField(Creneau, related_name="utilisateurs_disponibles", blank=True)

    def afficher_competences(self) -> List[str]:
        return [competence.nom for competence in self.competences.all()]

    def indique_disponibilite(self, creneau: Creneau) -> bool:
        return self.creneaux.filter(id=creneau.pk).exists()

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom}"


class Echange(models.Model):
    competence: Competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    creneau: Creneau = models.ForeignKey(Creneau, on_delete=models.CASCADE)
    utilisateur: Utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def afficher_details(self) -> str:
        return f"Echange de {self.competence.nom} avec {self.utilisateur} le {self.creneau.date}"

    def __str__(self) -> str:
        return f"Echange {self.competence.nom} le {self.creneau.date} avec {self.utilisateur}"
