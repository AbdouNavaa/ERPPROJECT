from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
# from typing import Type
from .models import *
from .forms import ClientForm, FourForm, FactFormCl, FactFormFr, PieceForm, PaiementForm, NoteForm, ProductForm, deviseForm,JournauxForm, immobForm, planForm,Paiement_Fr_Form, taxeForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
# from . import form

from django.shortcuts import render
import matplotlib.pyplot as plt

# GFC
def factures_graphique(request):
    factures = FactureCl.objects.all()
    montants = [facture.total for facture in factures]
    noms_factures = [facture.code for facture in factures]
    plt.bar(noms_factures, montants)
    plt.xlabel('Noms de factures')
    plt.ylabel('Montants totaux')
    plt.title('Montants totaux des factures')
    plt.savefig('factures_graphique.png')
    plt.show()
    return render(request, 'index.html')

# Paiements
def paiements_graphique(request):
    paies = Paiements.objects.all()
    montants = [paie.montant for paie in paies]
    noms_paies = [paie.code for paie in paies]
    plt.bar(noms_paies, montants)
    plt.xlabel('Noms de paies')
    plt.ylabel('Montants totaux')
    plt.title('Montants totaux des paies')
    plt.savefig('paies_graphique.png')
    plt.show()
    return render(request, 'index.html')
# Paiements Fr
def paiementsFr_graphique(request):
    paies = PaiementsFr.objects.all()
    montants = [paie.montant for paie in paies]
    noms_paies = [paie.code for paie in paies]
    plt.bar(noms_paies, montants)
    plt.xlabel('Noms de paies')
    plt.ylabel('Montants totaux')
    plt.title('Montants totaux des paies')
    plt.savefig('paiesFr_graphique.png')
    plt.show()
    return render(request, 'index.html')


def facturesFr_graphique(request):
    factures = FactureFr.objects.all()
    montants = [facture.total for facture in factures]
    noms_factures = [facture.code for facture in factures]
    plt.bar(noms_factures, montants)
    plt.xlabel('Noms de factures')
    plt.ylabel('Montants totaux')
    plt.title('Montants totaux des factures')
    plt.savefig('factures_graphique2.png')
    plt.show()
    return render(request, 'index.html')


def index(request):
    if request.session.get('username', None):
        x = request.session['username']
        return render(request, 'index.html', {"name": x})
    else:
        return redirect('login')


def produitList(request):
    if request.session.get('username', None):
        userId = User.objects.get(
            username=request.session['username'])
        produitList = Produit.objects.all()
        # print(bookingList)
        return render(request, 'produits.html', {"produitList": produitList})
    else:
        return redirect('login')


# Produit
def produits(request):

    produits = Produit.objects.all()
    return render(request, 'produits.html', {"produits": produits})


class ProdCreateView(CreateView):
    model = Produit
    template_name = 'prod_form.html'
    fields = '__all__'
    success_url = reverse_lazy('produits')


class ProdUpdateView(UpdateView):
    model = Produit
    form_class = ProductForm
    template_name = 'update_prod.html'
    success_url = reverse_lazy('produits')


class ProdDeleteView(DeleteView):
    model = Produit
    template_name = 'prod_confirm_delete.html'
    success_url = reverse_lazy('produits')

# Clients


def clientList(request):

    clientList = Client.objects.all()
    return render(request, 'clients.html', {"clientList": clientList})


class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_form.html'
    fields = '__all__'
    success_url = reverse_lazy('clientList')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'update_client.html'
    success_url = reverse_lazy('clientList')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('clientList')

# End Clients

    # Fournisseurs


def foursList(request):

    foursList = Fournisseur.objects.all()
    return render(request, 'fournis.html', {"foursList": foursList})


class FoursCreateView(CreateView):
    model = Fournisseur
    template_name = 'fourn_form.html'
    fields = '__all__'
    success_url = reverse_lazy('foursList')


class FournUpdateView(UpdateView):
    model = Fournisseur
    form_class = FourForm
    template_name = 'update_fourn.html'
    success_url = reverse_lazy('foursList')


class FournDeleteView(DeleteView):
    model = Fournisseur
    template_name = 'fours_confirm_delete.html'
    success_url = reverse_lazy('foursList')
# End Fournisseurs


# Factures
# Ajouter
class FactClCreateView(CreateView):
    model = FactureCl
    template_name = 'fact_cl_form.html'
    fields = '__all__'
    success_url = reverse_lazy('factCl')


class FactFrCreateView(CreateView):
    model = FactureFr
    template_name = 'fact_fr_form.html'
    fields = '__all__'
    success_url = reverse_lazy('factFr')
