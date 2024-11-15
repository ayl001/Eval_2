import pytest
from salt.models import Competence

# Test compétence
	# test chaîne
def test_competence():
    
    c = Competence()

    c.nom = "Test_Non_Random"
    attendu = "Test_Non_Random"

    assert str(c) == attendu

