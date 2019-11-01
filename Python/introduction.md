----------------------------------
## Boîtes noires et pensée magique
----------------------------------

Nous vivons de plus en plus entourés de nombreuses "_boîtes noires_". Les scientifiques ont l’habitude de nommer ainsi les divers dispositifs technologiques que nous utilisons couramment, sans en connaître ni la structure ni le fonctionnement exacts. Tout le monde sait se servir d’un téléphone, par exemple, alors qu’il n’existe qu’un très petit nombre de techniciens hautement spécialisés qui soient capables d’en concevoir un nouveau modèle.

Ces boîtes noires existent dans tous les domaines, et pour tout le monde. En général, cela ne nous affecte guère, car nous pouvons nous contenter d’une compréhension sommaire de leur mécanisme pour les utiliser. Par exemple, la composition précise d’une pile électrique ne nous importe guère. Elle produit son électricité à partir d’une réaction chimique et elle sera épuisée après quelque temps d’utilisation. Inutile donc d’en savoir davantage.

Cependant que certaines boîtes noires deviennent tellement complexes que nous n’arrivons plus à en avoir une compréhension suffisante pour les utiliser tout-à-fait correctement dans n’importe quelle circonstance. Nous serons alors tentés de tenir des raisonnements faisant appel à l’intervention de propriétés ou de pouvoirs surnaturels pour expliquer ce que notre raison n’arrive pas à comprendre. Comme lorsqu’un magicien nous montre un tour de passe-passe, et que nous sommes enclins à croire qu’il possède un pouvoir magique, tant que nous n’avons pas compris le truc utilisé.

Du fait de leur extraordinaire complexité, les ordinateurs constituent bien évidemment l’exemple type de la boîte noire. Même si vous avez l’impression d’avoir toujours vécu entouré de moniteurs vidéo et de claviers, il est fort probable que vous n’ayez qu’une idée très confuse de ce qui se passe réellement dans la machine, par exemple lorsque vous déplacez la souris, et qu’en conséquence de ce geste un petit dessin en forme de flèche se déplace docilement sur votre écran. Qu’est-ce qui se déplace, au juste ? Vous sentez-vous capable de l’expliquer en détail, sans oublier (entre autres) les capteurs, les ports d’interface, les mémoires, les portes et bascules logiques, les transistors, les bits, les octets, les interruptions processeur, les cristaux liquides de l’écran, la micro-programmation, les pixels, le codage des couleurs … ?

De nos jours, plus personne ne peut prétendre maîtriser absolument toutes les connaissances techniques et scientifiques mises en œuvre dans le fonctionnement d’un ordinateur. Lorsque nous utilisons ces machines, nous sommes donc forcément amenés à les traiter mentalement, en partie tout au moins, comme des objets magiques, sur lesquels nous sommes habilités à exercer un certain pouvoir, magique lui aussi.

Par exemple, nous comprenons tous très bien une instruction telle que : « déplacer la fenêtre d’application en la saisissant par sa barre de titre ». Dans le monde réel, nous savons parfaitement ce qu’il faut faire pour l’exécuter, à savoir manipuler un dispositif technique familier (souris, pavé tactile …) qui va transmettre des impulsions électriques à travers une machinerie d’une complexité prodigieuse, avec pour effet ultime la modification de l’état de transparence ou de luminosité d’une partie des pixels de l’écran. Mais dans notre esprit, il ne sera nullement question d’interactions physiques ni de circuiterie complexe. C’est un objet tout à fait virtuel qui sera activé (la flèche du curseur se déplaçant à l’écran), et qui agira tout à fait comme une baguette magique, pour faire obéir un objet tout aussi virtuel et magique (la fenêtre d’application). L’explication rationnelle de ce qui se passe effectivement dans la machine est donc tout à fait escamotée au profit d’un « raisonnement » figuré, qui nous rassure par sa simplicité, mais qui est bel et bien une illusion.

