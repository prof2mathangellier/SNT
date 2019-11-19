-----------------------
# Calculer avec Python
-----------------------

1.  Tapez les codes suivants dans la console Python. Les valeurs fournies par Python sont-elles justes ?
```python
>>> 5*5
>>> 15 - 4  
```
2. Tapez maintenant les codes suivants. Les valeurs calculées sont-elles justes ? Comment l'ordinateur parvient-il à choisir quelle opération faire d'abord ?
```python
>>> 9*9 + 2
>>> 2 + 9*9
>>> 12 - 2*0.2
>>> - 2*0.2 + 12
```

## Déroulement séquentiel

3. Evaluer de tête ces deux expressions. Donnent-elles le même résultat ?
```python
>>> 3 + 2*3 + 2
>>> (3+2) * (3+2)
```

## Règles de priorité

l'ordinateur n'évalue pas au hasard : il utilise les règles qu'on lui a fourni, qui correspondent aux règles de priorité que vous connaissez depuis longtemps :

	Multiplication et division prioritaires sur addition et soustraction
    Ordre d'apparition lorsqu'il faut différencier des multiplications ou des divisions
    Ordre d'apparition lorsqu'il faut différencier des additions ou des soustractions
    L'évaluation d'une expression située dans une parenthèse est toujours prioritaire

## Les différents type de nombres

4. Taper les expressions suivantes: le résultat d'une division.
```python
>>> 15 / 2
>>> 14 / 3 
>>> 14 / 2 
```
5. Réfléchir ensuite sur la réponse donnée. Taper dans la console.
```python
>>> type(14 / 2) 
>>> type(15 / 2) 
>>> type(14 / 3) 
```

### Vocabulaire à connaitre !

Les __entiers__ sont nommés des _integers_. C'est leur _type_: __`int`__

Les __nombres à virgules__ sont nommées: nombres à virgules flottantes. Leur _type_: __`float`__

## Bonne pratique pour un code clair

Vous avez peut-être remarqué que plusieurs lignes de calcul possèdent des espacements différents.  
Ceux-ci ne sont pas positionnés au hasard:  

Lorsqu'une expression ne contient que des opérateurs ayant la même priorité, on laisse un espace entre les différents termes.

Expressions correctement écrites :
```python
>>> 25 / 10
>>> 25 + 10 - 5
```
Lorsqu'une expression ne contient que des opérateurs ayant des priorités différentes, on ne place pas d'espace sur les opérateurs prioritaires:

Expressions correctement écrites:
```python
>>> 10 + 25*5
>>> 25/10 - 5
```
S'il faut des parenthèses, on ne rajoute pas d'espace au début ou à la fin de l'expression située dans les parenthèses.

L'expression dans la parenthèse est prioritaire sur la multiplication. Cette fois, on ne placera donc pas d'espace entre le `+` mais on en place autour du `*`:

Expressions correctement écrites :
```python
>>> (4+5) * (12+55)
```

6. Corriger ces expressions posant des problèmes de lecture :
```python
>>> (25+5)*5
>>> (30 - 5) * 2
>>> ( 5+2 ) * 7
>>> 7*( 25 + 5 )
```
Et pour les cas plus complexes ? On fait appel à son bon sens !

## Un nouvel opérateur

7. Taper les expressions suivantes qui illustrent un nouvel opérateur `**` : la puissance.
```python
>>> 3 ** 2
9
>>> 5 ** 4
625
>>> 2 ** 3
...
>>> 2 ** 0
...
```
8. Calculer l'expression suivante `5**2*5**2` : l'opérateur puissance a-t-il le même degré de priorité que la multiplication ? 
Faire le calcul étape par étape dans les trois cas possibles :
- aucune n'est prioritaire
- la multiplication est prioritaire
- la puissance est prioritaire.
9. Quelle est alors la forme la plus adaptée à la bonne compréhension de ce que fait le code parmis les 3 suivantes ?
```python
>>> 5 ** 2 * 5 ** 2 
625
>>> 5 ** 2*5 ** 2 
625
>>> 5**2 * 5**2 
625
```

------------
# Variables
------------

Le stockage d’une valeur dans une variable en langage Python se fait avec le signe `=` et avec la syntaxe suivante:
`nom_de_la_variable = valeur`.

La __casse__ est significative (les caractères majuscules et minuscules sont distingués).  
_Toto, toto, TOTO sont donc trois variables différentes. Soyez attentifs !_  
  
Prenez l’habitude d’écrire l’essentiel des noms de variables en caractères minuscules (y compris la première lettre). Il s’agit d’une simple convention, mais elle est largement respectée.  

## Affectation (ou assignation)

```python
>>>altitude = 176
>>>altitude
176
``` 