# Affiche


def factCl(request):

    facturesList = FactureCl.objects.all()
    Total1 = 0
    Total2 = 0
    for p in facturesList:
        Total1=Total1+p.HTaxe
        Total2=Total2+p.total
    return render(request, 'factCl.html', {"facturesList": facturesList,"Total1":Total1,"Total2":Total2})
# END


def factFr(request):

    facturesList = FactureFr.objects.all()
    Total1 = 0
    Total2 = 0
    for p in facturesList:
        Total1=Total1+p.HTaxe
        Total2=Total2+p.total
    return render(request, 'factFr.html', {"facturesList": facturesList,"Total1":Total1,"Total2":Total2})


# Update
class FactClUpdateView(UpdateView):
    model = FactureCl
    form_class = FactFormCl
    template_name = 'update_fact_cl.html'
    success_url = reverse_lazy('factCl')


class FactFrUpdateView(UpdateView):
    model = FactureFr
    form_class = FactFormFr
    template_name = 'update_fact_fr.html'
    success_url = reverse_lazy('factFr')

# Delete


class FactClDeleteView(DeleteView):
    model = FactureCl
    template_name = 'factCl_confirm_delete.html'
    success_url = reverse_lazy('factCl')


class FactFrDeleteView(DeleteView):
    model = FactureFr
    template_name = 'factFr_confirm_delete.html'
    success_url = reverse_lazy('factFr')

# End Fact

# Notes
# Ajouter


class NoteCreateView(CreateView):
    model = Notes
    template_name = 'note_form.html'
    fields = '__all__'
    success_url = reverse_lazy('notes')

# Affiche


def notes(request):

    notes = Notes.objects.all()
    Total1 = 0
    Total2 = 0
    for p in notes:
        Total1=Total1+p.HTaxe
        Total2=Total2+p.total
    return render(request, 'notes.html', {"notes": notes,"Total1":Total1,"Total2":Total2})
# Update


class NoteUpdateView(UpdateView):
    model = Notes
    form_class = NoteForm
    template_name = 'update_note.html'
    success_url = reverse_lazy('notes')

# Delete


class NoteDeleteView(DeleteView):
    model = Notes
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('notes')
# END

# Piece Journal


def Pieces(request):

    pieces = PieceCompt.objects.all()
    facturesList = FactureFr.objects.all()
    facturesClList = FactureCl.objects.all()
    paiements = Paiements.objects.all()
    paiementsFr = PaiementsFr.objects.all()
    notes = Notes.objects.all()
    # piece =None
    Total1 = 0
    Total2 = 0
    Total3 = 0
    Total4 = 0
    Total5 = 0
    Total = 0
    for p in paiements:
        Total1=Total1+p.montant 
    for f2 in facturesClList:
        Total2 = Total2+f2.total
    for f in facturesList:
        Total3 = Total3+f.total
    for n in notes:
        Total4 = Total4+n.total

    for p in paiementsFr:
        Total5=Total5+p.montant 
    Total = Total1 + Total2 - Total3 + Total4 + Total5
    return render(request, 'pieces.html', {"pieces": pieces, "paiements": paiements,"paiementsFr": paiementsFr,
                                           "facturesList": facturesList, "notes": notes, "facturesClList": facturesClList, 'Total': Total})


class PieceCreateView(CreateView):
    model = PieceCompt
    template_name = 'piece_form.html'
    fields = '__all__'
    success_url = reverse_lazy('pieces')


class PieceUpdateView(UpdateView):
    model = PieceCompt
    form_class = PieceForm
    template_name = 'update_piece.html'
    success_url = reverse_lazy('pieces')


class PieceDeleteView(DeleteView):
    model = PieceCompt
    template_name = 'piece_confirm_delete.html'
    success_url = reverse_lazy('pieces')

# End Pieces

# Ecriture Comptable


