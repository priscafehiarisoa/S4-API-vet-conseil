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
from globale.models import Client
from globale.models import Patient

# Create your views here.
# def test(request):
#     return render(request, 'admin/index.html', {})


#patient
def liste_patient(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'admin/patient/liste.html', context)
def form_insert_patient(request):
    context={'cients':Client.objects.all()}
    return render(request,'admin/patient/insertion.html',context)

def save_patient(request):
    patient=Patient()
    patient.nom=request.POST['nom']
    patient.proprietaire=request.POST['proprietaire']
    patient.nature=request.POST['nature']
    patient.age=request.POST['age']
    patient.save()
    return redirect('liste_patient')

def modify_patient(request,idPatient):
    patient=Patient.get_object_or_404(Patient, id=idPatient)
    if(request.method=='POST'):
        patient.nom = request.POST['nom']
        patient.proprietaire = request.POST['proprietaire']
        patient.nature = request.POST['nature']
        patient.age = request.POST['age']
        patient.save()
        return redirect('liste_patient')
    else:
        return render(request, 'admin/patient/insertion.html', {'patient1': patient})

def delete_patient(request,idPatient):
    Patient.get_object_or_404(Patient, id=idPatient).delete()
    return redirect('liste_patient')


#client
def form_insert_client(request):
    return render(request,'admin/client/insertion.html',{})

def select_client(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'admin/client/liste.html', context)

def save_client(request):
    context = {
        'saved': 'vita',
    }
    client=Client(nom=request.POST['nom'],prenom=request.POST['prenom'],adresse=request.POST['adresse'],mail=request.POST['mail'],contact=request.POST['contact'],facebook=request.POST['facebook'])
    client.save()
    return redirect('liste_client')

def modify_client(request,idClient):
    client = get_object_or_404(Client, id=idClient)
    if request.method == 'POST':
        client.nom=request.POST['nom']
        client.prenom=request.POST['prenom']
        client.adresse=request.POST['mail']
        client.mail=request.POST['mail']
        client.contact=request.POST['contact']
        client.facebook=request.POST['facebook']
        client.save()
        return redirect('liste_client')
    else:
        return render(request, 'admin/client/insertion.html', {'client1': client})


def delete_client(request,idClient):
    client = Client.objects.get(id=idClient).delete()
    return redirect('liste_client')

#race
def form_insert_race(request):
    return render(request,'admin/insert_race.html',{})
def save_race(request):
    race=Race(designation=request.POST['designation'])
    race.save()
    return redirect('liste_race')




def list_race(request):
    liste=Race.objects.all()
    return render(request, 'admin/liste_race.html', {'races':liste})

def modify_race(request,idRace):
    race = get_object_or_404(Race, id=idRace)
    if request.method == 'POST':
        race.designation=request.POST['designation']
        race.save()
        return redirect('liste_race')
    else:
        return render(request,'admin/insert_race.html',{'race1':race})


def delete_race(request,idRace):
    Race.objects.get(id=idRace).delete()
    return redirect('liste_race')

#POSTE

def form_insert_poste(request):
    p=PosteForm()
    return render(request,'admin/insert_poste.html',{'forms':p})

def save_poste(request):
    formulaire=PosteForm(request.POST)
    poste=Poste()
    poste.designation=formulaire['designation'].value()
    poste.rang=formulaire['rang'].value()
    poste.save()
    return redirect('liste_poste')

def liste_poste(request):
    liste_poste = Poste.objects.all()
    context = {'postes' : liste_poste}
    return render(request, 'admin/liste_poste.html', context)

def delete_poste(request, idPoste):
    Poste.objects.get(id=idPoste).delete()
    return redirect('liste_poste')


def detail_poste(request, idPoste):
    poste = Poste.objects.get(id=idPoste)
    return render(request,'admin/detail_poste.html', {'poste': poste})

def modify_poste(request, idPoste):
    poste = get_object_or_404(Poste, id=idPoste)
    if request.method == 'POST':
        form = PosteForm(request.POST, instance=poste)
        if form.is_valid():
            form.save()
            return redirect('liste_poste')
    else:
        form = PosteForm(instance=poste)
    return render(request, 'admin/insert_poste.html',{'form': form, 'poste1': poste})
    

# PERSONNEL
def form_insert_personnel(request):
    liste_poste = Poste.objects.all()
    context = {'postes' : liste_poste}
    return render(request,'admin/insert_personnel.html',context)

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
    return render(request, 'admin/insert_login.html', context)

def liste_personnel(request):
    liste_personnel = Personnel.objects.all()
    context = {'personnels' : liste_personnel}
    return render(request, 'admin/liste_personnel.html', context)

def delete_personnel(request, idPersonnel):
    Personnel.objects.get(id=idPersonnel).delete()
    liste_personnel = Personnel.objects.all()
    context = {'personnels' : liste_personnel}
    return render(request, 'admin/liste_personnel.html', context)

def detail_personnel(request, idPersonnel):
    personnel = Personnel.objects.get(id=idPersonnel)
    return render(request,'admin/detail_personnel.html', {'personnel': personnel})

def modify_personnel(request, idPersonnel):
    personnel = get_object_or_404(Personnel, id=idPersonnel)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail_personnel', args=[idPersonnel]))
    else:
        form = PersonnelForm(instance=personnel)
    return render(request, 'admin/modify_personnel.html',{'form': form, 'personnel': personnel})


#LOGIN

def save_login(request):
    idPersonnel=request.POST['idPersonnel'] 
    personnel = Personnel.objects.get(pk=idPersonnel) 
    email=request.POST['email']
    password=request.POST['password']
    login = Login(mail = email, mot_de_passe = password, personnel = personnel)
    login.save()
    return redirect('admin/index')
