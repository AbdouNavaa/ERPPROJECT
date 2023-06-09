from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "User: "+self.username


class Client(models.Model):
    Name = models.CharField(max_length=40, null=False)
    address = models.CharField(max_length=40,)
    mobile = models.CharField(max_length=20, null=False)
    Type = models.ForeignKey("Type", on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Type(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Fournisseur(models.Model):
    Name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    Type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class FactureCl(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    journal = models.ForeignKey("Journal", on_delete=models.CASCADE)
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    Devise = models.ForeignKey("Devises", on_delete=models.CASCADE)
    compte = models.ForeignKey("Plan", on_delete=models.CASCADE)
    date_facturation = models.DateField()
    quantity = models.FloatField()

    @property
    def code(self):
        return str(self.journal.code)+str(self.date_facturation.year)+"/"+str(self.id)

    def __str__(self):
        return self.code

    @property
    def HTaxe(self):
        hTaxe = self.quantity*self.produit.prix
        return hTaxe

    @property
    def TVA(self):
        tva = (self.quantity*self.produit.prix) * self.produit.Taxes.Montant
        return tva

    @property
    def total(self):
        Total = self.TVA + self.HTaxe
        return Total


class Notes(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    journal = models.ForeignKey("Journal", on_delete=models.CASCADE)
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    Devise = models.ForeignKey("Devises", on_delete=models.CASCADE)
    compte = models.ForeignKey("Plan", on_delete=models.CASCADE)
    date_facturation = models.DateField()
    quantity = models.FloatField()

    @property
    def code(self):
        return "R"+str(self.journal.code)+str(self.date_facturation.year)+"/"+str(self.id)

    def __str__(self):
        return self.code

    @property
    def HTaxe(self):
        hTaxe =-self.quantity*self.produit.prix
        return hTaxe
    @property
    def HTaxe1(self):
        hTaxe =self.quantity*self.produit.prix
        return hTaxe

    @property
    def TVA(self):
        tva =(self.quantity*self.produit.prix) * self.produit.Taxes.Montant
        return tva

    @property
    def total(self):
        Total = -(self.TVA - self.HTaxe)
        return Total
    @property
    def total1(self):
        Total = self.TVA - self.HTaxe
        return Total


class FactureFr(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey("Produit", on_delete=models.CASCADE)
    journal = models.ForeignKey("Journal", on_delete=models.CASCADE)
    Devise = models.ForeignKey("Devises", on_delete=models.CASCADE)
    compte = models.ForeignKey("Plan", on_delete=models.CASCADE)
    date_facturation = models.DateField()
    # Taxe = models.FloatField()
    quantity = models.FloatField()

    @property
    def code(self):
        return str(self.journal.code)+str(self.date_facturation.year)+"/"+str(self.id)

    def __str__(self):
        return self.code

    @property
    def total(self):
        Total = self.TVA + self.HTaxe
        return Total

    @property
    def HTaxe(self):
        HTaxe = self.quantity*self.produit.prix
        return HTaxe

    @property
    def TVA(self):
        tva = (self.quantity*self.produit.prix) * self.produit.Taxes.Montant
        return tva

    @property
    def total1(self):
        Total1 = 0
        Total1 = Total1 - self.total
        return Total1


class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    prix = models.FloatField()
    Taxes = models.ForeignKey("Taxes", on_delete=models.CASCADE)
    Taxesfourn = models.FloatField()

    def __str__(self):
        return self.libelle


class Journal(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40, null=True)
    code = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class PieceCompt(models.Model):
    ref = models.FloatField()
    date_comptable = models.DateField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    partenaire = models.ForeignKey(Client, on_delete=models.CASCADE)
    deb = models.FloatField()
    cred = models.FloatField()

    @property
    def total(self):
        Total = self.deb-self.cred
        return Total

    def __str__(self):
        return self.journal.name


class Paiements(models.Model):
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Date = models.DateField()
    montant = models.FloatField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    Devise = models.ForeignKey("Devises", on_delete=models.CASCADE)
    Mode = models.CharField(max_length=100)
    Type_CHOICES = [
        ('E', 'Envoyer'),
        ('R', 'Recevoire'),
    ]
    Type = models.CharField(max_length=1, choices=Type_CHOICES)

    @property
    def Montant(self):
        Montant = 0
        if self.Type in self.Type_CHOICES[0]:
            Montant -= self.montant
        else:
            Montant = self.montant
        return Montant

    @property
    def Deb(self):
        Montant = 0
        if self.Type in self.Type_CHOICES[1]:
            Montant = self.montant
        return Montant

    @property
    def Cred(self):
        Montant =0
        if self.Type in self.Type_CHOICES[0]:
            Montant = self.montant
        return Montant

    @property
    def Credit(self):
        Montant = 0
        if self.Type in self.Type_CHOICES[0]:
            Montant = -self.montant
        return Montant
    
    @property
    def code(self):
        return str(self.journal.code)+str(self.Date.year)+"/"+str(self.id)

    def __str__(self):
        return self.code
    #  = models.BooleanField(choices=)
    # comptBank = models.FloatField()
    # @property
    # def total(self):
    #     Total = self.deb-self.cred
    #     return Total

class PaiementsFr(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    Date = models.DateField()
    montant = models.FloatField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    Devise = models.ForeignKey("Devises", on_delete=models.CASCADE)
    Mode = models.CharField(max_length=100)
    Type_CHOICES = [
        ('E', 'Envoyer'),
        ('R', 'Recevoire'),
    ]
    Type = models.CharField(max_length=1, choices=Type_CHOICES)

    @property
    def Montant(self):
        Montant = 0
        if self.Type in self.Type_CHOICES[0]:
            Montant -= self.montant
        else:
            Montant = self.montant
        return Montant

    @property
    def Deb(self):
        Montant = 0
        if self.Type in self.Type_CHOICES[1]:
            Montant = self.montant
        return Montant

    @property
    def Cred(self):
        Montant =0
        if self.Type in self.Type_CHOICES[0]:
            Montant = self.montant
        return Montant

    @property
    def Credit(self):
        Montant = 0
        if self.Type in self.Type_CHOICES[0]:
            Montant = -self.montant
        return Montant
    
    @property
    def code(self):
        return str(self.journal.code)+str(self.Date.year)+"/"+str(self.id)

    def __str__(self):
        return self.code
    #  = models.BooleanField(choices=)
    # comptBank = models.FloatField()
    # @property
    # def total(self):
    #     Total = self.deb-self.cred
    #     return Total


class Devises(models.Model):
    devise = models.CharField(max_length=100)
    Nom = models.CharField(max_length=100)
    unite = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.devise

class TypesTaxe(models.TextChoices):
    Vente =  'Vente'
    Achat = 'Achats'
    Aucun =  'Aucun'
class Taxes(models.Model):
    nom_taxe = models.CharField(max_length=100)
    type_taxe = models.CharField(max_length=10, choices=TypesTaxe.choices)
    Montant = models.FloatField()

    def __str__(self):
        return self.nom_taxe



class MethodChoices(models.TextChoices):
    Lin = 'Linéaire'
    Deg = 'Degressif'
class TypeChoices(models.TextChoices):
    Year = 'Annee'
    Month = 'Mois'

class Immobe(models.Model):
    nom_immob = models.CharField(max_length=100)
    val_origin= models.FloatField()
    date_acquisition = models.DateField()
    modelActif = models.CharField(max_length=100)
    val_non_amort = models.FloatField()
    methode = models.CharField(max_length=20, choices=MethodChoices.choices)
    duree_amort = models.FloatField()
    duree_amort_type = models.CharField(max_length=10, choices=TypeChoices.choices)

    def __str__(self):
        return self.nom_immob

    @property
    def val_amort(self):
        val_amort = self.val_origin-self.val_non_amort
        return val_amort


class Plan(models.Model):
    code = models.CharField(max_length=40, null=True)
    nom_compte = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    # devise_compte = models.CharField(max_length=100)

    def __str__(self):
        return self.code
