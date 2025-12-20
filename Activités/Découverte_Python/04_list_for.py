"""
Activité 04 : leds = [ ... , ... , ... ]
    Utiliser une variable de type list et accéder aux éléments de la liste en fonction de leur indice.

Fonctionnalités de la carte mise en oeuvre :
    Utilisation des trois leds.
    
Principes spécifiques abordés dans ce script : 
    → variable de type list   
"""
from machine import Pin
from time import sleep

bp  = Pin( 0, Pin.IN ) # connecté au GPIO 0 → entrée

led_v = Pin( 5, Pin.OUT ) # led verte connectée au GPIO 5 → sortie
led_j = Pin( 18, Pin.OUT ) # led jaune
led_r = Pin( 19, Pin.OUT ) # led rouge

# ====================================================================== attendre_appui_bp
def attendre_appui_bp ( bp )->bool :
    """
    Cette fonction attend un changement d'état du bouton poussoir.
    Si le bouton passe de l'état haut à l'état bas, cette fonction renvoie True
    Si le bouton passe de l'état bas à l'état haut, cette fonction renvoie False
    """
    # etat_bp <- lire létat actuel du bouton
    
    # mémorisation de l'état du bouton : etat_memo <- etat_bp
    
    # tant que le bouton n'a pas chagé d'état
        # etat_bp <- lire létat actuel du bouton

    # si le bouton a été enfoncé ( rappel : 0 → enfoncé / 1 → relâché )
        return ...  # → enfoncé
    # sinon
        return ...  # → relâché

# ================================================================== allumer
def allumer ( led ):
    # allumer la led
    # attendre 1 s
    # éteindre la led

# ================================================================== fonction principale

leds = [ led_v, led_j, led_r ] # affecter chaque led dans une variable de type list

allumer ( ... ) # appeler la fonction allumer(...) avec la leds d'indice 0 en argument

allumer ( leds[...] ) # appeler la fonction allumer(...) avec la led jaune en argument

# appeler la fonction allumer(...) avec la led rouge en argument

print("Appuyer sur le bouton poussoir pour la suite ...")
# attendre l'appui sur le bouton poussoir

# faire 2 fois :

    # Pour i allant de 0 à 3 exclu ( i prendra pour valeur successives 0, 1, 2 )
        
        # appeler la fonction allumer(...) et passer en argument la leds d'indice i
