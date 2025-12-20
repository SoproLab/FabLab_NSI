from machine import Pin, PWM
from time import sleep, sleep_ms # attente en secondes, idem mais en millisecondes

buz = PWM ( Pin(2) ) # contrôle de la broche 2 en mode vibration

buz.freq( 440 ) # fréquence du signal 440 Hz
sleep(1)
buz.duty(10) # diminuer l'intensité sonore à 10
sleep(1)
buz.duty(0) # intensité sonore à 0 → silence 
sleep(1)

notes = { 'DO':262, 'RE':294, 'MI':330, 'FA':349, 'SOL':392, 'LA':440, 'SI':494 }
buz.duty(35)
for key in ['DO', 'RE','MI', 'FA', 'SOL', 'FA', 'MI', 'RE', 'DO' ]:
    buz.freq( notes[key] )
    sleep_ms(250 ) # attendre 250 ms entre chaque note
    
buz.deinit() # désactiver le buzzer