def EcritureComp(request):

    pieces = PieceCompt.objects.all()
    facturesList = FactureFr.objects.all()
    facturesClList = FactureCl.objects.all()
    paiements = Paiements.objects.all()
    paiementsFr = PaiementsFr.objects.all()
    notes = Notes.objects.all()

    # piece =None
    Total1 = 0
    Total2 = 0
    Total3 = 0
    Total4 = 0
    Total44 = 0
    Total11 = 0
    Total22 = 0
    Total5 = 0
    TotalPF = 0
    Total = 0
    # for p in pieces:
    #             Total1=Total1+p.deb
    #             Total4=Total4+p.cred
    for f2 in facturesClList:
        Total2 = Total2 + f2.total
    for n in notes:
        Total1 = Total1 + n.total
    for f in facturesList:
        Total3 = Total3+f.HTaxe + f.TVA
        Total4 = Total4 + f.total1
    for p in paiements:
        Total44=Total44+p.Cred + p.Deb
    for p in paiementsFr:
        TotalPF=TotalPF+p.Cred + p.Deb

    Total = Total2 + Total3 + Total44 - Total1 + TotalPF
    Total5 = Total2 - Total4 + Total44 - Total1 + TotalPF
    return render(request, 'ecriture.html', {"paiements": paiements,"paiementsFr": paiementsFr, "notes": notes, 
                                             "facturesList": facturesList, "facturesClList": facturesClList, 
                                             'Total': Total, 'Total5': Total5})


class EcritUpdateView(UpdateView):
    model = PieceCompt
    form_class = PieceForm
    template_name = 'update_piece.html'
    success_url = reverse_lazy('ecriture')

# End Ecriture


# End Ecriture
def GL(request):
    # pieces = None

    factCl = FactureCl.objects.all()
    factFr = FactureFr.objects.all()
    paie = Paiements.objects.all()
    paies = PaiementsFr.objects.all()
    note = Notes.objects.all()

    balance1 = 0;balance2 = 0;balance3 = 0;balance4 = 0;balance5 = 0;balance6 = 0;balance7 = 0;balancePF = 0;balancePF1 = 0;
    balance = 0;totalOR = 0;totalOP1 = 0;totalOP = 0;totalAR = 0;totalAR1 = 0; totalAR2 = 0 ;totalTP = 0
    totalTP1 = 0;totalAP = 0;totalAP1 = 0;totalTR = 0;totalTR1 = 0;totalTR2 = 0;totalPS = 0;totalPS1 = 0;totalPS2 = 0;totalEX = 0;
    totalEX1 = 0;TG = 0;TG1 = 0;TG2 = 0
    for f in factCl:
        balance1=balance1+f.total
        totalTR1 = totalTR1 + f.TVA
        totalPS1 = totalPS1 + f.HTaxe
                
    for f in factFr:
        balance2=balance2-f.total
        totalTP1=totalTP1+f.TVA
        totalEX1 = totalEX1 + f.HTaxe

    for p in paie:
        balance3=balance3+p.Deb
        balance6=balance6-p.Cred
    for p in paies:
        balancePF=balancePF+p.Deb
        balancePF1=balancePF1-p.Cred
    for n in note:
        balance7=balance7-n.total
        totalTR2 = totalTR2 + n.TVA
        totalPS2 = totalPS2 + n.HTaxe1

    totalOR = totalOR + balance3 + balancePF
    totalOP = totalOP - balance6 - balancePF1
    totalOP1 = totalOP1 - totalOP
    totalAR1 = totalAR1 + balance1 - balance6 
    totalAR2 =-( totalAR2 - balance7 - balance3 )
    totalAR = totalAR + totalAR1 - totalAR2
    totalTP = totalTP + totalTP1
    totalAP = totalAP - balance2 
    totalAP1 =  - balancePF1
    totalAP2 = totalAP1 - totalAP
    totalTR = totalTR2 - totalTR1
    totalPS = totalPS2 - totalPS1
    totalEX = totalEX + totalEX1
 
    TG1 = totalOR + totalAR1 + totalTP + totalTR2 + totalPS2 + totalEX + totalAP1
    TG2 = totalOP + totalAR2 + totalAP + totalTR1 + totalPS1 
    TG = TG1 - TG2
    return render(request, 'grandLiver.html', {"paie": paie,"paies": paies,"factCl":
        factCl,"factFr": factFr,"note": note,
        'totalOR':totalOR,'totalOP':totalOP,'totalOP1':totalOP1,'totalAR':totalAR,'totalAR1':totalAR1,
        'totalAR2':totalAR2,'totalTP':totalTP,'totalAP':totalAP,'totalAP1':totalAP1,'totalAP2':totalAP2,
        'totalTR':totalTR,'totalTR1':totalTR1,'totalTR2':totalTR2,
        'totalPS':totalPS,'totalPS1':totalPS1,'totalPS2':totalPS2,
        'totalEX':totalEX,'totalEX1':totalEX1,
        'TG':TG,'TG1':TG1,'TG2':TG2,
        })
    
