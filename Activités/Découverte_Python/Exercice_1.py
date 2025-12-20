"""
Exercice 1 :

Allumer la led verte tant que le bouton poussoir est enfoncé.
Éteindre la led verte lorsqu'il est relâché

"""

from machine import Pin

bp  = Pin( 0, Pin.IN ) # connecté au GPIO 0 → entrée
led = Pin( 5, Pin.OUT ) # connectée au GPIO 5 → sortie

led.off()

# attendre que le bouton poussoir soit enfoncé

# allumer la led verte

# attendre que le bouton poussoir soit relâché

# éteindre la led verte