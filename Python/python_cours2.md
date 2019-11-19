--------------------------------
# IHM : Interface Homme Machine 
--------------------------------
## Affichage : la fonction print()

Nous avons déjà rencontré cette fonction.  
Précisons simplement ici qu’elle permet d’afficher n’importe quel nombre de valeurs fournies en arguments (c’est-à-dire entre les parenthèses).  
__Par défaut__, ces valeurs seront séparées les unes des autres par un espace, et le tout se terminera par un saut à la ligne.

Vous pouvez remplacer le séparateur par défaut (l’espace donc) par un autre caractère quelconque (ou même rien), grâce à l’argument « sep ». Exemple :
1. Tester les codes suivants:
```python
>>> print("Bonjour", "à", "tous")
Bonjour à tous
>>> print("Bonjour", "à", "tous", sep ="*") 
Bonjour*à*tous
>>> print("Bonjour", "à", "tous", sep ="") 
Bonjouràtous 
```

De même, vous pouvez remplacer le saut à la ligne terminal avec l’argument « end » :
```python
>>> print("zut")
	print("flute")
	print("etc...")
   zut
   flute
   etc...

>>> print("zut", end ="")
	print("flute", end ="")
	print("etc...", end ="")
   zutfluteetc...
```

## Interaction avec l'utilisateur : la fonction input()

La plupart des scripts élaborés nécessitent à un moment ou l’autre une intervention de l’utilisateur (entrée d’un paramètre, clic de souris sur un bouton, etc.). La méthode la plus simple consiste à employer la fonction intégrée input(). Cette fonction provoque une interruption dans le programme courant. L’utilisateur est invité à entrer des caractères au clavier et à terminer avec Enter. Lorsque cette touche est enfoncée, l’exécution du programme se poursuit, et la fonction fournit en retour une chaîne de caractères correspondant à ce que l’utilisateur a entré. Cette chaîne peut alors être assignée à une variable quelconque, convertie, etc.

On peut invoquer la fonction input en laissant les parenthèses vides, mais le plus souvent on y placera un message explicatif destiné à l’utilisateur.

2. Taper:
```python
>>> prenom = input("Entrez votre prénom : ")
	print("Bonjour,", prenom)
Entrez votre prénom : Auguste
Bonjour, Auguste
```
## ATTENTION : Remarque importante

La fonction input renvoie toujours une chaîne de caractères, donc de type string !

3. Essayer:
```python
>>> age = input("indiquer votre age: ")
	type(age)
<class 'str'>
```
Cela pose quelques problèmes...
4. Taper:
```python
>>> age = input("indiquer votre age: ")
	print ('vous avez ',age,' ans')
	print ('l\'année prochaine, vous aurez ',age + 1,' ans')
indiquer votre age: 15
vous avez  15  ans
Traceback (most recent call last):
  File "<pyshell>", line 3, in <module>
TypeError: can only concatenate str (not "int") to str
```
On a déjà rencontré cette erreur. Si vous souhaitez que l’utilisateur entre une valeur numérique, vous devrez donc convertir la valeur entrée en une valeur numérique du type qui vous convient.

5. Proposer un code pour corriger l'erreur.
```python
>>> age = input("indiquer votre age: ")
	age=int(age)
	print ('vous avez ',age,' ans')
	print ('l\'année prochaine, vous aurez ',age + 1,' ans')
indiquer votre age: 18
vous avez  18  ans
l'année prochaine, vous aurez  19  ans
```

-------------------------------------------------
# Utilisation de nos connaissances dans un script
-------------------------------------------------
>Premiers scripts, ou comment conserver nos programmes

