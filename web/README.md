-----------------
# Le monde du Web
-----------------

Le monde du Web est construit sur la métaphore de la toile. Chacun des fils seraient la représentation des hyperliens, là où chaque point d'ancrage de la toile serait alors le représentant d'une page web.  
![image_toile](../images/toile.gif)
Le lien est un composant essentiel de la structure des documents. Il offre la possibilité de naviguer vers une autre ressource, et de mettre en relation des ressources similaires ou complémentaires. 


L'élément HTML ``` <link> ``` définit la relation entre le document courant et une ressource externe. Cet élément peut être utilisé pour définir un lien vers une feuille de style, vers les icônes utilisées en barre de titre ou comme icône d'application sur les appareils mobiles.

Pour lier une feuille de style externe, on inclut donc un élément ``` <link> ```de la forme suivante, à l'intérieur de l'élément ``` <head> ```:
```html
<link rel="stylesheet" type="text/css" href="main.css">
```
Dans cet exemple, on indique le chemin vers la feuille de style grâce à l'attribut href, l'attribut  rel possède une valeur stylesheet qui indique que c'est une feuille de style. rel signifie relationship qui correspond donc à la relation entre la ressource et le document courant. Il existe de nombreux types de liens possibles.
Certains types sont assez fréquents. Ainsi, pour l'icône présentant le site dans l'onglet, on trouvera :
<link rel="icon" href="favicon.ico">
Il existe différents types de relations pour préciser les icônes et qui permettent notamment de cibler certaines plateformes mobiles :
<link rel="apple-touch-icon-precomposed" sizes="114x114"
      href="apple-icon-114.png" type="image/png">
L'attribut sizes indique la taille de l'icône tandis que l'attribut type contient le type MIME de la ressource qui est liée. Ces attributs permettent alors au navigateur de sélectionner la ressource la plus adéquate.
On peut également fournir l'attribut media afin d'utiliser telle ou telle ressource lorsqu'une requête média est vérifiée. Ainsi, on pourra utiliser ce qui suit afin d'avoir une feuille de style utilisée à l'impression et une autre dédiée au mobile :
<link href="print.css" rel="stylesheet" media="print">
<link href="mobile.css" rel="stylesheet" media="screen and (max-width: 600px)">
Certaines fonctionnalités relatives à la sécurité sont également disponibles avec certains attributs de <link>. Dans cet exemple :
https://developer.mozilla.org/fr/docs/Web/HTML/Element/link

Pour résumer Internet est le réseau informatique mondial, c’est l’infrastructure globale, basée sur le protocole IP, et sur laquelle s’appuient de nombreux autres services. Dont le web. 




