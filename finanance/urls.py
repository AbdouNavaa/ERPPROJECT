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
    path('factsFr/<int:pk>/update/', views.FactFrUpdateView.as_view(), name='factFr_update'),
    path('factFr/<int:pk>/delete/', views.FactFrDeleteView.as_view(), name='delete_factFr'),
    path('factFr/', views.factFr, name='factFr'),
    path('create_factFr/', views.FactFrCreateView.as_view(), name='create_factFr'),
    
# FactCl
    path('factCl/<int:pk>/update/', views.FactClUpdateView.as_view(), name='factCl_update'),
    path('factCl/<int:pk>/delete/', views.FactClDeleteView.as_view(), name='delete_factCl'),
    path('factCl/', views.factCl, name='factCl'),
    path('create_fact/', views.FactClCreateView.as_view(), name='create_factCl'),
   
# Client
    path('client/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='delete_client'),
    path('clientList/', views.clientList, name='clientList'),
    path('create_client/', views.ClientCreateView.as_view(), name='create_client'),
   
# Fournisseurs
    path('fourn/<int:pk>/update/', views.FournUpdateView.as_view(), name='fourn_update'),
    path('fours/<int:pk>/delete/', views.FournDeleteView.as_view(), name='delete_fourn'),
    path('foursList/', views.foursList, name='foursList'),
    path('create_fours/', views.FoursCreateView.as_view(), name='create_fours'),


    path('GL/', views.GL, name='GL'),
    
# Paiements
    path('paiments/', views.Paiments, name='paiments'),
    path('paiments/<int:pk>/update/', views.PaiementUpdateView.as_view(), name='pie_update'),
    path('paiment/<int:pk>/delete/', views.PaiementDeleteView.as_view(), name='delete_pie'),
    path('create_pie/', views.PaiementCreateView.as_view(), name='create_pie'),
# Ecritures Comptable
    path('ecriture/', views.EcritureComp, name='ecriture'),
    path('ecrit/<int:pk>/update/', views.EcritUpdateView.as_view(), name='ecrit_update'),
# Pieces
    path('piece/<int:pk>/update/', views.PieceUpdateView.as_view(), name='piece_update'),
    path('piece/<int:pk>/delete/', views.PieceDeleteView.as_view(), name='delete_piece'),
    path('pieces/', views.Pieces, name='pieces'),
    path('create_piece/', views.PieceCreateView.as_view(), name='create_piece'),

] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
