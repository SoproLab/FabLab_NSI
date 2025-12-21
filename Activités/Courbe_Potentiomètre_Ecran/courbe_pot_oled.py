""" tracer une courbe sur l'écran OLED 132x28 où la position
du spot dépend de la tension aux bornes du potentiomètre """

import ssd1306
from machine import Pin, ADC, I2C
import time

# Initialiser le bus I2C pour communiquer avec l'écran
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)

# Déclarer une instance de classe SSD1306 _ comunication via le bus I2C
ecran = ssd1306.SSD1306_I2C(128,32,i2c)

# Déclarer une instance de classe ADC connectée au potentiomètre
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

# Déclarer une instance de classe Bouton Poussoir
bp = Pin(0, Pin.IN)

# convertir la valeur du potentiomètre en ordonnée relative
# -> [0 ; 4095) -> [0 ; 31 ]
pot_to_y = lambda val : 31-int(val/4095*31)
x = 0
y = pot_to_y( pot.read() )

print("Tournez le potentiomètre pour modifier la hauteur du spot sur l'écran ...")
print("Appuyer sur le bouton poussoir pour terminer.")
while bp.value() :
    y_memo = y
    y = pot_to_y( pot.read() )

    if x==127 :        
        ecran.scroll(-1, 0)
        ecran.pixel( x, y_memo, 0)
    else :
        x +=1
          
    ecran.pixel( x, y, 1)
    ecran.show()

    time.sleep_ms( 50 )
    
ecran.poweroff()