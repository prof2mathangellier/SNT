# Client, serveurs et protocoles
---------------------------------
![client_serveur](client_serveur.svg)

# Le modèle client-serveur 	

Alice appelle son ami Edgar en salle B101 :

- "Edgar, peux tu me ramener quelque chose, s'il te plait ?"
- "Bien sûr Alice", répond Edgar, "que souhaites-tu?"
- "L'enveloppe rouge qui est dans le  tiroir de mon bureau."
- "Okay, j'y vais!" ... "La voilà Alice"
- "Merci Edgar"

Alice et Edgar viennent d'établir une relation sur un modèle _client/serveur_  :

* Alice et Edgar parlent la même langue. Sinon, il auraient bien du mal à se comprendre.
* Alice, _le client_, adresse une demande (une _requête_) à Edgar : amener une ressource dont elle a besoin.
* Edgar, _le serveur_, est prêt à l'aider mais il a besoin de savoir ce qu'elle veut (_la ressource_) et où est localisée cette ressource ( il n'est pas médium).  
Heureusement, Alice lui fournit tout ce dont il a besoin :
* Le _site_ où chercher est la salle B101
* Le _chemin d'accès_ pour arriver à la ressource est: _/site de la salle B101/dans le tiroir du bureau_.  
(C'est un chemin _absolu_ ou _relatif_, on en reparle après!)
* Il pourrait y avoir plusieurs choses dans ce tiroir, mais Edgar a précisé qu'il voulait l'enveloppe rouge.
* Si le document n'est pas à l'endroit précisé, Alice ne pourra que lui dire qu'il ne le trouve pas. Sinon, il pourra le lui ramener. 

>Sur internet, ce modèle **client/serveur** domine assez largement, même  s'il existe des cas où un ordinateur pourra jouer tour à tour le rôle de  client et le rôle de serveur (exemple le [peer to peer](https://www.journaldunet.fr/web-tech/dictionnaire-du-webmastering/1203399-p2p-peer-to-peer-definition-traduction-et-acteurs/)) très souvent, des ordinateurs (les clients) passeront leur  temps à demander des ressources à d'autres ordinateurs (les serveurs). 

![modèle client / serveur - source wikipédia - CCA](modele_client_serveur.png)

N'importe quel type d'ordinateur peut jouer le rôle de serveur!

>Dans le monde professionnel les serveurs sont des machines spécialisées, conçues pour fonctionner 24h sur 24h de la façon la plus fiable possible grace à des systèmes de sauvegardes pour éviter les pertes de données, et des moyens de protections très strictes.	
 						 
>Environ 6500 clients se connectent sur Google chaque seconde. Il serait impossible de gérer cela avec un seul serveur. Imaginez un restaurant où 6500 clients commandent leur repas en même temps au même serveur....

Google, Amazon ou encore Facebook possèdent un très grand nombre de  serveurs afin de pouvoir satisfaire les demandes des utilisateurs en  permanence. Ces entreprises possèdent d'immenses salles contenant chacune des centaines ou des milliers de serveurs: __les datacenters__  

![salle-serveur](salle_serveur.jpg) 				

Les serveurs sont spécialisés dans certaines tâches, par exemple, les serveurs qui envoient aux clients des pages au format HTML sont appelés _serveur web_. 

# HTTP et URL 

Pour surfer sur le web, un internaute utilise la plupart du temps un navigateur Internet (Firefox, Chrome, Edge, Opéra, Safari ...).
En fonction de ses clics ou de ses saisies, le navigateur va envoyer une demande au sujet de pages stockées sur des serveurs afin d'obtenir des renseignements à leurs sujets, ou de les afficher, ou de les récupérer : on dit qu'il fait une requête au serveur.  

De son côté, un  serveur attend les requêtes envoyés par les internautes.  
Lorsqu'il en reçoit une, il se contente de  répondre à la demande en envoyant du contenu.  

En général, le surf commence par **une adresse** (saisie manuellement dans la barre d'adresse ou obtenue en cliquant sur un lien)... il vous faut toujours une adresse pour aller quelque part. Pour  atteindre un _serveur http_, c’est pareil : on utilise une adresse.  

Une adresse est toujours constituée de la façon suivante : 

**protocole://adresse-du-serveur:port/chemin/ressource** 

Cette adresse est appelée **URL**  (**U**niform **R**esource **L**ocator, système universel de localisation des ressources) :

Pour que Alice et Edgar se comprennent, ils doivent suivre des règles (_parler la même langue et la politesse par exemple_).  
Pour Alice et Edgar, l' URL va se décomposer ainsi:
- protocole OPFP : On Parle Français Poliment
- adresse du serveur : salle B101 ( c'est là que se trouve Edgar)
- chemin: le bureau/le tiroir
- resource: l'enveloppe rouge

En informatique, c’est la même chose : il faut que navigateur et serveur suivent un protocole.  
Le protocole utilisé par navigateur et serveur pour communiquer, c'est le __protocole HTTP__ :  **H**yper**T**ext **T**ransfert **P**rotocol":  
* Le but du protocole HTTP est de permettre un transfert de  fichiers (essentiellement au format HTML (_la langue_)),  localisés grâce à une  URL, entre un navigateur (le client) et un serveur  Web.
* Ce protocole est un protocole de communication client-serveur et fonctionne sur le principe "requête-réponse".   

_Exemple :_
[http://www1.ac-lille.fr/pid32379/eleves.html](http://www1.ac-lille.fr/pid32379/eleves.html) 

* L'**adresse du serveur** est ... l'adresse où se situe le serveur. Dans notre exemple, c'est _www1.ac-lille.fr_, le serveur de l'académie de Lille. Cela correspond à la salle B101 pour Alice et Edgar.
* le **chemin** est l'endroit sur le serveur où est placée la ressource désirée.
	- Dans notre exemple, on ouvre le dossier _pid32379_ situé directement à __la racine__ du serveur. 
	- pour trouver la ressource nommée _eleves.html_...  
	à l'image du bureau et du tiroir dont on a parlé plus haut.

Si l'adresse n'est pas correcte, le serveur ne trouvera pas la ressource et viendra s'excuser platement... alors qu'il n'y peut rien... Il ne sous-entend même pas que vous vous êtes trompé d'adresse. Quel gentleman ce serveur.

[hum...](http://www1.ac-lille.fr/Hum.fr)
​	
Toutefois, ils sont robustes les serveurs : ils essaient d'afficher quelques choses même en cas d'erreur. Ils interpréteront correctement certaines adresses erronées où le protocole est manquant. Parfois il s'arrêteront à l'endroit où vous les avez conduits plutôt que de vous renvoyer une erreur.

# HTTPS

[https://www.education.gouv.fr/pid24301/annuaire-de-l-education.html](https://www.education.gouv.fr/pid24301/annuaire-de-l-education.html)

Le protocole **HTTPS** ajoute le **S** de **S**ecure au protocole HTTP.



![httpS - source wikipédia - CCA](https://upload.wikimedia.org/wikipedia/commons/e/e5/HTTPS_icon.png)



- Le HTTP n'est pas sécurisé : tout ordinateur présent entre le serveur et votre ordinateur peut lire en clair, c'est à dire sans aucun cryptage, tout ce que vous demandez et tout ce que vous recevez lorsque vous utiliser ce protocole.... C'est **extrêmement dangereux** : tous vos codes et identifiants sont à la merci des pirates !


- le HTTP**S** crypte toutes les requêtes et toutes les réponses en y ajoutant une couche de chiffrement :

  - le client — par exemple le navigateur Web — contacte un serveur  — par exemple Wikipédia — et demande une connexion sécurisée, en lui  présentant un certain nombre de méthodes de chiffrement de la connexion  (des [suites cryptographiques](https://fr.wikipedia.org/wiki/Suite_cryptographique)) .

  - le serveur répond en  confirmant pouvoir dialoguer de manière  sécurisée et en choisissant dans cette liste une méthode de chiffrement  et surtout, en produisant un certificat garantissant qu'il est bien le  serveur en question et pas un serveur pirate déguisé (on parle de  l'homme du milieu). 
    Ces [certificats électroniques](https://fr.wikipedia.org/wiki/Certificat_électronique)  sont délivrés par une autorité tiers dans laquelle tout le monde a  confiance, un peu comme un notaire dans la vie courante, et le client a  pu vérifier auprès de cette autorité que le certificat est authentique  (il y a d'autres variantes, mais c'est le principe général). 
    Le  certificat contient aussi un cadenas en quelque sorte (une clé dite  publique) qui permet de prendre un message et de le mélanger avec ce  cadenas pour le rendre complètement secret et uniquement déchiffrable  par le serveur qui a émis ce cadenas (grâce à une clé dite privée, que  seul le serveur détient, on parle de [chiffrement asymétrique](https://fr.wikipedia.org/wiki/Cryptographie_asymétrique)) .

  - cela permet au client d'envoyer de manière secrète un code (une [clé symétrique](https://fr.wikipedia.org/wiki/Clé_symétrique))  qui sera mélangé à tous les échanges entre le serveur et le client de  façon que tous les contenus de la communication — y compris l'adresse  même du site web, l'[URL](https://fr.wikipedia.org/wiki/Uniform_Resource_Locator) —  soient chiffrées. Pour cela on mélange le contenu avec le code, ce qui  donne un message indéchiffrable et à l'arrivée refaire la même opération  avec ce message redonne le contenu en clair, comme dans un miroir.

    

> En bref : serveur et client se sont reconnus, ont choisi une manière  de chiffrer la communication et se sont passé de manière chiffrée un  code (clé de chiffrement symétrique) pour dialoguer de manière secrète.  