![diagramme d’état](diagrammepytutor.jpg)

## Typage des variables  

Le typage des variables sous Python est un typage __dynamique__, par opposition au typage statique.  

10. Taper le code suivant
```python
>>> largeur = 20
>>> longueur = 9.3
>>> surface = largeur * longueur
```
Puis, en essayant de deviner les réponses de l'interpréteur!  

```python
>>> type(largeur)
...
>>> type(longueur)
...
>>> type(surface)
...
```

11. On peut imposer le typage... Taper le code:
```python
>>> longueur = int(longueur)
>>> type(longueur)
...
>>> longueur
...
```

12. De la même manière: 
```python
>>> largeur=float(largeur)
>>> type(largeur)
...
>>> largeur
...
```

### Et le texte ?

 
On va gérer des chaînes de caractères (_strings_ en anglais).

On doit les fournir entourées de guillemets simples ' ' ou doubles " ".

13. Taper:
```python
>>> message = 'Hello World !'
>>> message
'Hello World !'
>>> type(message)
...
```
Sans guillemet, l'interpréteur ne peut pas comprendre que vous voulez lui fournir une chaînes de caractères :
```python
>>> message = Hello World !
  File "<pyshell>", line 1
    message = Hello World !
                        ^
SyntaxError: invalid syntax
```

## Affichage

14. Taper ces instructions ? Quelle est la différence entre les deux versions ?
```python
>>> 'Hello World !'
...
>>> print('Hello World !')
...
```

La première fois, l'expression est juste évaluée : la console affiche donc le résultat entouré de guillemets simples (' et ') pour indiquer qu'il s'agit d'une chaîne de caractères.

La seconde fois, on utilise la fonction `print()` qui permet d'afficher le contenu passé entre parenthèses. La différence ? Uniquement l'absence des guillements simples pour l'instant. Nous verrons néanmoins que la différence est un peu plus subtile...  

On peut se retrouver confronter à un problème... que faire si la chaine de caractères contient elle-même un `'` 

15. Taper le code suivant:
```python
>>> phrase = 'Angellier, l'antre du savoir'
```

Et l'interpréteur Python va refuser !!!
```python
>>> phrase = 'Angellier, l'antre du savoir'
  File "<pyshell>", line 1
    phrase = 'Angellier, l'antre du savoir'
                               ^
SyntaxError: invalid syntax
```

On ouvre avec un `'` mais notre phrase contient un `'`  ! Et l'interpréteur Python ne s'y retrouve plus... 

__Première méthode__ : utiliser des guillemets double:

16. Taper maintenant:
```python
>>> phrase = "Angellier, l'antre du savoir"
>>> phrase
...
>>> print(phrase)
...
```
__Deuxième méthode__ on utilise l’antislash `\` avant le signe que l'on désire échapper de notre chaine.
17. Taper:
```python
>>> phrase = 'Angellier, l\'antre du savoir'
>>> phrase
...
>>> print(phrase)
...
```

18. Proposer un code permettant d'afficher la phrase suivante: ' "Hello World", on l'utilise souvent en exemple! '

L’ antislash est un caractère spécial, il sert à coder des fonctions particulières...  
Par exemple, `\n` pour le retour à la ligne

19. Taper:
```python
>>> identite = 'prenom\nnom\nclasse'
>>> identite
...
>>> print(identite)
...
```   
Sans le print, l'interpréteur évalue la chaîne mais il donne simplement le contenu.   
Pour activer l'évaluation des caractères __à l'intérieur de la chaîne__, le print est obligatoire.

## Composition 

20. Taper:
```python
>>> nom = 'Angellier'
>>> prenom = 'Auguste'
>>> prenom + nom
...
>>> print(prenom + nom)
...
```
On appelle celà la __concaténation__ .

```python
>>> altitude = 176
>>> phrase = 'Le mont Cassel culmine à :' + altitude
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

21. Observez bien le message d'erreur... l'interpréteur Python ne s'y retrouve plus, __pouquoi?__

22. Taper:

```python
>>> altitude = 176
>>> phrase = 'Le mont Cassel culmine à :' + str(altitude)
>>> print(phrase)
...
```
On peut aussi procéder différemment en entrant la variable altitude comme une chaine de caractères!
```python
>>> altitude = '176'
>>> phrase = 'Le mont Cassel culmine à :' + altitude
>>> print(phrase)
...
```

23. Tenter de deviner ce que vont afficher les codes suivants.  
Tapez et exécutez le code une fois que vous pensez avoir la réponse.
```python
>>> 12 + 2
...
>>> 12 * 2
...
>>> '12' + '2'
...
>>> '12' * '2'
...
>>> '12' * 2
...
```

