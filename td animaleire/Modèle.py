import json

def lit_état(animal_id):
    with open('animal.json', "r") as f:
        animal=json.load(f)
    if animal_id in animal :
        return animal[animal_id]['ETAT']
    else :
        print("Désolé,", animal_id, "n'est pas un animal connu")
        return None

def lit_lieu(animal_id):
    with open('animal.json', "r") as f :
        animal=json.load(f)
    if animal_id in animal :
      return animal[animal_id]['LIEU']
    else :
        print ("Désolé,",animal_id,"n'est pas un animal connu")
        return None

def vérifie_disponibilité(équipement_id):
    with open('Équipement.json', "r") as f :
        équipement=json.load(f)
    if équipement_id in équipement:
        return équipement[équipement_id]['DISPONIBILITÉ']
    else :
        print("Désolé,", équipement_id, "n'est pas un équipement connu")
        return None

def cherche_occupant(lieu):
    liste_occupant=""
    with open('animal.json', "r") as f :
        animal=json.load(f)
    with open('Équipement.json', "r") as f :
        équipement=json.load(f)
    if lieu in équipement:
        for animal_id in animal :
            if animal[animal_id]["LIEU"]==lieu:
                liste_occupant = liste_occupant+", " + animal_id
        return liste_occupant
    else :
        print("Désolé,", lieu, "n'est pas un lieu connu")
        return None

def change_état(animal_id, etat):
    with open('animal.json', "r") as f:
        animal = json.load(f)
    if animal_id not in animal:
        print("Désolé,", animal_id, "n'est pas un animal connu.")
        return None
    if etat not in ['affamé', 'fatigué', 'repus', 'endormi']:
        print("Désolé,", etat, "n'est pas un état connu.")
        return None
    else:
        animal[animal_id]['ETAT'] = etat
        json.dump(animal, open("animal.json", "w"), indent=4)

def change_lieu(animal_id, lieu):
    with open('animal.json', "r") as f:
        animal = json.load(f)
    with open('Équipement.json', "r") as g:
        équipement = json.load(g)
    if animal_id not in animal:
        print("Désolé,", animal_id, "n'est pas un animal connu.")
        return None
    if lieu not in équipement:
        print("Désolé,", lieu, "n'est pas un état connu.")
        return None
    ancien_lieu = animal[animal_id]['LIEU']
    if lieu=='litière':
        équipement[ancien_lieu]['DISPONIBILITÉ'] = 'libre'
        animal[animal_id]['LIEU'] = lieu
        json.dump(animal, open("animal.json", "w"), indent=4)
        json.dump(équipement, open("Équipement.json", "w"), indent=4)
    if vérifie_disponibilité(lieu)=='libre' :
        équipement[ancien_lieu]['DISPONIBILITÉ'] = 'libre'
        animal[animal_id]['LIEU'] = lieu
        json.dump(animal, open("animal.json", "w"), indent=4)
        équipement[lieu]['DISPONIBILITÉ']= 'occupé'
        json.dump(équipement, open("Équipement.json", "w"), indent=4)
    else :
        print ("Désolé,", lieu, "est déjà occupé")
        return None