# Balance General
def BG(request):
    # pieces = None

    factCl = FactureCl.objects.all()
    factFr = FactureFr.objects.all()
    paie = Paiements.objects.all()
    note = Notes.objects.all()

    balance1 = 0;balance2 = 0;balance3 = 0;balance4 = 0;balance5 = 0;balance6 = 0;balance7 = 0;
    balance = 0;totalOR = 0;totalOP1 = 0;totalOP = 0;totalAR = 0;totalAR1 = 0; totalAR2 = 0 ;totalTP = 0
    totalTP1 = 0;totalAP = 0;totalAP1 = 0;totalTR = 0;totalTR1 = 0;totalTR2 = 0;totalPS = 0;totalPS1 = 0;totalPS2 = 0;totalEX = 0;
    totalEX1 = 0;TG = 0;TG1 = 0;TG2 = 0
    for f in factCl:
        balance1=balance1+f.total
        totalTR1 = totalTR1 + f.TVA
        totalPS1 = totalPS1 + f.HTaxe
                
    for f in factFr:
        balance2=balance2-f.total
        totalTP1=totalTP1+f.TVA
        totalEX1 = totalEX1 + f.HTaxe

    for p in paie:
        balance3=balance3+p.Deb
        balance6=balance6-p.Cred
    for n in note:
        balance7=balance7-n.total
        totalTR2 = totalTR2 + n.TVA
        totalPS2 = totalPS2 + n.HTaxe1

    totalOR = totalOR + balance3
    totalOP = totalOP - balance6
    totalOP1 = totalOP1 - totalOP
    totalAR1 = totalAR1 + balance1 - balance6
    totalAR2 =-( totalAR2 - balance7 - balance3)
    totalAR = totalAR + totalAR1 - totalAR2
    totalTP = totalTP + totalTP1
    totalAP = totalAP - balance2
    totalAP1 = totalAP1 - totalAP
    totalTR = totalTR2 - totalTR1
    totalTR11 =0
    totalTR11 =totalTR11 - totalTR
    totalPS = totalPS1 - totalPS2
    totalEX = totalEX + totalEX1
 
    TG1 = totalOR + totalAR + totalTP + totalEX
    TG2 = totalOP + totalAP + totalTR11 + totalPS
    TG = totalOR + totalOP1 + totalAR + totalTP + totalAP1 + totalTR + totalPS + totalEX
    return render(request, 'BG.html', {"paie": paie,"factCl":
        factCl,"factFr": factFr,"note": note,
        'totalOR':totalOR,'totalOP':totalOP,'totalOP1':totalOP1,'totalAR':totalAR,'totalAR1':totalAR1,
        'totalAR2':totalAR2,'totalTP':totalTP,'totalAP':totalAP,'totalAP1':totalAP1,
        'totalTR':totalTR,'totalTR1':totalTR1,'totalTR11':totalTR11,
        'totalPS':totalPS,'totalPS1':totalPS1,'totalPS2':totalPS2,
        'totalEX':totalEX,'totalEX1':totalEX1,
        'TG':TG,'TG1':TG1,'TG2':TG2,
        })


def BAC(request):
    clients = Client.objects.all()

    client_info_list = []
    balance3 = 0
    
    for client in clients:
        factures = FactureCl.objects.filter(client=client)
        paiements = Paiements.objects.filter(Client=client)

        balance = 0; balance1 = 0; balance2 = 0;
        for f in factures:
            balance1=balance1+f.total

        for p in paiements:
            balance2=balance2+p.Montant
        balance = balance + balance1 + balance2
        balance3 = balance3 + balance 
        client_info_list.append({
            'client': client,
            'factures': factures,
            'paiements': paiements,
            'balance' : balance
        })

    context = {
        'client_info_list': client_info_list,
        'balance3' : balance3
    }

    return render(request, 'BAC.html', context)

def BAF(request):
    fournisseurs = Fournisseur.objects.all()
    
    fournisseur_info_list = []
    balance3 = 0
    for fournisseur in fournisseurs:
        factures = FactureFr.objects.filter(fournisseur=fournisseur)
        paiements = PaiementsFr.objects.filter(fournisseur=fournisseur)

        balance = 0; balance1 = 0; balance2 = 0;
        for f in factures:
            balance1=balance1+f.total

        for p in paiements:
            balance2=balance2+p.Montant
        balance = balance + balance1 + balance2
        balance3 = balance3 + balance 
        fournisseur_info_list.append({
            'fournisseur': fournisseur,
            'factures': factures,
            'paiements': paiements,
            'balance' : balance
        })

    context = {
        'fournisseur_info_list': fournisseur_info_list,
        'balance3' : balance3
    }
    return render(request, 'BAF.html', context)



# # Hmmmmmmm
# def client_table(request):
#     clients = Client.objects.all()

#     context = {
#         'clients': clients,
#     }

