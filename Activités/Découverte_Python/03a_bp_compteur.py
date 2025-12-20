"""
Activité 03-a : tant que ... compter
    Allumer une led différente à chaque appui sur le bouton poussoir
    Eteindre les trois leds après avoir appuyer trois fois sur le bouton poussoir.

Fonctionnalités de la carte mise en oeuvre :
    Utilisation du bouton poussoir et de trois leds.
    
Principes spécifique abordés dans ce script : 
    → Compter le nombre d'impulsions sur un bouton poussoir
    → si / sinon si / sinon
    
"""
from machine import Pin

bp  = Pin( 0, Pin.IN ) # connecté au GPIO 0 → entrée

led_v = Pin( 5, Pin.OUT ) # led verte connectée au GPIO 5 → sortie
led_j = Pin( 18, Pin.OUT ) # led jaune
led_r = Pin( 19, Pin.OUT ) # led rouge

# etat_bp <- lire l'état du bouton poussoir 

# Initialiser le compteur d'appuis à 0 ( cptr <- 0 )

# si le bouton est enfoncé alors ( Rappel : 0 → enfoncé / 1 → relâché )
    # Initialiser le compteur d'appuis à 1
    # allumer la led verte

# tant que le nombre d'appuis est inférieur à 3 faire
    
    # etat_bp <- état du bouton poussoir
    
    # Si le bouton est enfoncé (0)
        
        # ajouter 1 au compteur d'appuis
        
        # si le compteur est égal à 1
            # allumer la led verte
            
        # sinon si le compteur est égal à 2
            # allumer la led jaune
            
        # sinon (le compteur est égal à 3)
            # allumer la led rouge

# éteindre les trois led

print("Vous avez appuyé", cptr, "fois sur le bouton.") # Afficher la valeur affectée au compteur d'appuis