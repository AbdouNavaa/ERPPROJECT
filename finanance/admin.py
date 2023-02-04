from django.contrib import admin
from .models import *

# # Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Fournisseur)
admin.site.register(Type)
admin.site.register(FactureCl)
admin.site.register(FactureFr)
admin.site.register(Produit)
admin.site.register(Journal)
admin.site.register(PieceCompt)
admin.site.register(Paiements)
admin.site.register(JournalPaiement)
# admin.site.register(Booking)
