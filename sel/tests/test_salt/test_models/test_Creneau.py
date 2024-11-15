import pytest
from salt.models import Creneau
# test_Creneau

@pytest.mark.django_db
def test_reserver():

    rv = Creneau()
    rv.date = "2024-12-24"
    rv.disponible = False

    assert not rv.reserver()

    rv = Creneau()
    rv.date = "2024-12-31"
    rv.disponible = True

    assert rv.reserver()
    assert not rv.disponible