Si vous vous intéressez à la programmation des ordinateurs, sachez que vous serez constamment confronté à des formes diverses de cette « pensée magique », non seulement chez les autres (par exemple ceux qui vous demanderont de réaliser tel ou tel programme), mais surtout aussi dans vos propres représentations mentales. Vous devrez inlassablement démonter ces pseudo-raisonnements qui ne sont en fait que des spéculations, basées sur des interprétations figuratives simplifiées de la réalité, pour arriver à mettre en lumière (au moins en partie) leurs implications concrètes véritables.

Ce qui est un peu paradoxal, et qui justifie le titre de ce chapitre, c’est qu’en progressant dans cette compétence, vous allez acquérir de plus en plus de pouvoir sur la machine, et de ce fait vous allez vous-même devenir petit à petit aux yeux des autres, une sorte de magicien !



Une autre façon de voir la chose : `14 = 4*3 + 2` . Ici, c'est le 4 qui est renvoyé.

Réfléchir ensuite sur la réponse donnée par les deux dernières expressions. Vérifier votre réponse en tapant l'expression dans la console.
```python

```
>>> 12 // 5

>>> 12 // 9
Priorité de l'opérateur //

L'opérateur // possède le même degré de priorité que la multiplication ou la division.

On dit parfois que l'opérateur // permet de faire des divisions entières.

Ce n'est pas entièrement vrai : si on tape >>> 14.0 // 3, on obtient 4.0 un nombre à virgule.

On préférera donc dire que l'opérateur // renvoie la partie entière de la division correspondante.

Lorsque nous parlerons des structures de données, nous verrons d'ailleurs qu'il faut être très vigilant lorsqu'on travaille avec des nombres à virgules sur un ordinateur. Un exemple pour vous en convaincre : 12.7 / 0.1 qui devrait donner 127.
```python

```
>>> 12.7 / 0.1
126.99999999999999


>>> 12.7 // 0.1
126.0
  
Vocabulaire

Nous venons de voir que Python ne gère pas de la même façon les nombres entiers et les nombres à virugles.

Les entiers sont nommés des integers.

Les nombres à virgules (même si on place 0 derrière la virgule) sont nommées des float : des nombres à virgules flottantes.

Ainsi :

    5 est un integer
    5.2 est un float
    5.0 est un float aussi.

06° Comment devrait être évaluer les expressions suivantes ? Donner votre réponse puis vérifier le calcul que Python va affecter sur ces floats.
```python

```
>>> 3*0.1 - 0.3

>>> 3*0.125 - 0.375

Nous verrons dans une activité spécifique pourquoi les flottants se comportent de cette façon. Pour l'instant, retenez simplement qu'on ne peut pas totalement faire confiance aux résultats incluant des flottants.

07° Taper les expressions suivantes qui illustrent un nouvel opérateur % : le modulo. On parle également de reste d'une division entière.
```python

```
>>> 14 % 3 donne 2.

En effet, 14 = 4*3 + 2. Ici, c'est le 2 qui est renvoyé.

>>> 11 % 5 donne 1.

En effet, 11 = 2*5 + 1. Ici, c'est le 1 qui est renvoyé.

Réflechir ensuite aux réponses attendues pour les quatre dernières expressions. Vérifier votre réponse en tapant l'expression dans la console.
```python

```
>>> 25 % 10

>>> 360 % 360

>>> 370 % 360

>>> 380 % 360

Encore une fois, il faut se méfier des résultats d'un modulo comportant des nombres à virgules.
Priorité de l'opérateur %

L'opérateur % possède le même degré de priorité que la multiplication ou la division.

Vous avez vu maintenant plusieurs lignes de calcul possèdant des espacements. Ceux-ci ne sont clairement pas positionnés au hasard :
Ecrire un code clair 1 : les espaces dans les expressions

Lorsqu'une expression ne contient que des opérateur ayant la même priorité, on laisse un espace entre les différentes termes :

Expressions correctement écrites :
```python

```
>>> 25 % 10
>>> 25 + 10 - 5


Expressions posant des problèmes de lecture :
```python

```
>>> 25%10
>>> 25+10+5
  

Lorsqu'une expression ne contient que des opérateurs ayant des priorités différentes, on ne place pas d'espace sur les opérateurs prioritaires :

