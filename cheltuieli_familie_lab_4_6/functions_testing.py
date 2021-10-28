from functions import *

def test_validare_tip_cheltuiala():

"""Testeaza functia validare_tip_cheltuiala"""

    assert validare_tip_cheltuiala('mancare') == 'mancare'
    assert validare_tip_cheltuiala('altele') == 'altele'
    assert validare_tip_cheltuiala('imbracaminte') == 'imbracaminte'
    assert validare_tip_cheltuiala('telefon') == 'telefon'

test_validare_tip_cheltuiala()


def test_validare_optiune_submeniu():
    """Testeaza functia validare_optiune_submeniu"""

    assert validare_optiune_submeniu('a') == 'a'
    assert validare_optiune_submeniu('b') == 'b'
    assert validare_optiune_submeniu('c') == 'c'

test_validare_optiune_submeniu()
