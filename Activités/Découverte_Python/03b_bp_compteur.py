"""
Activité 03-b : tant que ... compter
    Allumer une led différente à chaque appui sur le bouton poussoir
    Eteindre les trois leds après avoir appuyer trois fois sur le bouton poussoir.

Fonctionnalités de la carte mise en oeuvre :
    Utilisation du bouton poussoir et de trois leds.
    
Principe spécifique abordé dans ce script : 
    → utilisation d'une temporisation pour éviter de compter plusieurs fois le même appui
    
"""
from machine import Pin
from time import sleep # temporisation

bp  = Pin( 0, Pin.IN ) # connecté au GPIO 0 → entrée

led_v = Pin( 5, Pin.OUT ) # led verte connectée au GPIO 5 → sortie
led_j = Pin( 18, Pin.OUT ) # led jaune
led_r = Pin( 19, Pin.OUT ) # led rouge

# Initialiser le compteur d'appuis à 0 ( cptr <- 0 )

# etat_bp <- lire l'état du bouton poussoir

# si le bouton est enfoncé  ( Rappel : 0 → enfoncé / 1 → relâché )
    # initialiser le compteur d'appuis à 1
    # allumer la led verte

# tant que le nombre d'appuis est inférieur à 3 faire
    
    # etat_bp <- lire l'état du bouton poussoir
    
    # Si le bouton est enfoncé
        
        # ajouter 1 au compteur
        
        # si le compteur est égal à 1
            # allumer la led verte
            
        # sinon si le compteur est égal à 2
            # allumer la led jaune
            
        # sinon (le compteur est égal à 3)
            # allumer la led rouge

    sleep(0.5) # Attendre 0.5s avant de détecter un nouvel appui


# éteindre les trois led

print("Vous avez appuyé", cptr, "fois sur le bouton.")