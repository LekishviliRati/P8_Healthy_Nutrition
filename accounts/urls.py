from django.urls import path
from accounts import views

# NE FONCTIONNE PAS, POUR RAISON INCONNU A REESAAYER

urlpatterns = [
    path('accounts/profile/', views.profile, name="profile"),
]
