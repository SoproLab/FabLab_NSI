"""
Activité 03-d : Utiliser une fonction
    Allumer une led différente à chaque appui sur le bouton poussoir
    Eteindre les trois leds après avoir appuyer trois fois sur le bouton poussoir.

Fonctionnalités de la carte mise en oeuvre :
    Utilisation du bouton poussoir et de trois leds.
    
Principes spécifiques abordés dans ce script : 
    → déplacer une partie du code dans une fonction    
"""
from machine import Pin

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
    
# ============================================================================ partie principale (main)
# etat_bp <- lire l'état du bouton poussoir 

# Initialiser le compteur d'appuis à 0 ( cptr <- 0 )

# si le bouton est enfoncé alors ( Rappel : 0 → enfoncé / 1 → relâché )
    # Initialiser le compteur d'appuis à 1
    # allumer la led verte

# tant que le nombre d'appuis est inférieur à 3 faire
        
    # si le compteur est égal à 1
        # allumer la led verte
        
    # sinon si le compteur est égal à 2
        # allumer la led jaune
        
    # sinon (le compteur est égal à 3)
        # allumer la led rouge

    # appui <- valeur renvoyée par la fonction attente_appui_bp( ... ) (Rappel : True ou False) 
    
    # tant que le bouton n'a pas été enfoncé 
        # appui <- valeur renvoyée par la fonction attente_appui_bp( ... )
        
    # ajouter 1 au compteur

# éteindre les led

print("Vous avez appuyé", cptr, "fois sur le bouton.")