Expressions correctement écrites :
```python

```
>>> 10 + 25*5
>>> 25/10 - 5


Expressions posant des problèmes de lecture :
```python

```
>>> 10+25*5
>>> 10 + 25 * 5
>>> 25/10-5
>>> 25 / 10 - 5

S'il faut des parenthèses, on ne rajoute pas d'espace au début ou à la fin de l'expression située dans les parenthèses.

L'expression dans la parenthèse est prioritaire sur la multiplication. Cette fois, on ne placera donc pas d'espace entre le + mais on en place autour du * :

Expressions correctement écrites :
>>>(25+5) * 5
>>> (4+5) * (12+55)


Expressions posant des problèmes de lecture :
```python

```
>>> (25+5)*5
>>> (25 + 5) * 5
>>> ( 25+5 ) * 5
>>> ( 25 + 5 ) * 5

Et pour les cas plus complexes ? On fait appel à son bon sens !

08° Taper les expressions suivantes qui illustrent un nouvel opérateur ** : la puissance. Trouver seul les réponses attendues non fournies puis vérifier votre réponse en tapant l'expression dans la console.
```python

```

>>> 3**2 donne 9.

>>> 4**2 donne 16.

>>> 5**2

>>> 6**2

>>> 2**1

>>> 2**2

>>> 2**3

>>> 2**4

>>> 2**5

>>> 2**6

>>> 2**7

>>> 2**8

09° Taper l'expression suivante : l'opérateur puissance a-t-il le même degré de priorité que la multiplication ? Faire le calcul étape par étape dans les trois cas possibles : aucune n'est prioritaire - la multiplication est prioritaire - la puissance est prioritaire. Lancer ensuite le code. Qui est prioritaire ? Quelle est alors la forme la plus adaptée à la bonne compréhension de ce que fait le code ?
```python

```

>>> 5**2*5**2

>>> 5 ** 2*5 ** 2

>>> 5**2 * 5**2
Correction ?

La bonne réponse étant 625, on voit clairement que l'opérateur puissance est prioritaire sur les autres.

La "bonne" façon d'écrire cette ligne est donc :
```python

```

>>> 5**2 * 5**2
625

Bon, c'est bien gentil les divisions entières et les restes de divisions entières, mais ça sert à quoi ? Les autres opérateurs ok, ça permet de calculer mais // et % ?

Pour vous montrer l'utilité de ces deux nouveaux opérateurs // et % prenons par exemple le cas d'un nombre ENTIER dont nous voulons obtenir l'unité, la dizaine et la centaine.

Posons ainsi clairement les données d'entrée voulues pour notre problème et les données de sortie qu'on veut produire :

    Entrée du problème : un nombre ENTIER positif

    Exemple d'entrée :  1234 
    Sorties du problème : un ensemble de nombre entier représentant l'unité, la dizaine et la centaine du nombre d'entrée.

    Sorties attendues pour l'entrée précédente :
         4  pour l'unité
         3  pour la dizaine
         2  pour la centaine

Nombre M = 	1 	2 	3 	4
La case code 	1000 	100 	10 	1
On obtient donc 	1x1000 = 1000 	2x100 = 200 	3x10 = 30 	4x1 = 4

Pour un humain, pas trop de problème pour sortir les réponses. Mais pour l'ordinateur ?

10° Taper ceci pour faire évaluer ce calcul. Correspond-t-il à l'unité de 1234 ?
```python

```

>>> 1234 % 10

11° Quelles expressions fournissent la dizaine de 1234 ? Quelle est la forme qu'on préférerait voir dans un code pour le rendre plus compréhensible pour un humain ?
```python

```