#     return render(request, 'client_table.html', context)

# def client_details(request, client_id):
#     client = Client.objects.get(pk=client_id)
#     factures = FactureCl.objects.filter(client=client)
#     paiements = Paiements.objects.filter(Client=client)

#     context = {
#         'client': client,
#         'factures': factures,
#         'paiements': paiements,
#     }

#     return render(request, 'client_details.html', context)
# #Hmmmmm 

# Bilan
def Bilan(request):
    
    factCl = FactureCl.objects.all()
    factFr = FactureFr.objects.all()
    paie = Paiements.objects.all()
    paies = PaiementsFr.objects.all()
    note = Notes.objects.all()

    balance1 = 0;balance2 = 0;balance3 = 0;balance4 = 0;balance5 = 0;balance6 = 0;balance7 = 0;balancePF = 0;balancePF1 = 0;
    balance = 0;totalOR = 0;totalOP1 = 0;totalOP = 0;totalAR = 0;totalAR1 = 0; totalAR2 = 0 ;totalTP = 0
    totalTP1 = 0;totalAP = 0;totalAP1 = 0;totalTR = 0;totalTR1 = 0;totalTR2 = 0;totalPS = 0;totalPS1 = 0;totalPS2 = 0;totalEX = 0;
    totalEX1 = 0;TG = 0;TG1 = 0;TG2 = 0;TotalAC =0;TotalAC1 =0
    for f in factCl:
        balance1=balance1+f.total
        totalTR1 = totalTR1 + f.TVA
        totalPS1 = totalPS1 + f.HTaxe
                
    for f in factFr:
        balance2=balance2-f.total
        totalTP1=totalTP1+f.TVA
        totalEX1 = totalEX1 + f.HTaxe

    for p in paie:
        balance3=balance3+p.Deb
        balance6=balance6-p.Cred
    for p in paies:
        balancePF=balancePF+p.Deb
        balancePF1=balancePF1-p.Cred
    for n in note:
        balance7=balance7-n.total
        totalTR2 = totalTR2 + n.TVA
        totalPS2 = totalPS2 + n.HTaxe1

    totalOR = totalOR + balance3 + balancePF
    totalOP = totalOP - balance6 - balancePF1
    totalOP1 = totalOP1 - totalOP
    totalAR1 = totalAR1 + balance1 - balance6 
    totalAR2 =-( totalAR2 - balance7 - balance3 )
    totalAR = totalAR + totalAR1 - totalAR2
    totalTP = totalTP + totalTP1
    totalAP = totalAP - balance2 
    totalAP1 =  - balancePF1
    totalAP2 = totalAP1 - totalAP
    totalTR = totalTR2 - totalTR1
    totalPS = totalPS2 - totalPS1
    totalEX = totalEX + totalEX1
 
    TG1 = totalOR + totalAR1 + totalTP + totalTR2 + totalPS2 + totalEX
    TG2 = totalOP + totalAR2 + totalAP + totalTR1 + totalPS1 
    TG = TG1 - TG2
    
    TotalAC = TotalAC + totalOR + totalOP1 + totalTP
    TotalAC1 = TotalAC + totalAR
    TotalDCT = -(totalTR + totalAP2)
    totalAP11 = - totalAP2
    totalTR11 = -totalTR
    totalCP = -totalPS - totalEX
    totalPCP = totalCP + TotalDCT
    TotalBillan = TotalAC1 - totalPCP
    return render(request, 'bilan.html', {"paie": paie,"paies": paies,"factCl":
        factCl,"factFr": factFr,"note": note,
        'totalOR':totalOR,'totalOP':totalOP,'totalOP1':totalOP1,'totalAR':totalAR,'totalAR1':totalAR1,
        'totalAR2':totalAR2,'totalTP':totalTP,'totalAP':totalAP,'totalAP1':totalAP1,
        'totalTR':totalTR,'totalTR1':totalTR1,'totalTR2':totalTR2,
        'totalPS':totalPS,'totalPS1':totalPS1,'totalPS2':totalPS2,
        'totalEX':totalEX,'totalEX1':totalEX1,
        'TG':TG,'TG1':TG1,'TG2':TG2,'TotalAC':TotalAC,'TotalAC1':TotalAC1,'TotalDCT':TotalDCT,
        'totalAP11':totalAP11,'totalTR11':totalTR11,'totalCP':totalCP,'totalPCP':totalPCP,'TotalBillan':TotalBillan
        })
