--------------------------------
# Les Fonctions
--------------------------------
## Fonction dites 'built-in'
	
Vous avez déjà rencontré des fonctions intégrées au langage lui-même, comme les fonctions print() ou input() par exemple. 
Ces fonctions _'built-in'_ sont relativement peu nombreuses : ce sont seulement celles qui sont susceptibles d’être utilisées très très fréquemment.
Il n’est pas possible d’intégrer toutes les fonctions imaginables dans le corps standard de Python, car il en existe virtuellement une infinité : nous allons d’ailleurs en créer nous-même de nouvelles.

## Définition d'une fonction

###Syntaxe
La syntaxe Python pour la définition d’une fonction est la suivante :
```python
def nom_fonction(liste de paramètres):
    bloc instructions
```
Vous pouvez choisir n’importe quel nom pour la fonction que vous créez, à l’exception des mots-clés réservés du langage, et à la condition de n’utiliser aucun caractère spécial ou accentué.  
L’instruction def est une instruction __composée__. La ligne contenant cette instruction se termine obligatoirement par un deux-points `:`, qui introduisent __un bloc d’instructions__ qui est précisé grâce à __l’indentation__. Par convention, l'indentation en Pyhon correspond à 4 espaces.  
Le bloc d’instructions constitue le corps de la fonction.
1. Taper ce code
```python
def conversion_ms_kmh(vitesse_en_ms):
    vitesse_en_km_h = vitesse_en_ms * 3600 / 1000 # 3600 secondes pour 1 heure et 1000 mètres pour 1 kilomètre
    return vitesse_en_km_h # la fonction 'retourne' la réponse
```
Il ne se passe rien...? Normal, la fonction est bien définie mais n'a reçu aucun argument en entrée!
2. Dans la console, taper:
```python
>>> conversion_ms_kmh(15)
54.0
```
Que s'est-il passé ?
3. Rechercher la formule permettant de convertir des degrés Farenheit en degrés Celcus.
Ecrire une fonction permettant de convertir des degrés Farenheit en degrés Celcus.
```python
def farenheit_celcus(temperature_f):
    temperature_c = (temperature_f-32)/1.8
    return temperature_c
```

---------------------------------
# Importer un module de fonctions
---------------------------------

On l'a dit, il y a relativement peu de fonctions 'built-in'... celà veut-il dire que nous derons toutes les créer nous-mêmes?
Non, heureusement! Un grand nombre de fonctions ont été définies et regroupées par 'famille' dans des fichiers séparés que l’on appelle des __modules__.

> donc __les modules sont des fichiers séparés qui regroupent un ensemble de fonctions.__

Il existe un grand nombre de modules pré-programmés qui sont fournis d’office avec Python.  
On importe un ou plusieurs modules en fonction de nos besoins... ce qui permet d'allèger le code!

>remarque: il est commode de découper un programme important en plusieurs fichiers de taille modeste pour en faciliter la maintenance. Une application Python typique sera alors constituée d’un programme principal, accompagné de un ou plusieurs modules contenant chacun les définitions d’un certain nombre de fonctions accessoires.

Le module `math`, par exemple, contient les définitions de nombreuses fonctions mathématiques telles que sinus, cosinus, tangente, racine carrée, le nombre pi, etc.  
Pour pouvoir utiliser ces fonctions, il vous suffit d’importer le module par son nom en tapant la ligne suivante :
```python
from math import *
```
Cette ligne indique à Python qu’il lui faut inclure dans le programme courant toutes les fonctions (c’est là la signification du symbole `*` ) du module math, lequel contient une bibliothèque de fonctions mathématiques pré-programmées.

4. Dans la console, taper:
```python
>>> pi
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
NameError: name 'pi' is not defined
```
le message d'erreur indique que `pi` n'est pas défini.
5. Taper maintenant:
```python
>>> from math import *
>>> pi
3.141592653589793
```
Peut-être direz-vous "mais pi, c'est un nombre, pas une fonction!!" oui,... mais non! C'est bien une fonction qui permet de calculer ce nombre!
6. écrire le script, que vous nommerez `demo_module_python.py`
```python
# Démo : utilisation des fonctions du module <math>
from math import *
nombre = 121       
print('racine carrée de ', nombre, ' = ', sqrt(nombre)) # en anglais, 'racine carrée' se dit 'square root'
```

L’exécution de ce script provoque l’affichage suivant :
```python
>>> %Run demo_module_python.py
racine carrée de 121 = 11.0
```

7. Exercices
	- exercice 3: Écrivez un script, que vous nommerez `ex3_python.py`, qui calcule l'hypoténuse d'un triangle rectangle dont l’utilisateur fournit les 2 mesures des deux autres côtés. Ce script contiendra une fonction...

```python
from math import *

def hypotenuse(cote1,cote2):
    hypotenuse = sqrt( cote1**2 + cote2**2)
    return hypotenuse

print('On calcule l\'hypoténuse d\'un triangle rectangle')
cote1 = float(input('entrer la longueur du premier côté : '))
cote2 = float(input('entrer la longueur du deuxième côté : '))
reponse = hypotenuse(cote1,cote2)
print('l\'hypoténuse du triangle rectangle est égale à :',reponse)
```