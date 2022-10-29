from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.ajout_affiche, name="ajoutafficheEtudiant"),
    path('delete/<int:id>',views.supprimer_etudiant, name="suppressionEtudiant"),
    path('<int:id>',views.modifier_etudiant, name="modifierEtudiant")
]