# Compte de result
# Compte de result
def ComptRes(request):
    
    factCl = FactureCl.objects.all()
    factFr = FactureFr.objects.all()
    paie = Paiements.objects.all()
    note = Notes.objects.all()

    balance1 = 0;balance2 = 0;balance3 = 0;balance4 = 0;balance5 = 0;balance6 = 0;balance7 = 0;
    balance = 0;totalOR = 0;totalOP1 = 0;totalOP = 0;totalAR = 0;totalAR1 = 0; totalAR2 = 0 ;totalTP = 0
    totalTP1 = 0;totalAP = 0;totalAP1 = 0;totalTR = 0;totalTR1 = 0;totalTR2 = 0;totalPS = 0;totalPS1 = 0;totalPS2 = 0;totalEX = 0;
    totalEX1 = 0;TG = 0;TG1 = 0;TG2 = 0;TotalAC =0;TotalAC1 =0
    for f in factCl:
        balance1=balance1+f.total
        totalTR1 = totalTR1 + f.TVA
        totalPS1 = totalPS1 + f.HTaxe
                
    for f in factFr:
        balance2=balance2-f.total
        totalTP1=totalTP1+f.TVA
        totalEX1 = totalEX1 + f.HTaxe

    for p in paie:
        balance3=balance3+p.Deb
        balance6=balance6-p.Cred
    for n in note:
        balance7=balance7-n.total
        totalTR2 = totalTR2 + n.TVA
        totalPS2 = totalPS2 + n.HTaxe1

    totalOR = totalOR + balance3
    totalOP = totalOP - balance6
    totalOP1 = totalOP1 - totalOP
    totalAR1 = totalAR1 + balance1 - balance6
    totalAR2 =-( totalAR2 - balance7 - balance3)
    totalAR = totalAR + totalAR1 - totalAR2
    totalTP = totalTP + totalTP1
    totalAP = totalAP - balance2
    totalAP1 = totalAP1 - totalAP
    totalTR = totalTR2 - totalTR1
    totalPS = totalPS2 - totalPS1
    totalEX = totalEX + totalEX1
 
    TG1 = totalOR + totalAR1 + totalTP + totalTR2 + totalPS2 + totalEX
    TG2 = totalOP + totalAR2 + totalAP + totalTR1 + totalPS1 
    TG = totalOR + totalOP1 + totalAR + totalTP + totalAP1 + totalTR + totalPS + totalEX
    
    TotalAC = TotalAC + totalOR + totalOP1 + totalTP
    TotalAC1 = TotalAC + totalAR
    TotalDCT = -(totalTR + totalAP1)
    totalAP11 = -totalAP1
    totalTR11 = -totalTR
    TotalRev = -totalPS
    totalCR = TotalRev - totalEX
    return render(request, 'compte_res.html', {"paie": paie,"factCl":
        factCl,"factFr": factFr,"note": note,
        'totalOR':totalOR,'totalOP':totalOP,'totalOP1':totalOP1,'totalAR':totalAR,'totalAR1':totalAR1,
        'totalAR2':totalAR2,'totalTP':totalTP,'totalAP':totalAP,'totalAP1':totalAP1,
        'totalTR':totalTR,'totalTR1':totalTR1,'totalTR2':totalTR2,
        'totalPS':totalPS,'totalPS1':totalPS1,'totalPS2':totalPS2,
        'totalEX':totalEX,'totalEX1':totalEX1,
        'TG':TG,'TG1':TG1,'TG2':TG2,'TotalAC':TotalAC,'TotalAC1':TotalAC1,'TotalDCT':TotalDCT,
        'totalAP11':totalAP11,'totalTR11':totalTR11,'TotalRev':TotalRev,'totalCR':totalCR
        })