>>> 1234 // 10
>>> 1234 // 10 % 10
>>> (1234 // 10) % 10
>>> (1234//10) % 10
>>> (1234//10)%10
>>> 1234//10 % 10

12° Quelles expressions fournissent la centaine de 1234 ? Quelle est la forme qu'on préférerait voir dans un code pour le rendre plus compréhensible pour un humain ?
```python

```

>>> 1234 // 100
>>> 1234 // 100 % 10
>>> (1234 // 100) % 10
>>> (1234//100) % 10
>>> (1234//100)%10
>>> 1234//100 % 10

13° Et pour les milliers ?

Le stockage d’une valeur dans une variable en langage Pythonse fait avec le signe ” = ” et avec la syntaxenom_de_la_variable=valeur.Remarques :Le nom de la variable ne doit pas contenir d’espace d’où l’utilisation des tirets _Les nombres décimaux s’écrivent avec un point et non une virgule.
4 - Module Turtle

⇩ ⇧ ⤊

Bon, la console c'est sympa mais c'est un peu lassant lorsqu'on est habitué à de belles animations graphiques. L'intérêt c'est la rapidité et la simplicité.

Voyons maintenant un peu comment créer quelques dessins facilement avec l'un des modules les plus courants de Python dans l'apprentissage de la programmation : le module Turtle qui va vous permettre de vous mettre à la place d'une tortue qui dessine.

Cela nous permettra surtout de bien ancrer la notion de séquence dans l'exécution des instructions envoyées à l'ordinateur.

14° Utiliser les instructions suivantes une à une pour visualiser leurs effets.

Instruction n°1

>>> import turtle as trt

✱ En interne : importe dans l'interpréteur et en mémoire les codes permettant de créer la tortue.

✱ Visuellement : rien.

Instruction n°2

>>> crayon = trt.Turtle()

✱ En interne : on crée une variable crayon et on y place un objet-dessin basé sur le module Turtle.

✱ Visuellement : ouvre une fenêtre graphique et y place une flèche orientée vers la droite : la flèche symbolise le crayon.

Instruction n°3

>>> crayon.right(90)

✱ En interne : on agit sur crayon.

✱ Visuellement : la flèche tourne de 90° vers la droite.

Instruction n°4

>>> crayon.right(90)

✱ Visuellement : idem, on tourne de 90° vers la droite.

Instructions n°5

>>> crayon.forward(50)
>>> crayon.forward(100)
>>> crayon.forward(-150)

✱ En interne : on agit sur l'objet-crayon.

✱ Visuellement :

    la flèche avance de 50 pixels dans le sens indiqué et trace un trait noir.
    la flèche avance de 100 pixels et trace un trait noir.
    la flèche recule de 150 pixels par rapport au sens indiqué, et trace un trait noir.

Instructions n°6

>>> crayon.pencolor('red')
>>> crayon.forward(50)

✱ En interne : on change la couleur du crayon.

✱ Visuellement : on avance en traçant en rouge

Instructions n°7

>>> crayon.penup()
>>> crayon.forward(-200)
>>> crayon.pendown()
>>> crayon.forward(200)

✱ En interne : on empèche l'objet de tracer des traits (symboliquement, on lève la pointe du crayon virtuel.

✱ Visuellement : on recule sans faire de nouvelle trace

✱ En interne : on permet à nouveau à l'objet de tracer des traits (symboliquement, on abaisse la pointe du crayon virtuel sur la feuille.

✱ Visuellement : on avance en traçant un trait

Instructions n°8

>>> crayon.clear()

✱ Visuellement : on fait disparaître les traits créés par l'objet nommé crayon.

Instructions n°9

>>> crayon.home()

✱ Visuellement : on ramène le crayon au centre et on le replace en orientation vers la droite. Comme le crayon était 'posé', il a dessiné un trait.

15° Dessiner (avec crayon supposé exister) un carré de 200 pixels de côté en utilisant une séquence d'instructions précises et ordonnées. Les couleurs des côtés devront être red, pink, blue et orange.
Correction ?

16° Le dessin serait-il le même si on traçait les instructions dans un ordre aléatoire ?

Cette notion de séquence d'exécution est évidente ici puisqu'on tape les instructions une à une. Par contre, il faudra vous en souvenir lorsque nous commencerons à faire de vrais programmes : on doit placer les instructions dans l'ordre logique voulu pour réaliser les tâches demandées.
Quelques commandes disponibles avec Turtle

N'oubliez pas d'importer au préalable le module Turtle avec import Turtle as trt.

Voici quelques méthodes qu'on peut appliquer aux objets de classe Turtle, qu'on crée à l'aide de crayon = trt.Turtle().

Pour avancer : crayon.forward(50) permet d'avancer de 50.

Pour reculer : crayon.backward(50) permet de reculer de 50.

Pour tourner à droite : crayon.right(45) permet de tourner de 45° à droite.

Pour tourner à gauche : crayon.left(45) permet de tourner de 45° à gauche.

Pour aller faire un mouvement linéaire jusqu'au point de coordonnées (x,y) : crayon.setposition(x,y).

Pour faire un mouvement horizontal jusqu'à atteindre la valeur donnée en x : crayon.setx(x).

Pour faire un mouvement vertical jusqu'à atteindre la valeur donnée en y : crayon.sety(y).

Pour revenir au point d'origine : crayon.home().

Pour dessiner un cercle de rayon x : crayon.circle(x).

Pour dessiner un arc de cercle d'angle a et de rayon x : crayon.circle(x,a).

Pour tracer des polygones de "rayon" x possèdant y côtés : crayon.circle(x,360,y).

Pour placer un point de rayon x et de couleur précise : crayon.dot(x,"red").

Pour modifier la vitesse x, x variant de 1 à 10 : crayon.speed(x), x=0 veut dire pas d'animation.

Pour lever la pointe du crayon : crayon.penup().

Pour abaisser la pointe du crayon : crayon.pendown().

Pour changer la couleur du crayon : crayon.pencolor("red").

Pour augmenter la taille du crayon : crayon.pensize(5).

Cela nous suffira mais vous pouvez aller voir la documentation Python pour voir ce que le module peut faire d'autre : DOCUMENTATION TURTLE PYTHON.

17° Utilisez le temps qu'il vous reste pour réaliser le dessin le plus sympa possible.

Il existe notamment la possibilité de définir une couleur de remplissage avec crayon.fillcolor("yellow").

De signaler de commencer à gérer les traits comme faisant partie d'une forme à remplir : crayon.begin_fill().

De signaler la fin de la zone à remplir : crayon.end_fill().

Un exemple rapide :

>>> crayon.fillcolor("yellow")
>>> crayon.begin_fill()
>>> crayon.circle(50)
>>> crayon.end_fill()

Nous allons réutiliser Turtle un peu plus loin dans le cours car il permet vraiment de tester certaines choses et de rendre visuellement le résultat du code.

Ici, j'espère qu'il vous a permis de 'visualiser' que l'ordre des instructions est important.

Voici pour ce premier contact avec le Shell de Python.

Pour la plupart des activités, vous trouverez un récapitulatif des notions vues dans l'activité. Il ne s'agit pas vraiment d'un résumé, juste d'un rappel des notions vues.

Le menu global de Python vous permet ainsi d'atteindre la page globale des récapitulatif et la page des résumés, plus complets que les récapitulatifs.

Sur les premières activités, la différence entre récapitulatif et résumé n'est pas flagrant car la difficulté des notions abordées est plutôt faible.


La blague du jour : Le problème de la logique des informaticiens :

Ma mère : « Mon chéri, peux-tu aller au supermarché et me ramener une bouteille de lait. Si ils ont des œufs, prends en 6 ».

Je suis revenu avec 6 bouteilles de lait.

Ma mère a dit : « Pourquoi as-tu pris 6 bouteilles de lait ? »

J’ai répondu : « Car ils avaient des œuf … »



Pour comprendre cela, il faut bien entendu suivre ces instructions à la lettre :

    Si il n'y a d'oeuf, prendre 1 bouteille de lait.
    Si il y a des oeufs, prendre 6 bouteilles de lait

L'air de rien comprendre cela permet de comprendre qu'un ordinateur ne fait que suivre séquentiellement les instructions qu'on lui impose. Il ne tente jamais d'y mettre du sens et de tenter de comprendre ce que vous voulez réellement. Il exécute. Point.