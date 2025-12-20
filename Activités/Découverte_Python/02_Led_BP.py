"""
Activité 02 : tant que ...
    Allumer la led verte.
    Eteindre la led lorsque le bouton poussoir est enfoncé.

Fonctionnalités de la carte mise en oeuvre :
    Utilisation du bouton poussoir et d'une led.
    
Principes spécifique abordés dans ce script : 
    → Configurer des GPIO en Entrée ( Pin.IN ) et en sortie ( Pin.OUT ) ( mode tout ou rien )
    → Commander l'état de sortie d'un GPIO 
    → Lire l'état d'entrée d'un GPIO 
    → Exécuter les mêmes instructions TANT QU'une condition est Vraie : while ... :
    
Note : le bouton poussoir est relié à la broche 0. Cette broche est à l'état logique haut ( 1 ) si le bouton
est relâché et à l'état logique bas ( 0 ) lorsqu'il est enfoncé.
"""

from machine import Pin

bp  = Pin( 0, Pin.IN ) # connecté au GPIO 0 → entrée
led = Pin( 5, Pin.OUT ) # connectée au GPIO 5 → sortie

led.on() # allumer la led verte

# lire l'état du bp et affecter la réponse à la variable etat_bp

# tant que le bp est à l'état haut ( 1 )
    
    # etat_bp <- lire l'état du bouton poussoir

led.off() # éteindre la led

