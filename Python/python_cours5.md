# Instructions répétitives 

L’une des tâches que les machines font le mieux est la répétition sans erreur de tâches identiques. Il existe bien des méthodes pour programmer ces tâches répétitives. Les boucles de répétition !

## l'instruction de boucle `while` 
```py
>>> a = 0
>>> while a < 7:     # (n'oubliez pas le double point !)
...     a = a + 1     # (n'oubliez pas l'indentation !)
...     print(a)
```
Que se passe-t-il ? Prenez le temps d’ouvrir votre cahier et d’y noter cette série de commandes. Décrivez aussi le résultat obtenu, et essayez de l’expliquer de la manière la plus détaillée possible.  

Le mot while signifie « tant que » en anglais. Cette instruction utilisée à la seconde ligne indique à Python qu’il lui faut répéter continuellement le bloc d’instructions qui suit, tant que le contenu de la variable a reste inférieur à 7.  



Nous avons ainsi construit notre première boucle de programmation, laquelle répète un certain nombre de fois le bloc d’instructions indentées. Voici comment cela fonctionne.  

- Avec l’instruction while, Python commence par évaluer la validité de la condition (ici a < 7).
- Si la condition se révèle fausse, alors tout le bloc qui suit est ignoré et l’exécution du programme se termine.
- Si la condition est vraie, alors Python exécute tout le bloc d’instructions constituant le corps de la boucle:   
	c’est-à-dire :
    * l’instruction a = a + 1 qui ajoute une unité au contenu de la variable a.
    * l’appel de la fonction print pour afficher la valeur courante de la variable a.  

    Lorsque ces deux instructions ont été exécutées, nous avons assisté à une première itération, et le programme __boucle__, c’est-à-dire que l’exécution reprend à la ligne contenant l’instruction while. La condition qui s’y trouve est à nouveau évaluée, et ainsi de suite.
    Dans notre exemple, si la condition a < 7 est encore vraie, le corps de la boucle est exécuté une nouvelle fois et le bouclage se poursuit.

```py
from turtle import *
 
def carre(cote):
    '''fonction qui dessine un carré de côtés déterminés'''
    compteur = 0 #on initialise un compteur
    while compteur < 4:
        forward(cote)
        right(90)
        c = c + 1
```
## l'instruction de boucle `for`  

Le parcours d’une séquence est une opération très fréquente en programmation. Pour en faciliter l’écriture, Python vous propose une structure de boucle plus appropriée que boucle `while` , basée sur le couple d’instructions `for ... in ...` et la fonction `range()`:

```py
from turtle import *
 
def carre(cote):
    '''fonction qui dessine un carré de côtés déterminés'''
    for compteur in range(4):
        forward(cote)
        right(90)
```


>Les instructions de boucle amorcent une instruction composée. Le double point à la fin de la ligne introduit le bloc d’instructions à répéter, lequel doit obligatoirement se trouver en retrait. Comme vous l’avez appris au chapitre précédent, toutes les instructions d’un même bloc doivent être indentées exactement au même niveau (c’est-à-dire décalées à droite de 4 espaces).