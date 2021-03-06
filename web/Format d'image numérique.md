## Format d'image numérique couramment utilisé sur le web.

JPEG ou JPG :
--
Joint Photographic Experts Group est une norme qui définit le format d'enregistrement et l'algorithme de décodage pour une représentation numérique compressée d'une image fixe.
C'est un nom donné aux fichiers et images de MAC.  
JPG signifie exactement la même chose mais s'utilise en abrégé avec ces trois lettres pour faire référence aux fichiers ou images sur PC ou Windows.
Les fichiers JPEG et JPG sont donc en fait la même chose, il s'agit seulement de différencier s'il ont été généré sous MAC ou PC

GIF :
--
Le Graphics Interchange Format (littéralement « format d'échange d'images »). Ce format est un peu limité en couleur, et surtout, il a été longtemps été soumis à des droits d'utilisation par Unisys (propriétaire)

PNG
--
Le Portable Network Graphics est un format ouvert d'images numériques, qui a été créé pour remplacer le format GIF,
à l'époque propriétaire, et dont la compression était soumise à un brevet. 
Le PNG est un format sans perte spécialement adapté pour publier des images simples comprenant des aplats de couleurs.

La Transparence, ou couche Alpha
--
Les images peuvent posséder une quatrième couche, la couche alpha, en plus des trois couches rouge, verte et bleue. Cette couche ne modifie pas les couleurs de l'image et sert dans la plupart des cas à gérer la transparence de l'image, par exemple pour permettre de voir ce qu'il y a derrière l'image. Le format PNG peut prendre en charge une couche alpha. Le format GIF simule la transparence en utilisant une couleur considérée comme transparente. Dans les jeux vidéo, l'emploi de la couche alpha sur les textures permet par exemple de modifier leur réflexion ou leur transparence. 


```html
<div style="background-color: yellow">
  <p> image .png </p>
  <img src="emoji.png" alt="exemple image png">
  <p> image .jpg </p>
  <img src="emoji.jpg" alt="exemple image jpg">
</div>
```
![exemple image png jpg](exemple_png_jpg.png) 

En 1993, le navigateur web NCSA Mosaic a été le premier à permettre l'intégration d'images aux pages web : les formats GIF et XBM étaient supportés. Le support du format JPEG a été introduit en 1994 par Netscape Navigator.

Le manque de couleurs de GIF le rend peu adapté pour les dégradés très colorés, tandis que la compression avec pertes du JPEG provoque des flous sur les images dessinées directement sur ordinateur. 
Pour les images fixes, la répartition des rôles est donc : JPEG pour les photographies, GIF pour les images synthétiques.

Cependant, en réaction aux limitations de GIF, et aux exigences de royalties d'Unisys, un nouveau format a été proposé, PNG (Portable Network Graphics. PNG gère 16 millions de couleurs, une variation des degrés de transparence, et a un algorithme de compression plus élaboré, ce qui rend en général les images plus légères qu'en GIF, sans pertes.

PNG a toutefois mis longtemps à s'imposer, car non seulement les navigateurs anciens ne le supportaient pas (son support commence avec Internet Explorer 4), mais les navigateurs censés le supporter avaient de nombreux bugs dans ce domaine, surtout avec la transparence. 

