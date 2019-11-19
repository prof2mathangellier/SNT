from math import *

def hypotenuse(cote1,cote2):
    hypotenuse = sqrt( cote1**2 + cote2**2)
    return hypotenuse
    
print('On calcule l\'hypoténuse d\'un triangle rectangle')
cote1 = float(input('entrer la longueur du premier côté : '))
cote2 = float(input('entrer la longueur du deuxième côté : '))
reponse = hypotenuse(cote1,cote2)
print('l\'hypoténuse du triangle rectangle est égale à :',reponse)