## Utilisation du buzzer pour jouer une mélodie.  

### Dictionnaires des notes
Les fréquences des notes sont dans un dictionnaire ( ex  : { "La":440, ... }  
Il y a un dictionnaire par octave pour adapter les fréquences des notes.  
Ainsi, les notes sont classées dans une liste de deux dictionnaires  

### Jouer une mélodie  
Une mélodie est une liste de notes.  
La durée d'une note est indiquée par un tulple ou une note est jouée pendant une fraction d'un quantum de temps qt en millisecondes.  
Ainsi, pour jouer une blanche "La" (pendant 2 temps) on utilise ici un tuple ("La",qt*2)
Le changement d'octave se fait en "jouant" une note sans durée : ("Up",None) ou ("Down",None)  
Une pause de 50ms est jouée entre chaque note.  
Pour un silence d'un temps (un quantum), on joue une note (".", qt)  

### Extension possible 
Le logiciel MuseScode permet de scanner une partition et de générer un fichier xml qui contient les informations sur les notes.  
Il doit être possible ensuite de lire ce fichier xml pour interpréter les informations sur les notes et ainsi adapter les information pour faire jouer la partition à l'ESP32 ... ;-)  


S'il y a des mélomanes motivés, la perche est lancée ;-)
