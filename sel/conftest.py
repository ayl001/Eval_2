import sys
import os

# Ajoute la racine du projet Django au PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
print("Je suis conftest, je suis bien là et je suis chargé")
