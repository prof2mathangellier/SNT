# Portable pixmap

## Extensions: .ppm, .pgm, .pbm, .pnm	

## Type de format: Format d’image matriciel

> Le portable pixmap file format (PPM), le portable graymap file format (PGM) et le portable bitmap file format (PBM) sont des formats de fichier graphique utilisés pour les échanges. 
Ils proposent des fonctionnalités élémentaires et sont utilisés pour convertir les fichiers de type pixmap, graymap et bitmap entre différentes plateformes.
Plusieurs applications désignent cet ensemble de formats comme le format PNM (portable anymap)

> Un logiciel de traitement d’image (tel que Gimp, ...) est capable de lire les fichiers portables anymap (.pbm, .pgm, .ppm, .pnm)

## Comme vu précédemment, pour transmettre une information, il faut d’abord préciser le protocole de transmission. 
Pour les images, sur le même principe, il faut préciser le système d’encodage de l’image.
Les fichiers PBM, PGM ou PPM sont composés sur la même base :  
• le nombre magique du format (deux octets) : il indique le type de format (PBM, PGM, ou
PPM) et la variante (binaire ou ASCII) ;  
• un caractère d’espacement (espace, tabulation, nouvelle ligne) ;  
• la largeur de l’image (nombre de pixels, écrit explicitement sous forme d’un nombre en caractères
ASCII) ;  
• un caractère d’espacement ;  
• la hauteur de l’image (idem) ;  
• un caractère d’espacement ;  
• les données de l’image : succession des valeurs associées à chaque pixel:  
* *l’image est codée ligne par ligne en partant du haut*   
* *chaque ligne est codée de gauche à droite.*  

# Création "manuelle" d'une image


\newpage

## Partie 1 : Création d'une image noir et blanc

Pour le format d'image .pbm (Portable BitMap), le nombre magique est `P1`.

Le fichier de l'image ressemble à :

```
P1
7 5
1 1 1 1 1 1 1
1 0 1 0 1 0 1
1 1 1 1 1 1 1
1 0 1 0 1 0 1
1 1 1 1 1 1 1
```

Ce qui donne :

 ![Image Noir et Blanc](./ImagePBM0.png)

L'image est de dimensions 7 sur 5 pixels (c'est tout petit, il faut donc zoomer, à 1600% par exemple, pour voir le résultat)

Les pixels noirs sont représentés par des 1 et les blancs par des 0

* Travail à effectuer : 
  + Coder l'image suivante :
  
  ![Une lettre en Noir et Blanc](./ImagePBM1.png)  
  
  Le fichier s'appellera ImageLettre.pbm
  
  + Coder ensuite : 
  
  ![SNT en Noir et Blanc](./ImagePBM2.png)
  
  Le fichier s'appellera ImageSntNB.pbm
  
* Questions à rendre sur feuille: 
  1. Pour une image de 7 sur 5 pixels, combien faut-il de bits (les 0 et les 1) pour le codage de l'image(on ne compte pas le nombre magique ni les dimensions)?
  2. Sachant qu'un octet est groupe de 8 bits, combien faut-il d'octets ?
  3. De manière générale, combien faut-il d'octets pour coder une image de L sur H pixels ?

------------------------------------------

\newpage


## Partie 2 :  Création d'une image en niveau de gris.

Pour une image en niveaux de gris, on peut utiliser le format d'image .pgm (Portable Grayscale Map), pour lequel le nombre magique est `P2`.

Le fichier de l'image ressemble à :

```
P2
7 5
9
0 9 9 0 0 9 9
1 8 8 1 1 8 8
2 7 7 2 2 7 7
3 6 6 3 3 6 6
4 5 5 4 4 5 5
```

Ce qui donne :

 ![Dégradé ](./ImagePGM0.png)

L'image est de dimensions 7 sur 5 pixels (c'est tout petit, il faut donc zoomer, à 1600% par exemple, pour voir le résultat)

A la troisième ligne, on indique la valeur maximale de gris. (Ce qui correspondra à du blanc).
Les pixels noirs sont représentés ici par des 0 et les blancs par la valeur maximale indiquée.


* Travail à effectuer : 
   + Coder l'image suivante : la valeur maximale sera 255
   
   ![Invaders Miroir](./ImagePGM1.png) 
   
   Le fichier s'appellera ImageInvader.pgm
          
