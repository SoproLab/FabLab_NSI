""" L'utilisation des interruptions : irq (interrutpion request)
permet d'éviter d'avoir à lire l'état de la broche.
C'est la fonction (routine) de gestion de l'interruption qui
va interagir avec le programme principal via l'affectation
d'une valeur spécifique à variable globale souvent appelée flag (drapeau) """

from machine import Pin

def irq_flag ( pin ): # routine (fonction) de gestion de l'interruption
    global bp_flag # variable globale
    bp_flag = True # modification de la valeur affectée au drapeau

bp = Pin( 0 , Pin.IN )
bp.irq( trigger=Pin.IRQ_RISING, handler = irq_flag ) # utilisation de l'interruption

bp_flag = False # déclaration de la variable globale (drapeau)

while not bp_flag :  # modification de bp_flag par la routine d'interruption
    pass

print("Ok pour interruption.")