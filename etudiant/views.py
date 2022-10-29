from cmath import pi
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import EtudiantRegistration
from .models import User

# Create your views here.

#cette fonction permet de creer et d'afficher un etudiant
def ajout_affiche(request):
    if request.method == 'POST':
         fm =EtudiantRegistration(request.POST)
         if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg =User(name= nm, email=em, password=pw)
            reg.save()
            fm.save()
    else:
        fm = EtudiantRegistration()
    etu =User.objects.all()
    return render(request, 'etudiant/ajoutafficheEtudiant.html', {'form':fm , 'etudiant':etu})

#fonction pour la suppression d'etuidant
def supprimer_etudiant(request, id):
    if request.method == 'POST':
        sup =User.objects.get(pk = id)
        sup.delete()
        return HttpResponseRedirect('/')

#fonction pour modifier les informations de l'etudiant
def modifier_etudiant(request, id):
    if request.method=='POST':
        mod =User.objects.get(pk = id)
        fm = EtudiantRegistration(request.POST, instance=mod)
        if fm.is_valid():
            fm.save()
    else:
         mod = User.objects.get(pk = id)
    fm = EtudiantRegistration(request.POST, instance=mod)
    return render(request, 'etudiant/updateEtudiant.html', {'form': fm})
