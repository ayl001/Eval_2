from django.contrib import admin
from .models import Utilisateur, Creneau, Competence, Echange

# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Creneau)
admin.site.register(Competence)
admin.site.register(Echange)