from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Animal, Equipement
import copy

# Create your views here.
def animal_list(request):
    animals = Animal.objects.filter()
    return render(request, 'blog/animal_list.html', {'animals': animals})


def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    lieu = get_object_or_404(Equipement, id_equip=animal.lieu)
    message = ''
    ancien_lieu = copy.deepcopy(lieu)
    if request.method == "POST" :
        form = MoveForm(request.POST, instance=animal)
    else :
        form = MoveForm()
    if form.is_valid():
        form.save(commit=False)
        if animal.lieu.disponibilite == 'libre' :
            if animal.etat == 'fatigué' and animal.lieu.id_equip=='nid' :
                animal.etat = 'endormi'
                animal.save()
                ancien_lieu.disponibilite = "libre"
                ancien_lieu.save()
                nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
                nouveau_lieu.disponibilite = "occupé"
                nouveau_lieu.save()
                return redirect('animal_detail', id_animal=id_animal)
            if animal.etat == 'affamé' and animal.lieu.id_equip == 'mangeoire':
                animal.etat = 'repus'
                animal.save()
                ancien_lieu.disponibilite = "libre"
                ancien_lieu.save()
                nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
                nouveau_lieu.disponibilite = "occupé"
                nouveau_lieu.save()
                return redirect('animal_detail', id_animal=id_animal)
            if animal.etat == 'repus' and animal.lieu.id_equip=='roue' :
                animal.etat = 'fatigué'
                animal.save()
                ancien_lieu.disponibilite = "libre"
                ancien_lieu.save()
                nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
                nouveau_lieu.disponibilite = "occupé"
                nouveau_lieu.save()
                return redirect('animal_detail', id_animal=id_animal)
            if animal.etat == 'endormi' and animal.lieu.id_equip=='litière' :
                animal.etat = 'affamé'
                animal.save()
                ancien_lieu.disponibilite = "libre"
                ancien_lieu.save()
                nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
                nouveau_lieu.disponibilite = "libre"
                nouveau_lieu.save()
                return redirect('animal_detail', id_animal=id_animal)
            else:
                message="Activité impossible compte tenu de l'état de l'animal"
                return render(request,
                              'blog/animal_detail.html',
                              {'animal': animal, 'lieu': lieu, 'form': form, 'message': message})
        else :
            message="Lieu déjà occupé"
            return render(request,
                  'blog/animal_detail.html',
                  {'animal': animal, 'lieu': lieu, 'form': form, 'message': message})
    else:
        form = MoveForm()
        return render(request,
                  'blog/animal_detail.html',
                  {'animal': animal, 'lieu': lieu, 'form': form, 'message': message})
