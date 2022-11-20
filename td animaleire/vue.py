from appjar import gui
app=gui()
app.addLabel("en-tête", "Bienvenue à l'animalerie !")
app.setLabelBg("en-tête","salmon")
app.setLabelFg("en-tête","white")

app.addLabel("tableau", "Tableau de bord")
app.setLabelBg("tableau","gray")
app.setLabelFg("tableau","white")

import Modèle

liste_animaux=['Tic','Tac','Totoro','Patrick','Pocahontas']

for animal in liste_animaux:
    app.addLabel(animal, "[" + animal + "]" +" État : " + Modèle.lit_état(animal) + "; Lieu : " + Modèle.lit_lieu(animal))
    app.setLabelBg(animal,"lightgray")
    app.setLabelFg(animal,"white")

liste_actions=["nourrir","divertir","coucher","réveiller"]

for animal in liste_animaux:
    app.addRadioButton("animal_id", animal)
for action in liste_actions:
    app.addRadioButton("Actions",action)

import Contrôleur

def press(act):
    if app.getRadioButton("Actions")=="nourrir":
        [texte1,texte2]= Contrôleur.nourrir(app.getRadioButton("animal_id"))
        if texte2==0:
            app.warningBox("", texte1)
        if texte1==0:
            app.infoBox("", texte2)
        actualisation()
        return None
    if app.getRadioButton("Actions") == "divertir":
        [texte1,texte2]= Contrôleur.divertir(app.getRadioButton("animal_id"))
        if texte2==0:
            app.warningBox("", texte1)
        if texte1==0:
            app.infoBox("", texte2)
        actualisation()
        return None
    if app.getRadioButton("Actions") == "coucher":
        [texte1,texte2]= Contrôleur.coucher(app.getRadioButton("animal_id"))
        if texte2==0:
            app.warningBox("", texte1)
        if texte1==0:
            app.infoBox("", texte2)
        actualisation()
        return None
    if app.getRadioButton("Actions") == "réveiller":
        [texte1,texte2]= Contrôleur.réveiller(app.getRadioButton("animal_id"))
        if texte2==0:
            app.warningBox("", texte1)
        if texte1==0:
            app.infoBox("", texte2)
        actualisation()
        return None

def actualisation():
    liste_animaux = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']

    for animal in liste_animaux:
        app.setLabel(animal,
                     "[" + animal + "]" + " État : " + Modèle.lit_état(animal) + "; Lieu : " + Modèle.lit_lieu(animal))
    return None


app.addButton("go",  press)

app.go()
