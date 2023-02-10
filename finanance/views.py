from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
# from typing import Type
from .models import *
from .forms import ClientForm,FourForm,FactFormCl,FactFormFr,PieceForm,PaiementForm,NoteForm,ProductForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView,DeleteView,CreateView
# from . import form

from django.shortcuts import render
import matplotlib.pyplot as plt

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

def facturesFr_graphique(request):
    factures = FactureFr.objects.all()
    montants = [facture.total1 for facture in factures]
    noms_factures = [facture.code for facture in factures]
    plt.bar(noms_factures, montants)
    plt.xlabel('Noms de factures')
    plt.ylabel('Montants totaux')
    plt.title('Montants totaux des factures')
    plt.savefig('factures_graphique1.png')
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
    form_class =ProductForm
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
    return render(request, 'factCl.html', {"facturesList": facturesList})
# END
def factFr(request):
    
    facturesList = FactureFr.objects.all()
    return render(request, 'factFr.html', {"facturesList": facturesList})


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
    return render(request, 'notes.html', {"notes": notes})
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
    notes = Notes.objects.all()
    # piece =None
    Total1=0
    Total2=0
    Total3=0
    Total4=0
    Total=0
    for p in paiements:
        Total1=Total1+p.Montant 
    for f2 in facturesClList:
        Total2=Total2+f2.total
    for f in facturesList:
        Total3=Total3+f.total 
    for n in notes:
        Total4=Total4+n.total 
    
    Total = Total1 + Total2 + Total3 + Total4
    return render(request, 'pieces.html', {"pieces": pieces,"paiements":paiements,
                                           "facturesList":facturesList,"notes":notes,"facturesClList":facturesClList,'Total':Total})

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
    
    # piece =None
    Total1=0
    Total2=0
    Total3=0
    Total4=0
    Total5=0
    Total=0
    # for p in pieces:
    #             Total1=Total1+p.deb 
    #             Total4=Total4+p.cred
    for f2 in facturesClList:
                Total1=Total1+f2.HTaxe + f2.TVA
                Total2= Total2 + f2.total
    for f in facturesList:
        Total3=Total3+f.HTaxe + f.TVA
        Total4 = Total4 + f.total1 
    # for p in paiements:
    #     Total2=Total2+p. 
    
    Total = Total2 + Total3
    Total5 = Total2 - Total4
    return render(request, 'ecriture.html', {"paiements":paiements,"pieces": pieces,"facturesList":facturesList,"facturesClList":facturesClList,'Total':Total,'Total5':Total5})
class EcritUpdateView(UpdateView):
    model = PieceCompt
    form_class = PieceForm
    template_name = 'update_piece.html'
    success_url = reverse_lazy('ecriture')

# End Ecriture
def GL(request):
    # pieces = None

    factCl = FactureCl.objects.all()
    factFr = FactureFr.objects.all()
    paie = Paiements.objects.all()
    note = Notes.objects.all()

    balance1 = 0
    balance2 = 0
    balance3 = 0
    balance4 = 0
    balance5 = 0
    balance6 = 0
    balance7 = 0
    balance = 0
    for f in factCl:
                balance1=balance1+f.total
    for f in factFr:
        balance2=balance2-f.total

    for p in paie:
        balance3=balance3+p.Deb
        balance6=balance6-p.Cred
    for n in note:
        balance7=balance7-n.total
    balance = balance + balance1 +balance3
    balance4 = balance4 + balance2 + balance6
    balance5 = balance5 + balance + balance4
    
    bal = -balance4
    return render(request, 'grandLiver.html', {"paie": paie,"factCl": factCl,"factFr": factFr, 'balance':balance,'bal':bal,'balance5':balance5})



# Paiments
# Affiche
def Paiments(request):
    
    paiments = Paiements.objects.all()
    return render(request, 'paiments.html', {"paiments": paiments})

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
        
# Affiche
def Journaux(request):
    
    journaux = Journal.objects.all()
    return render(request, 'journaux.html', {"journaux": journaux})


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