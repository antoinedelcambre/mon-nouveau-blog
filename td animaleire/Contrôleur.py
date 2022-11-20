import Modèle

def nourrir(animal_id):
    texte1=0
    texte2=0
    if Modèle.lit_état(animal_id) != 'affamé':
        texte1 = 'Désolé, '+ animal_id + " n'a pas faim !"
        return [texte1,texte2]
    if Modèle.vérifie_disponibilité('mangeoire') == 'occupé':
        texte1 = "Impossible, la mangeoire est actuellement occupée par " + Modèle.cherche_occupant('mangeoire')
        return [texte1,texte2]
    Modèle.change_lieu(animal_id, 'mangeoire')
    Modèle.change_état(animal_id, 'repus')
    texte2 = "Félicitations, " + animal_id + " a rejoint la mangeoire et est maintenant repus."
    return [texte1,texte2]

def divertir(animal_id):
    texte1=0
    texte2=0
    if Modèle.lit_état(animal_id) != 'repus':
        texte1 = 'Désolé, '+ animal_id + " n'est pas en état de faire du sport !"
        return [texte1,texte2]
    if Modèle.vérifie_disponibilité('roue') == 'occupé':
        texte1 = "Impossible, la roue est actuellement occupée par " + Modèle.cherche_occupant('roue')
        return [texte1,texte2]
    Modèle.change_lieu(animal_id, 'roue')
    Modèle.change_état(animal_id, 'fatigué')
    texte2 = "Félicitations, " + animal_id + " a rejoint la roue et est maintenant fatigué."
    return [texte1,texte2]

def coucher(animal_id):
    texte1=0
    texte2=0
    if Modèle.lit_état(animal_id) != 'fatigué':
        texte1 = 'Désolé, ' + animal_id + " n'est pas fatigué !"
        return [texte1,texte2]
    if Modèle.vérifie_disponibilité('nid') == 'occupé':
        texte1 = "Impossible, le nid est actuellement occupée par " + Modèle.cherche_occupant('nid')
        return [texte1,texte2]
    Modèle.change_lieu(animal_id, 'nid')
    Modèle.change_état(animal_id, 'endormi')
    texte2 = "Félicitations, " + animal_id + " a rejoint le nid et est maintenant endormi."
    return [texte1,texte2]

def réveiller(animal_id):
    texte1=0
    texte2=0
    if Modèle.lit_état(animal_id) != 'endormi':
        texte1 = 'Désolé, '+ animal_id + " ne dort pas !"
        return [texte1,texte2]
    Modèle.change_lieu(animal_id, 'litière')
    Modèle.change_état(animal_id, 'affamé')
    texte2 = "Félicitations, " + animal_id + " a rejoint la litière et est maintenant affamé."
    return [texte1,texte2]