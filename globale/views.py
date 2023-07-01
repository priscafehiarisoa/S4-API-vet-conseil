from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render,get_object_or_404
# from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from globale.form import PosteForm
from globale.form import PersonnelForm
from globale.models import Race
from globale.models import Poste
from globale.models import Personnel
from globale.models import Login


# Create your views here.
def test(request):
    return render(request, 'index.html', {})

def form_insert_race(request):
    context={
        'id':1,
    }
    return render(request,'insert_race.html',context)

def save_race(request):
    context = {
        'saved': 'vita',
    }
    race=Race(designation=request.POST['designation'])
    race.save()
    return render(request, 'insert_race.html', context)

#POSTE

def form_insert_poste(request):
    return render(request,'insert_poste.html',{})

def save_poste(request):
    poste=Poste(designation=request.POST['designation'])
    poste.save()
    return redirect('index')

def liste_poste(request):
    liste_poste = Poste.objects.all()
    context = {'postes' : liste_poste}
    return render(request, 'liste_poste.html', context)

def delete_poste(request, idPoste):
    Poste.objects.get(id=idPoste).delete()
    liste_poste = Poste.objects.all()
    context = {'postes' : liste_poste}
    return render(request, 'liste_poste.html', context)   

def detail_poste(request, idPoste):
    poste = Poste.objects.get(id=idPoste)
    return render(request,'detail_poste.html', {'poste': poste})

def modify_poste(request, idPoste):
    poste = get_object_or_404(Poste, id=idPoste)
    if request.method == 'POST':
        form = PosteForm(request.POST, instance=poste)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail_poste', args=[idPoste]))
    else:
        form = PosteForm(instance=poste)
    return render(request, 'modify_poste.html',{'form': form, 'poste': poste})
    

# PERSONNEL
def form_insert_personnel(request):
    liste_poste = Poste.objects.all()
    context = {'postes' : liste_poste}
    return render(request,'insert_personnel.html',context)

def save_personnel(request):
    nom=request.POST['nom']
    prenom=request.POST['prenom']
    adresse=request.POST['adresse']
    contact=request.POST['contact']
    id_poste=request.POST['poste']
    poste = Poste.objects.get(pk=id_poste) 
    personnel = Personnel(nom = nom, prenom = prenom, adresse = adresse, contact = contact, poste = poste)
    personnel.save()
    idpersonnelSaver = personnel.id
    context = {'idPersonnel':idpersonnelSaver}
    return render(request, 'insert_login.html', context)

def liste_personnel(request):
    liste_personnel = Personnel.objects.all()
    context = {'personnels' : liste_personnel}
    return render(request, 'liste_personnel.html', context)

def delete_personnel(request, idPersonnel):
    Personnel.objects.get(id=idPersonnel).delete()
    liste_personnel = Personnel.objects.all()
    context = {'personnels' : liste_personnel}
    return render(request, 'liste_personnel.html', context) 

def detail_personnel(request, idPersonnel):
    personnel = Personnel.objects.get(id=idPersonnel)
    return render(request,'detail_personnel.html', {'personnel': personnel})

def modify_personnel(request, idPersonnel):
    personnel = get_object_or_404(Personnel, id=idPersonnel)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail_personnel', args=[idPersonnel]))
    else:
        form = PersonnelForm(instance=personnel)
    return render(request, 'modify_personnel.html',{'form': form, 'personnel': personnel})


#LOGIN

def save_login(request):
    idPersonnel=request.POST['idPersonnel'] 
    personnel = Personnel.objects.get(pk=idPersonnel) 
    email=request.POST['email']
    password=request.POST['password']
    login = Login(mail = email, mot_de_passe = password, personnel = personnel)
    login.save()
    return redirect('index')