Nous n’avons utilisé jusqu’ici que le mode interactif de l’interpréteur Python. 
Cela a permis d’apprendre très rapidement les bases du langage, par expérimentation directe. Cette façon de faire présente toutefois un gros inconvénient : toutes les séquences d’instructions que vous avez écrites disparaissent irrémédiablement dès que vous fermez l’interpréteur.  
Nous allons voir comment stocker les instructions dans un programme. Cela nous évitera d'avoir à retaper des instructions que nous avons déjà exécutées à chaque fois qu'on veut refaire la même chose, et surtout de les sauvegarder...

## Créer un script
6. recopier le code précédent dans la fenêtre du haut de THONNY (pour l'instant, elle se nomme 'untitled')
```python
age = input("indiquer votre age: ")
age=int(age)
print ('vous avez ',age,' ans')
print ('l\'année prochaine, vous aurez ',age + 1,' ans')
```
7. Utiliser `File - Save as` pour enregistrer le fichier (qui doit être un .py) dans votre dossier personnel.
8. Exécuter le programme en utilisant la flèche verte `Run` (ou directement la touche F5).
Si vous avez nommé votre fichier `exemple.py`Vous devriez voir ceci s'afficher dans le shell de Thonny 
```python
>>> %Run exemple.py
```
Puis votre script va s'exécuter...

## Les commentaires, la mise en forme.
L’un des points fondamentaux de la programmation est la clarté : votre code sera certainement un jour utilisé ou modifié par quelqu’un d’autre. Ou par vous même quelques mois ou années plus tard.

Lorsqu’un programme est simple, pas besoin d’explication.  
Mais lorsque le code commence à gonfler, on regrette souvent de ne plus savoir pourquoi on a codé ceci ou cela quelques semaines avant… Les commentaires servent à donner des explications sur ce que fait le code ou sur ce que doit contenir telle ou telle variable.  
Autre cas courant : la personne qui lit le code n’est pas celui qui l’a codé (votre professeur!).  
Sans commentaire, pas facile de comprendre le but de chaque ligne de code.

>Point important : les commentaires sont destinés à un lecteur humain. L'interpréteur Python ne tentera pas de les exécuter.  
Pour rajouter un commentaire, on utilise simplement le caractère dièse `#`

```python
# Toute cette ligne est un commentaire, on aime bien écrire 'Hello World' par exemple.
print('Hello World') # vous verrez bien que ceci n'est pas interprété, uniquement Hello World sera écrit
print('Mais attention, cette ligne ne contient pas de # commentaire')
```

Autre exemple, on donne des précisions sur ce que fait notre code et pourquoi on le fait...
```python
age = input("indiquer votre age: ") # age sera donc de type 'str'
age=int(age) # on convertit age en nombre entier
print ('vous avez ',age,' ans')
print ('l\'année prochaine, vous aurez ',age + 1,' ans') # age + 1 est donc une addition d'entiers
```
9. Exercice: écrire un script, que vous nommerez `exo_python.py` qui répond au problème suivant:
_"Je dispose d'un budget de 77 euros. Je dois acheter des paquets de biscuits valant 4 euros l'unité. Combien de paquets vais pouvoir acheter?"_
```python
budget = 78 # le budget pour acheter les paquets de biscuits
unite = 8 # le prix à l'unité
nombre = budget / unite # le nombre de paquets à acheter
nombre = int(nombre) # pour avoir un nombre entier
print('Je vais pouvoir acheter ',nombre,' paquets de biscuits')
```

11. Exercices
	- exercice 1: Écrivez un script, que vous nommerez `ex1_python.py`, qui calcule le périmètre et l’aire d’un rectangle quelconque dont l’utilisateur fournit les 2 côtés.

	- exercice 2: Écrivez un script, que vous nommerez `ex2_python.py`, qui convertisse en mètres par seconde une vitesse fournie par l’utilisateur en km/h.

12. Écrivez un script, que vous nommerez `coureur_python.py`, qui convertisse en 'minutes','secondes' par kilomètre une distance et un temps en heure, minutes et secondes, fourni par un coureur qui souhaite réaliser cette distance avec un objectif de temps.