# Compte de result
def RG(request):
    
    factCl = FactureCl.objects.all()
    factFr = FactureFr.objects.all()
    paie = Paiements.objects.all()
    paies = PaiementsFr.objects.all()
    note = Notes.objects.all()

    balance1 = 0;balance2 = 0;balance3 = 0;balance4 = 0;balance5 = 0;balance6 = 0;balance7 = 0;balancePF = 0;balancePF1 = 0;
    balance = 0;totalOR = 0;totalOP1 = 0;totalOP = 0;totalAR = 0;totalAR1 = 0; totalAR2 = 0 ;totalTP = 0
    totalTP1 = 0;totalAP = 0;totalAP1 = 0;totalTR = 0;totalTR1 = 0;totalTR2 = 0;totalPS = 0;totalPS1 = 0;totalPS2 = 0;totalEX = 0;
    totalEX1 = 0;TG = 0;TG1 = 0;TG2 = 0;TotalAC =0;TotalAC1 =0
    for f in factCl:
        balance1=balance1+f.total
        totalTR1 = totalTR1 + f.TVA
        totalPS1 = totalPS1 + f.HTaxe
                
    for f in factFr:
        balance2=balance2-f.total
        totalTP1=totalTP1+f.TVA
        totalEX1 = totalEX1 + f.HTaxe

    for p in paie:
        balance3=balance3+p.Deb
        balance6=balance6-p.Cred
    for p in paies:
        balancePF=balancePF+p.Deb
    balancePF1=balancePF1-p.Cred
    for n in note:
        balance7=balance7-n.total
        totalTR2 = totalTR2 + n.TVA
        totalPS2 = totalPS2 + n.HTaxe1

    totalOR = totalOR + balance3
    totalOP = totalOP - balance6
    totalOP1 = totalOP1 - totalOP
    totalAR1 = totalAR1 + balance1 - balance6
    totalAR2 =-( totalAR2 - balance7 - balance3)
    totalAR = totalAR + totalAR1 - totalAR2
    totalTP = totalTP + totalTP1
    totalAP = totalAP - balance2 
    totalAP1 =  - balancePF1
    totalAP2 = totalAP1 - totalAP
    totalTR = totalTR2 - totalTR1
    totalPS = totalPS2 - totalPS1
    totalEX = totalEX + totalEX1
 
    TG1 = totalOR + totalAR1 + totalTP + totalTR2 + totalPS2 + totalEX
    TG2 = totalOP + totalAR2 + totalAP + totalTR1 + totalPS1 
    TG = totalOR + totalOP1 + totalAR + totalTP + totalAP1 + totalTR + totalPS + totalEX
    
    TotalAC = TotalAC + totalOR + totalOP1 + totalTP
    TotalAC1 = TotalAC + totalAR
    TotalDCT = -(totalTR + totalAP1)
    totalAP11 = -totalAP2
    totalTR11 = -totalTR
    TotalRev = -totalPS
    totalCR = TotalRev - totalEX
    return render(request, 'RG.html', {"paie": paie,"factCl":
        factCl,"factFr": factFr,"note": note,
        'totalOR':totalOR,'totalOP':totalOP,'totalOP1':totalOP1,'totalAR':totalAR,'totalAR1':totalAR1,
        'totalAR2':totalAR2,'totalTP':totalTP,'totalAP':totalAP,'totalAP1':totalAP1,
        'totalTR':totalTR,'totalTR1':totalTR1,'totalTR2':totalTR2,
        'totalPS':totalPS,'totalPS1':totalPS1,'totalPS2':totalPS2,
        'totalEX':totalEX,'totalEX1':totalEX1,
        'TG':TG,'TG1':TG1,'TG2':TG2,'TotalAC':TotalAC,'TotalAC1':TotalAC1,'TotalDCT':TotalDCT,
        'totalAP11':totalAP11,'totalTR11':totalTR11,'TotalRev':TotalRev,'totalCR':totalCR
        })

# Paiments
# Affiche


def Paiments(request):
    
    paiments = Paiements.objects.all()
    Total1 = 0
    for p in paiments:
        Total1=Total1+p.Montant
    return render(request, 'paiments.html', {"paiments": paiments,"Total1":Total1})


class PaiementCreateView(CreateView):
    model = Paiements
    template_name = 'pie_form.html'
    fields = '__all__'
    success_url = reverse_lazy('paiments')


class PaiementUpdateView(UpdateView):
    model = Paiements
    form_class = PaiementForm
    template_name = 'update_pie.html'
    success_url = reverse_lazy('paiments')


class PaiementDeleteView(DeleteView):
    model = Paiements
    template_name = 'pie_confirm_delete.html'
    success_url = reverse_lazy('paiments')

#Paiements Fournisseur 
def PaimentsFr(request):

    paiments = PaiementsFr.objects.all()
    Total1 = 0
    for p in paiments:
        Total1=Total1+p.Montant
    return render(request, 'paimentsFr.html', {"paiments": paiments,"Total1":Total1})


class PaiementFr_CreateView(CreateView):
    model = PaiementsFr
    template_name = 'pie_Fr_form.html'
    fields = '__all__'
    success_url = reverse_lazy('paiments_fr')


class PaiementFr_UpdateView(UpdateView):
    model = PaiementsFr
    form_class = Paiement_Fr_Form
    template_name = 'update_pieFr.html'
    success_url = reverse_lazy('paiments_fr')


class PaiementFr_DeleteView(DeleteView):
    model = PaiementsFr
    template_name = 'pieFr_confirm_delete.html'
    success_url = reverse_lazy('paiments_fr')

# Affiche


