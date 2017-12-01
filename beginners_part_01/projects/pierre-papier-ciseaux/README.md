# Projet d'entraînement pierre-papier-ciseaux

Dans ce projet facultatif vous devez créer un simulateur en ligne de commande du jeu pierre papier ciseaux.

Ce projet vous fera retravailler les chapitres:
- variables
- types
- conditions
- lists

Vous anticiperez également sur les chapitres:
- fonctions
- boucles
- modules et namespaces

Par ailleurs il vous fera travailler:
- La création de conditions dans un algorithme
- L'intéraction avec l'utilisateur
- Le formatage de texte

## Consignes:

Vous devez créer un jeu en ligne de commande éxecutable comme ceci:
`python3 pierre_papier_ciseaux.py --manches 5`, 5 étant une option précisant le nombre de manches.

Une fois lancé, le jeu vous demande d'écrire:
- vous pouvez écrire: papier, feuille ou ciseaux pour jouer.
- quitter! pour quitter.
- historique! pour avoir l'historique des manches.

Vous pouvez utiliser la fonction `input` pour intéragir avec l'utilisateur (cf diapo 95 de la partie 1 du cours débutant).

Vous devez ensuite vérifier le retour de l'utilisateur:
- Si le retour de l'utilisateur est: `"pierre"` ou `"feuille"` ou `"ciseaux"`, vous allez jouer la manche et modifier le score et l'historique. Puis recommencez.
- Si le retour de l'utilisateur est: `"quitter!"`, vous affichez le score (on en reparlera plus loin) et vous quittez le script. (utilisez juste un `return` ou un `break` pour tout arrêter)
- Si le retour de l'utilisateur est: `"historique!"`, vous affichez le score et l'historique des manches (gagnez ou perdu). Puis recommencez.
- Si le résultat n'est rien de tout ça, recommencez.

Quand vous jouez la manche, vous devez générer une réponse aléatoire pour simuler un adversaire.
Pour se faire vous disposez de la fonction `random` (importée du module random).
Cette fonction génère un `float` aléatoire entre 0 et 1.
Ansi vous devez créer une réponse en se basant sur ce float:
- entre 0 et 0.33: "pierre"
- entre 0.33 et 0.66: "feuille"
- entre 0.66 et 1.0: "ciseaux"

Une fois la réponse aléatoire générée, comparez la réponse à celle de l'utilisateur et définissez s'il gagne ou perd.

S'il gagne vous augmentez le score de 1 (et gardez trâce de la manche dans l'historique).
S'il perd, le score ne change pas (mais gardez trâce de sa défaite dans l'historique).

En se basant sur ces informations, vous devez gérer le jeu et les affichages de ce dernier.

N'hésitez pas à ajouter de l'informations à l'utilisateur: nombre de manches jouées ect...


Pour réaliser votre application vous disposez d'un template de départ dans le fichier pierre_papier_ciseaux.py.

Vous devez coder entre les balises `# CODE HERE` et `# STOP HERE`.
N'hésitez pas à consulter le reste du template pour comprendre ce qu'il s'y passe.
Certaines variables sont déjà déclarées pour vous aidez.
Votre code se trouvera dans une boucle qui tournera jusqu'à ce que le nombre de manches précisées soit atteint.

Dans ce code vous pouvez vous en sortir en utilisant quelques unes des notions vues dans le cours (dans le désordre):
    - `list.append`
    - `x += 1`
    - `"word" in ["word", "answer", "thing"] `
    - `if`, `elif`, `else`
    - `x >= y`, `x <= y`, `x == y`
