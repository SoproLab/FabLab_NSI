""" fonction de générateur de son """
from machine import Pin, PWM
from time import sleep_ms
from micropython import const

pin_buz = const( 2 ) # broche GPIO 2 connecté au contrôle du buzzer

# Dictioonnaire nom de la note, fréquence de vibration du buzzer
notes = [ { "Do":262, "Reb":277, "Re":294, "Mib":311, "Mi":330, "Fa":349, "Solb":370, "Sol":392, "Lab":415, "La":440, "Sib":466, "Si":494 },
          { "Do":523, "Reb":554, "Re":587, "Mib":622, "Mi":659, "Fa":698, "Solb":740, "Sol":784, "Lab":831, "La":880, "Sib":932, "Si":988 } ]
          

def jouer_melodie ( melodie:list ):
    """ buz est un GPIO configuré en PWM
    notes est une liste d'item d'un dictionnaire """
    buz = PWM(Pin( pin_buz ))
    buz.duty(0) # placer un silence de 50 ms entre deux notes
    octave = 0
    for note, dt in melodie :
        if note=="Up" : # changement d'octave
            octave += 1
        elif note=="Down" :
            octave -= 1
        elif note=="." : # Silence
            sleep_ms(dt)            
        else :
            buz.freq( notes[octave][note] )
            buz.duty(512) # duty [ 0 → 1023 ]
            sleep_ms(dt)
            buz.duty(0) # placer un silence de 50 ms entre deux notes
            sleep_ms(50)
    
qt = 500  # quantum de temps ( dt:noire ; qt//2:croche ; qt*2 : blanche ; ...)
# "." -> silence   ;  "Up", "Down" -> changement d'octave
# mélodie liste de tuples ( note, durée en ms )
jouer_melodie ( [(".",qt), ("Sib",qt//3), ("Fa",qt//3), ("Up",None), ("Mib",qt//3), ("Fa",qt//3), ("Mib",qt//3), ("Down",None), ("Sib",qt//3), ("Sib",qt//3), ("Fa",qt//3), ("Up",None), ("Mib",qt//3),
                 ("Fa",qt//3), ("Mib",qt//3), ("Down",None), ("Sib",qt//3), ("Sib",qt//3), ("Fa",qt//3), ("Up",None), ("Mib",qt//3), ("Fa",qt//2), ("Down",None), ("Sib",qt//6),("Sib",qt//6),("Sib",qt//3), ("Fa",qt//3), ("Fa",qt//3), ("Fa",qt//3),
                 ("Sib",qt*2), ("Up",None), ("Fa", qt*2),
                 ("Mib",qt//3), ("Re",qt//3), ("Do",qt//3), ("Sib",qt*2), ("Fa",qt),
                 ("Mib",qt//3), ("Re",qt//3), ("Do",qt//3), ("Sib",qt*2), ("Fa",qt),
                 ("Mib",qt//3), ("Re",qt//3), ("Mib",qt//3), ("Do",int(qt*2.5)), ("Down",None), ("Fa",qt//6), ("Fa",qt//6), ("Fa",qt//6),
                 ("Sib",qt*2), ("Up",None), ("Fa",qt*2),
                 ("Mib",qt//3), ("Re",qt//3), ("Do",qt//3), ("Sib",qt*2), ("Fa",qt),
                 ("Mib",qt//3), ("Re",qt//3), ("Do",qt//3), ("Sib",qt*2), ("Fa",qt),
                 ("Mib",qt//3), ("Re",qt//3), ("Mib",qt//3), ("Do",qt*2), ("Down",None), ("Fa",int(qt*3/4)), ("Fa",int(qt//4)),
                 ("Sol",int(qt*1.5)), ("Sol",qt//2), ("Up",None), ("Mib",qt//2), ("Re",qt//2), ("Do",qt//2), ("Down",None), ("Sib",qt//2),
                 ("Sib",qt//3), ("Up",None), ("Do",qt//3), ("Re",qt//3),("Do",int(qt*3/4)), ("Down",None), ("Sol", int(qt//4)), ("La",qt), ("Fa",int(qt*3/4)), ("Fa",int(qt//4)),
                 ("Sol",int(qt*1.5)), ("Sol",qt//2), ("Up",None), ("Mib",qt//2), ("Re",qt//2), ("Do",qt//2), ("Down",None), ("Sib",qt//4), ("Up",None), ("Fa",qt//4),
                 ("Fa",int(qt*3/4)), ("Do",qt//4), ("Do",qt*3)])