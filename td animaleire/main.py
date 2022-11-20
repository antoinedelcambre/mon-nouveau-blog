import Modèle

def test_lit_etat():
    assert Modèle.lit_état('Tac') == 'affamé'

test_lit_etat()

def test_lit_etat_nul():
    assert Modèle.lit_état('Bob') == None

test_lit_etat_nul()

def test_lit_lieu():
    assert Modèle.lit_lieu('Tac') == 'litière'

test_lit_lieu()

def test_lit_lieu_nul():
    assert Modèle.lit_lieu('Bob') == None

test_lit_lieu_nul()

def test_vérifie_disponibilité():
    assert Modèle.vérifie_disponibilité('litière') == 'libre'
    assert Modèle.vérifie_disponibilité('nid') == 'occupé'

test_vérifie_disponibilité()

def test_vérifie_disponibilité_nul():
    assert Modèle.vérifie_disponibilité('nintendo') == None

test_vérifie_disponibilité_nul()

def test_cherche_occupant():
    assert Modèle.cherche_occupant('nid') == ['Pocahontas']
    assert 'Tac' in Modèle.cherche_occupant('litière')
    assert 'Tac' not in Modèle.cherche_occupant('mangeoire')

test_cherche_occupant()

def test_cherche_occupant_nul():
    assert Modèle.cherche_occupant('casino') == None

test_cherche_occupant_nul()

def test_change_état():
    Modèle.change_état('Totoro', 'fatigué')
    assert Modèle.lit_état('Totoro') == 'fatigué'
    Modèle.change_état('Totoro', 'excité comme un pou')
    assert Modèle.lit_état('Totoro') == 'fatigué'
    Modèle.change_état('Bob', 'fatigué')
    assert Modèle.lit_état('Bob') == None

test_change_état()

def test_change_lieu():
    Modèle.change_lieu('Totoro', 'roue')
    assert Modèle.lit_lieu('Totoro') == 'roue'
    assert Modèle.vérifie_disponibilité('litière') == 'libre'
    assert Modèle.vérifie_disponibilité('roue') == 'occupé'

test_change_lieu()

import Contrôleur


def test_nourrir():
    if Modèle.vérifie_disponibilité('mangeoire') == 'libre' and Modèle.lit_état('Tic') == 'affamé':
        Contrôleur.nourrir('Tic')
    assert Modèle.vérifie_disponibilité('mangeoire') == 'occupé'
    assert Modèle.lit_état('Tic') == 'repus'
    assert Modèle.lit_lieu('Tic') == 'mangeoire'
    Contrôleur.nourrir('Tac')
    assert Modèle.lit_état('Tac') == 'affamé'
    assert Modèle.lit_lieu('Tac') == 'litière'
    Contrôleur.nourrir('Pocahontas')
    assert Modèle.lit_état('Pocahontas') == 'endormi'
    assert Modèle.lit_lieu('Pocahontas') == 'nid'
    Contrôleur.nourrir('Bob')
    assert Modèle.lit_état('Bob') == None
    assert Modèle.lit_lieu('Bob') == None
    assert Modèle.vérifie_disponibilité('mangeoire') == 'occupé'

test_nourrir()


