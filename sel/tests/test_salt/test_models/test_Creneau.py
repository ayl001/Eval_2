from sel.salt.models import Creneau
# test_Creneau

def test_reserver():

    rv = Creneau()
    rv.date = "25/12/2024"
    rv.disponible = False

    assert not rv.reserver()

    rv = Creneau()
    rv.date = "31/12/2024"
    rv.disponible = True

    assert rv.reserver()
    assert not rv.disponible
