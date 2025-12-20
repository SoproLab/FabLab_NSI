"""
Activité 03-c : tant que ... compter
    Allumer une led différente à chaque appui sur le bouton poussoir
    Eteindre les trois leds après avoir appuyer trois fois sur le bouton poussoir.

Fonctionnalités de la carte mise en oeuvre :
    Utilisation du bouton poussoir et de trois leds.
    
Principes spécifiques abordés dans ce script : 
    → algorithme de gestion de changement d'état avec mémorisation pour compter le nombre d'appuis
    → double condition  if ...  and ... :    
"""
from machine import Pin

bp  = Pin( 0, Pin.IN ) # connecté au GPIO 0 → entrée

led_v = Pin( 5, Pin.OUT ) # led verte connectée au GPIO 5 → sortie
led_j = Pin( 18, Pin.OUT ) # led jaune
led_r = Pin( 19, Pin.OUT ) # led rouge

# Initialiser le compteur d'appuis à 0 ( cptr <- 0 )

""" L'algorithme de gestion du changement d'état consiste à mémoriser
l'état du bouton pour détecter lorsqu'il y a un changement d'état
entre l'état précédent et l'état actuel. """

# etat_bp <- lire l'état du bouton poussoir
# etat_memo <- etat_bp → mémoriser l'état actuel du bouton dans la variable etat_memo

# si le bouton est enfoncé ( Rappel : 0 enfoncé / 1 relâché )
    # Initialiser le compteur d'appuis à 1
    # allumer la led verte
    

# tant que le nombre d'appuis est inférieur à 3 faire
    
    # etat_bp <- lire l'état du bouton poussoir
    
    # Si le bouton a changé d'état et qu'il est enfoncé alors 
        
        # mémoriser le nouvel état du bouton : etat_memo <- etat_bp
        
        # ajouter 1 au compteur
        
        # si le compteur est égal à 1
            # allumer la led verte
            
        # sinon si le compteur est égal à 2
            # allumer la led jaune
            
        # sinon (le compteur est égal à 3)
            # allumer la led rouge

    # sinon si le bouton a changé d'état ( il a donc été relâché )
        
        # mémoriser le nouvel état du bouton : etat_memo <- etat_bp

# éteindre les led

print("Vous avez appuyé", cptr, "fois sur le bouton.")