from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    # FactFr
    path('factsFr/<int:pk>/update/',
         views.FactFrUpdateView.as_view(), name='factFr_update'),
    path('factFr/<int:pk>/delete/',
         views.FactFrDeleteView.as_view(), name='delete_factFr'),
    path('factFr/', views.factFr, name='factFr'),
    path('create_factFr/', views.FactFrCreateView.as_view(), name='create_factFr'),

    # FactCl
    path('factCl/<int:pk>/update/',
         views.FactClUpdateView.as_view(), name='factCl_update'),
    path('factCl/<int:pk>/delete/',
         views.FactClDeleteView.as_view(), name='delete_factCl'),
    path('factCl/', views.factCl, name='factCl'),
    path('create_fact/', views.FactClCreateView.as_view(), name='create_factCl'),

    # Note
    path('note/<int:pk>/update/', views.NoteUpdateView.as_view(), name='note_update'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete_note'),
    path('notes/', views.notes, name='notes'),
    path('create_note/', views.NoteCreateView.as_view(), name='create_note'),

    # Client
    path('client/<int:pk>/update/',
         views.ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/',
         views.ClientDeleteView.as_view(), name='delete_client'),
    path('clientList/', views.clientList, name='clientList'),
    path('create_client/', views.ClientCreateView.as_view(), name='create_client'),
    # Prod
    path('prod/<int:pk>/update/', views.ProdUpdateView.as_view(), name='prod_update'),
    path('prod/<int:pk>/delete/', views.ProdDeleteView.as_view(), name='delete_prod'),
    path('produits/', views.produits, name='produits'),
    path('create_prod/', views.ProdCreateView.as_view(), name='create_prod'),

    # Fournisseurs
    path('fourn/<int:pk>/update/',
         views.FournUpdateView.as_view(), name='fourn_update'),
    path('fours/<int:pk>/delete/',
         views.FournDeleteView.as_view(), name='delete_fourn'),
    path('foursList/', views.foursList, name='foursList'),
    path('create_fours/', views.FoursCreateView.as_view(), name='create_fours'),


#     path('clients/', views.client_table, name='client_table'),
#     path('clients/<int:client_id>/', views.client_details, name='client_details'),
#     path('providers/', views.provider_table, name='provider_table'),
#     path('providers/<int:provider_id>/', views.provider_details, name='provider_details'),

    path('GL/', views.GL, name='GL'),
    path('BG/', views.BG, name='BG'),
    path('BAC/', views.BAC, name='BAC'),
    path('BAF/', views.BAF, name='BAF'),
    path('Bilan/', views.Bilan, name='Bilan'),
    path('RG/', views.RG, name='RG'),
    path('ComptRes/', views.ComptRes, name='ComptRes'),

    # Paiements
    path('paiments/', views.Paiments, name='paiments'),
    path('paiments/<int:pk>/update/',
         views.PaiementUpdateView.as_view(), name='pie_update'),
    path('paiment/<int:pk>/delete/',
         views.PaiementDeleteView.as_view(), name='delete_pie'),
    path('create_pie/', views.PaiementCreateView.as_view(), name='create_pie'),
    
    # Paiements Fournisseur
    path('paiments_fr/', views.PaimentsFr, name='paiments_fr'),
    path('paiments_fr/<int:pk>/update/',
         views.PaiementFr_UpdateView.as_view(), name='pieFr_update'),
    path('paiment_fr/<int:pk>/delete/',
         views.PaiementFr_DeleteView.as_view(), name='delete_pieFr'),
    path('create_pieFr/', views.PaiementFr_CreateView.as_view(), name='create_pieFr'),
    # Ecritures Comptable
    path('ecriture/', views.EcritureComp, name='ecriture'),
    path('ecrit/<int:pk>/update/',
         views.EcritUpdateView.as_view(), name='ecrit_update'),
    # Pieces
    path('piece/<int:pk>/update/',
         views.PieceUpdateView.as_view(), name='piece_update'),
    path('piece/<int:pk>/delete/',
         views.PieceDeleteView.as_view(), name='delete_piece'),
    path('pieces/', views.Pieces, name='pieces'),
    path('create_piece/', views.PieceCreateView.as_view(), name='create_piece'),

    # Graph
    path('factures_graphique/', views.factures_graphique,name='factures_graphique'),
    path('facturesFr_graphique/', views.facturesFr_graphique,name='facturesFr_graphique'),
    path('paiements_graphique/', views.paiements_graphique,name='paiements_graphique'),
    path('paiementsFr_graphique/', views.paiementsFr_graphique,name='paiementsFr_graphique'),


    # devise
    path('devise/<int:pk>/update/',
         views.deviseUpdateView.as_view(), name='devise_update'),
    path('devise/<int:pk>/delete/',
         views.deviseDeleteView.as_view(), name='delete_devise'),
    path('devise/', views.devise, name='devise'),
    path('create_devise/', views.deviseCreateView.as_view(), name='create_devise'),

    # taxe
    path('taxe/<int:pk>/update/', views.taxeUpdateView.as_view(), name='taxe_update'),
    path('taxe/<int:pk>/delete/', views.taxeDeleteView.as_view(), name='delete_taxe'),
    path('taxe/', views.taxe, name='taxe'),
    path('create_taxe/', views.taxeCreateView.as_view(), name='create_taxe'),

    # immob
    path('immob/<int:pk>/update/',
         views.immobUpdateView.as_view(), name='immob_update'),
    path('immob/<int:pk>/delete/',
         views.immobDeleteView.as_view(), name='delete_immob'),
    path('immob/', views.immob, name='immob'),
    path('create_immob/', views.immobCreateView.as_view(), name='create_immob'),

    # plan
    path('plan/<int:pk>/update/',
         views.planUpdateView.as_view(), name='plan_update'),
    path('plan/<int:pk>/delete/',
         views.planDeleteView.as_view(), name='delete_plan'),
    path('plan/', views.plan, name='plan'),
    path('create_plan/', views.planCreateView.as_view(), name='create_plan'),
    
#     Journal
    path('journal/<int:pk>/update/', views.journauxUpdateView.as_view(), name='journal_update'),
    path('journal/<int:pk>/delete/', views.journauxDeleteView.as_view(), name='delete_journal'),
    path('create_journal/', views.journauxCreateView.as_view(), name='create_journal'),
    path('journaux/', views.Journaux, name='journaux'),
    

]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
