from django.http import HttpResponse
from django.db import models

from .models import Creneau, Utilisateur, Competence

# Create your views here.

def index(request):
    for personne in Utilisateur.objects.all(): # On n'affiche pas les caractéristique de la personne
        creneaux = personne.creneaux.all()
        talents = personne.afficher_competences()
        output = ""
        for cr in creneaux:
            output = output + cr.__str__()
            for comp in talents:
                output = output + ", " + comp.__str__()
            output = output + "<br>"
    return HttpResponse(output)

