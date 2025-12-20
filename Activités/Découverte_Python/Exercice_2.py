"""
Exercice 2 :
Utiliser la fonction randint(0,2) disponible dans la bibliothèque random
pour allumer aléatoirement chacune des leds pendant une durée de 0.3 s et
ceci jusqu'à ce que l'utilisateur appuie sur le bouton poussoir afin d'éteindre les leds.
"""

from random import randint # importer la fonction randint
from machine import Pin
from time import sleep

led_v = Pin( 5, Pin.OUT ) # led verte connectée au GPIO 5 → sortie
led_j = Pin( 18, Pin.OUT ) # led jaune
led_r = Pin( 19, Pin.OUT ) # led rouge

bp  = Pin( 0, Pin.IN ) # connecté au GPIO 0 → entrée

# ================================================================== allumer
def allumer ( led ):
    # allumer la led
    # attendre 0.3 s
    # éteindre la led

# ================================================================== programme principal ( main )

# affecter chaque led dans une variable de type list ( leds )

# etat_bp <- lire l 'état du bouton poussoir
# etat_memo <-etat_bp → mémoriser l'état actuel du bouton

# appui <- False  → affecter la valeur False à une variable ( appui )

# tant que appui est à False faire
    
    # etat_bp <- lire l 'état du bouton poussoir

    # Si le bouton a changé d'état
        # mémoriser le nouvel état du bouton
        
        # le bouton a été enfoncé
            # appui <- True   →  mettre fin à la boucle tant que
    
    # n <- générer un nombre entier aléatoire compris entre 0 et 2 inclus.
    # allumer la led d'indice n pendant 0.3s

    
