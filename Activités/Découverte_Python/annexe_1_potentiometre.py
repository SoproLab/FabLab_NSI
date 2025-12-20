from machine import Pin ,ADC

sensor = ADC ( Pin( 34 ) ) # potentiomètre connecté au GPIO 34 / LDR connectée au GPIO 35
sensor.atten ( ADC.ATTN_11DB ) # utiliser une atténuation de 11 dB pour effectuer une mesure 'correcte' 
 
val = sensor.read()  # lire l'état du Conv. Analog. Numerique et affecter la valeur renvoyée à la variable val
val_memo = val

print("Tournez le potentiomètre ...")
print("(Fin du script si la valeur obtenue est inférieure à 10)")
print(" ")
print("Valeur obtenue après mesure puis conversion :     ", end="" )
print("{:04d}".format(val), end="" ) # afficher la valeur sur 4 digits

while val > 10 :
    
    val = sensor.read() # lire l'état du Conv. Analog. Numerique
    
    if val < val_memo-20 or val_memo+20 < val :
        val_memo = val
        print("\b"*4, end="") # effacer la précédente mesure (\b → backspace
        print("{:04d}".format(val), end="" ) # mettre à jour l'affichage de la valeur