* Questions à rendre sur feuille: 
  1. Pour une image de 7 sur 5 pixels, combien faut-il de nombre pour le codage de l'image(on ne compte pas le nombre magique ni les dimensions)?
  2. Sachant qu'un nombre entre 0 et 255 nécessite un octet pour être codé. Combien faut-il d'octets, pour coder l'image avec 256 niveaux de gris.
  3. De manière générale, combien faut-il d'octets pour coder une image de L sur H pixels avec 256 niveaux de gris. 

------------------------------------------

\newpage



## Partie 3 :  Création d'une image en couleur.

Pour une image en couleur, on peut utiliser le format d'image .ppm (Portable Pixel Map), pour lequel le nombre magique est `P3`.

Le fichier de l'image ressemble à :

```
P3
7 5
255
000 000 000  000 000 000  000 000 000  000 000 000  000 000 000
000 255 000  000 255 000  000 255 000  000 255 000  000 255 000
255 000 000  255 000 000  255 000 000  255 000 000  255 000 000
000 000 255  000 000 255  000 000 255  000 000 255  000 000 255
255 255 255  255 255 255  255 255 255  255 255 255  255 255 255
000 255 255  000 255 255  000 255 255  000 255 255  000 255 255
255 255 000  255 255 000  255 255 000  255 255 000  255 255 000
255 000 255  255 000 255  255 000 255  255 000 255  255 000 255
```

Ce qui donne :

 ![Image Couleur](./ImagePPM0.png)

L'image est de dimensions 7 sur 5 pixels (c'est tout petit, il faut donc zoomer, à 1600% par exemple, pour voir le résultat)

A la troisème ligne, on indique la valeur maximale de chaque couleur.

### Prinicpe du codage dans le système RGB (Red Green Blue)
Chaque pixel est codé par trois nombres.

Les pixels noirs sont représentés ici par des 0 et les blancs par la valeur maximale indiquée pour les trois couleurs.

Il est courant de prendre 255 comme valeur maximale. On aura alors la représentation suivante pour :

* noir : 0 0 0
* rouge : 255 0 0
* vert : 0 255 0
* bleu : 0 0 255
* jaune : 255 255 0
* ...
* pour connaître les nombres associés à une couleur, vous pouvez regarder ici : __[palette de couleur](https://www.palettedecouleur.com/)__

_**Remarque** : Dans le fichier texte, pour mieux visualiser, on peut écrire 000 au lieu de 0 et éventuellement passer des lignes pour aérer le fichier.


* Travail à effectuer : 
    + Coder l'image suivante avec les consignes : 
        - la valeur maximale sera 255.
        - chaque lettre aura une couleur différente
        - les dimensions seront 7 pixels de largeur et 18 en hauteur
        
      ![SNT en couleur](./ImagePPM1.png)
      
      Le fichier s'appellera ImageSntCouleur.ppm
         
    + Coder au moins les cinq premières lettres de votre nom en utilisant une couleur différente par lettre :   
        - la valeur maximale sera 255.
        - chaque lettre aura une couleur différente
        - l'écriture peut être horizontale ou verticale (comme dans l'exemple)
        - les dimensions seront à adapter.  
    Le fichier s'appellera ImageNom.ppm et sera déposé sur pronote
* Questions à rendre sur feuille: 
  1. Pour une image de 7 sur 5 pixels, combien faut-il de nombre pour le codage de l'image (on ne compte pas le nombre magique ni les dimensions)?
  2. Sachant qu'un nombre entre 0 et 255 nécessite un octet pour être codé. Combien faut-il d'octets, pour coder l'image en couleurs avec 256 niveaux pour chacune des trois couleurs?
  3. De manière générale, combien faut-il d'octets pour coder une image de L sur H pixels en couleurs avec 256 niveaux pour chacune des trois couleurs?
  4. Pour une image de 12 MégaPixels (soit 4000 sur 3000), combien faut-il d'octets pour coder l'image en couleurs? 
  5. Avec 256 niveaux par couleur, cela représente combien de couleurs possibles ?  
  *info : Sachant qu'un octet permet de coder les nombres de 0 à 255, et qu'un octet est un groupe de 8 bits. Chaque couleur nécessite 8 bits. Il faut donc 24 bits pour coder une couleur. C'est ce qu'on appelle la profondeur de couleur d'une image.*
 
------------------------------------------



