from machine import Pin
from neopixel import NeoPixel
from time import sleep

ruban = NeoPixel( Pin(12), 8) # déclarer la variable ruban pour interagir avec les led NeoPixel
ruban.timing = (190, 500, 820, 430) # (250,800,820,430) temporisations -> synchronisation des signaux
 
ruban[3] = ( 35, 35, 125) # Configurer la led d'indice 3 avec la couleur (35,35,125)
ruban.write() # envoyer l'information au ruban

sleep( 2 ) # attendre 2 s

for i in range(8) : # i prend pour valeurs [0,1,2,3,4,5,6,7]
    ruban[i] = (i*15, 105-i*15, 0) # configurer la couleur de chaque led
ruban.write() # envoyer la configuration au ruban

sleep( 1 )

for i in range(8) :
    ruban[i] = (0, 0, 0) # aucune lumière → éteindre le ruban
ruban.write()    