def Journaux(request):

    journaux = Journal.objects.all()
    return render(request, 'journaux.html', {"journaux": journaux})

class journauxCreateView(CreateView):
    model = Journal
    template_name = 'journaux_form.html'
    fields = '__all__'
    success_url = reverse_lazy('journaux')


class journauxUpdateView(UpdateView):
    model = Journal
    form_class = JournauxForm
    template_name = 'update_journaux.html'
    success_url = reverse_lazy('journaux')


class journauxDeleteView(DeleteView):
    model = Journal
    template_name = 'journaux_confirm_delete.html'
    success_url = reverse_lazy('journaux')


# Logs
def logout(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('login')


def register(request):
    if request.session.get('username', None):
        return redirect('index')
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(username=username) or User.objects.filter(email=email):
            messages.warning(request, "account already exist")
        else:
            password = request.POST['password']
            error = []
            if (len(username) < 3):
                error.append(1)
                messages.warning(
                    request, "Username Field must be greater than 3 character.")
            if (len(password) < 5):
                error.append(1)
                messages.warning(
                    request, "Password Field must be greater than 5 character.")
            if (len(email) == 0):
                error.append(1)
                messages.warning(request, "Email field can't be empty")
            if (len(error) == 0):
                password_hash = make_password(password)
                user = User(username=username,
                            password=password_hash, email=email)
                user.save()
                messages.info(request, "account created successfully")
                redirect('register')
            else:
                redirect('register')
    return render(request, 'register.html', {})


def login(request):
    if request.session.get('username', None):
        return redirect('index')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if not len(username):
            messages.warning(request, "username is empty")
            redirect('login')
        elif not len(password):
            messages.warning(request, "password is empty")
            redirect('login')
        else:
            pass
        if User.objects.filter(username=username):
            user = User.objects.filter(username=username)[0]
            password_hash = user.password
            resp = check_password(password, password_hash)
            if resp == 1:
                request.session['id'] = user.id
                request.session['username'] = username
                return redirect('index')
            else:
                messages.warning(request, "username or password is incorrect")
                redirect('login')
        else:
            messages.warning(request, "account 404")
            redirect('login')
    return render(request, 'login.html', {})


# devise
def devise(request):

    devise = Devises.objects.all()
    return render(request, 'devise.html', {"devise": devise})


class deviseCreateView(CreateView):
    model = Devises
    template_name = 'devise_form.html'
    fields = '__all__'
    success_url = reverse_lazy('devise')


class deviseUpdateView(UpdateView):
    model = Devises
    form_class = deviseForm
    template_name = 'update_devise.html'
    success_url = reverse_lazy('devise')


class deviseDeleteView(DeleteView):
    model = Devises
    template_name = 'devise_confirm_delete.html'
    success_url = reverse_lazy('devise')


# taxe
def taxe(request):

    taxe = Taxes.objects.all()
    return render(request, 'taxe.html', {"taxe": taxe})


class taxeCreateView(CreateView):
    model = Taxes
    template_name = 'taxe_form.html'
    fields = '__all__'
    success_url = reverse_lazy('taxe')


class taxeUpdateView(UpdateView):
    model = Taxes
    form_class = taxeForm
    template_name = 'update_taxe.html'
    success_url = reverse_lazy('taxe')


class taxeDeleteView(DeleteView):
    model = Taxes
    template_name = 'taxe_confirm_delete.html'
    success_url = reverse_lazy('taxe')


# immob
def immob(request):

    immob = Immobe.objects.all()
    return render(request, 'immob.html', {"immob": immob})


class immobCreateView(CreateView):
    model = Immobe
    template_name = 'immob_form.html'
    fields = '__all__'
    success_url = reverse_lazy('immob')


class immobUpdateView(UpdateView):
    model = Immobe
    form_class = immobForm
    template_name = 'update_immob.html'
    success_url = reverse_lazy('immob')


class immobDeleteView(DeleteView):
    model = Immobe
    template_name = 'immob_confirm_delete.html'
    success_url = reverse_lazy('immob')


# plan
def plan(request):

    plan = Plan.objects.all()
    return render(request, 'plan.html', {"plan": plan})


class planCreateView(CreateView):
    model = Plan
    template_name = 'plan_form.html'
    fields = '__all__'
    success_url = reverse_lazy('plan')


class planUpdateView(UpdateView):
    model = Plan
    form_class = planForm
    template_name = 'update_plan.html'
    success_url = reverse_lazy('plan')


class planDeleteView(DeleteView):
    model = Plan
    template_name = 'plan_confirm_delete.html'
    success_url = reverse_lazy('plan')
