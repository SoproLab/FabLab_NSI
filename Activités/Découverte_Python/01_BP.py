"""
Activité 01 : if ...
    Afficher l'état du bouton poussoir (relaĉhé ou enfoncé)

Fonctionnalités de la carte mise en oeuvre :
    Utilisation du bouton poussoir.
    
Principes spécifique abordés dans ce script : 
    → Configurer des GPIO en Entrée ( IN ) ( mode tout ou rien )
    → Lire l'état d'entrée d'un GPIO 
    → Utiliser les instructions conditionnelles if ,else 

Note : le bouton poussoir est relié à la broche 0. Cette broche est à l'état logique haut ( 1 ) si le bouton
est relâché et à l'état logique bas ( 0 ) lorsqu'il est enfoncé.
"""

from machine import Pin

bp  = Pin( 0, Pin.IN ) # connecté au GPIO 0 → entrée
led = Pin( 5, Pin.OUT ) # connectée au GPIO 5 → sortie

etat_bp = bp.value() # lire l'état du bp et affecter la réponse à la variable etat_bp

# si etat_bp == True alors (état haut)
    
    # Afficher dans la console : "Le bouton poussoir est relâché."

# sinon
    
    # Afficher dans la console : "Le bouton poussoir est enfoncé."

