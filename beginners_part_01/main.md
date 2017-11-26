<!-- page_number: true -->
<!-- footer: Débuter en python - Partie 1 - https://git.io/vFxiU -->

# Débuter en python - Partie 1


###### Présenté par Guillaume Mousnier

<img src="./assets/python.png" style="width: 40%; margin-left: 8em;">


---

# C'est qui le mec au tableau ? 

**Guillaume Mousnier**

DataScientist | Développeur (Big Data) chez [TimeOne](http://timeonegroup.com)

Mail: mousnier.guillaume@gmail.com

Github: https://github.com/Gmousse

Langages: Python, JavaScript, Scala, R

--- 

# Prérequis

- Python3

> Installateur dispo sur https://www.python.org/ (windows, mac).
> Aussi dispo sur les gestionnaires de paquets linux.

- Un éditeur de texte de votre choix

> Atom (https://atom.io/ + https://atom.io/packages/language-python)
> VisualStudio (https://code.visualstudio.com/)

- Un terminal

---

# Plan

1. Introduction
2. Les variables
3. Les opérateurs
4. Les types primitifs
5. Les conditions
6. Les structures de données
7. Les boucles et autres types d'itérations
8. Les fonctions
9. Les erreurs
10. Les modules et les namespaces

---

# Introduction

## Présentation du langage 

Publié en 1991 par Guido van Rossum.

Langage de haut niveau interprété et dynamiquement typé.

Extrêmement polyvalent (sciences, web, ...).

Supporte plusieurs paradigmes (procédural, orienté-objet, fonctionnel...).

Dispose de fonctionnalités modernes (imports, asynchrone, parallélisation...) .

---

# Introduction

## Philosophie et Syntaxe

Le python suit une philosophie minimaliste ([Zen of Python](http://docs.python-guide.org/en/latest/writing/style/#zen-of-python)).

Se veut simple à lire et à écrire (et donc à maintenir).

Adopte un style compact, basé sur les indentations.

Favorise le EAFP (*it's easier to ask for forgiveness than permission*) plutôt que le LBYL (*look before you leap*).

---

# Introduction

## Lancer python

Lancer le cli (command-line interface) de python:

`python3`

Lancer un programme avec python:

`python3 /mon_chemin/mon_programme.py`
`python3 -m mon_module`


---


# Introduction 

## Les commentaires

En python on peut définir un commentaire (texte qui ne sera pas interprété dans votre programme) avec `#`:

````python3
# Ceci est un commentaire
"Ceci n'est pas un commentaire"

# Une petite opération
1 + 1  # Je crois que ça va faire 2!
````

On les utilisent pour ajouter des indications (doc) dans le code.

---


# Introduction 

## Afficher un résultat en python

La fonction `print` permet d'afficher un ou plusieurs résultats dans la console.

Ainsi:

````python3
print("Test")
print("Un et un font ", 1 + 1, "!")
````

Affichera dans la console (ou la sortie standard):
````python3
Test
Un et un font 2 !
````

---


# Introduction 

## Les lignes d'instructions

Normalement on déclare une instruction (statement) par ligne:

````python3
a + 4
a + 8
````

Il est possible mais non conseillé d'en déclarer plusieurs:

````python3
a + 4;a + 8
````

---

# Introduction 

## Les lignes d'instructions (2)

Ecrire une instruction (statement) sur plusieurs lignes est prohibé:
````python3
a + 
4
````

En effet celà provoque une erreur de parsing:

````
  File "<stdin>", line 1
    a + 
       ^
SyntaxError: invalid syntax
````

---


# Introduction 

## Les lignes d'instructions (3)

Pour des besoins de lisibilité on peut expliciter la continuation de la ligne via `\`:
````python3
1 + 4 + 5 + 7 + 8 + 9 + 10 + 545784 + 6 + 9 +\
4 + 1 + 3\
+ 2
````

Lors de l'appel d'une fonction, on peut également déclarer les paramètres sur plusieurs lignes:
````python
print(
    parametre1,
    parametre2, parametre3
)
````

---

# Introduction 

## Les indentations

Python utilise l'indentation pour séparer les blocs d'instructions d'un programme:

````python3
a = 1

if a != 1:
   print("WHAAAT")

print(a)
````

Il convient d'être rigoureux:

````
  File "<stdin>", line 1
    a + 8
    ^
IndentationError: unexpected indent
````

---

# Introduction 

## Les indentations (2)

La taille de l'indentation importe peu:

````python3
if a == 1:
           print("OUF")
````


Mais il faut être constant et rigoureux:

````python3
if a == 1:
    print("OUF")
           print("THAT WAS EXPECTED")
````

````
  File "<stdin>", line 3
    print("THAT WAS EXPECTED")
    ^
IndentationError: unexpected indent
````

---


# Introduction 

###### Exercice 01: Votre première commande en python
Instructions:
- Lancez le cli python.
- Affichez la phrase `Hello world !` en utilisant la fonction `print`.
- Affichez les opérations `2 + 2` et `4  - 1`  en utilisant une seule fonction `print`.

Résultats attendus:
- `Hello world !`
- `4 3`


---

# Introduction 

###### Exercice 02: Votre première programme
Instructions:
- Créez un fichier hello_world.py.
- Dans ce fichier affichez la phrase `Hello world !` en utilisant la fonction `print`.
- Executez le program hello_world.py avec python.

Résultats attendus:
- `Hello world !`

---

# Les variables 

## Déclarer une variable (1)

En python, la gestion des *objets* en mémoire et leur typage est dynamique.

Chaque valeur que vous allez utilisé se voit attribué un type et un id (localisation dans la mémoire):

````python3
print(128, id(128), type(128))
````

````
128 139810890631904 <class 'int'>
````

---


# Les variables 

## Déclarer une variable (2)

On peut affecter une valeur (e.g. 128) à un nom pour le manipuler à long terme:

````python3
x = 128
print(128, id(128), type(128))
print(x, id(x), type(x))
````

````
128 139810890631904 <class 'int'>
128 139810890631904 <class 'int'>
````

On vient alors de *déclarer la variable* x.

---

# Les variables 

## Déclarer une variable (3)

Affecter une valeur à une variable consiste à lui donner un alias.
On conserve l'id et le type de la valeur ainsi affectée.

On peut aussi affecter une variable à une autre variable:
````python3
x = 128
y = x    # équivalent de x = y = 128
print(x, y, id(x), id(y))
````

````
128 128 139810890631904 139810890631904
````

y possèdera alors l'identité de x.

---

# Les variables 

## Déclarer une variable (4)

On peut aussi déclarer plusieurs variables en même temps:

````python3
a, b = 35, 24
print(a, b)
````

````
35 24
````

---


# Les variables 

## Modifier une variable

Une variable peut varier dans le temps (!= constante).

On peut réattribuer la valeur assignée:

````python3
x = x + 10 # équivalent de x += 10
print(x, y, id(x), id(y))
````

````
138 128 139810890632224 139810890631904
````

La valeur de x change, son id aussi. 

y ne change pas car il ne partage plus le même id avec x. 

---


# Les variables 

## Modifier une variable (2)

**Attention!** Lorsque l'on travaille sur un objet complexe et que l'on effectue un passage par référence, on va impacter une variable qui partage cette objet.

````python
a = {"clef": "valeur"}; b = a
a["clef"] = "une autre valeur"
print(a, b)
print(id(a), id(b))
````

````
{'clef': 'une autre valeur'} {'clef': 'une autre valeur'}
139810876069496 139810876069496
````

Une modification par référence ne change pas l'id d'une valeur !!

---


# Les variables 

## Modifier une variable (3)

Il est souvent conseillé de ne pas écraser une variable mais d'en créer une nouvelle:

````python3
a = "Valeur"
b = a + "!"
````

Celà permet une lecture (et donc une maintenabilité) facilité du code.

---

# Les variables 

## Supprimer une variable

Si une variable est inutile, on peut la supprimer (forcant ainsi python à la supprimer de la mémoire):

````python3
a = "Valeur"
b = a
del a # on a plus besoin de a
print(b); print(a) 
````

Si on appelle la variable supprimée (on verra pourquoi plus tard):

````
Valeur # b n'est pas supprimé, on supprime juste a
NameError: name 'a' is not defined
````
Il faut néanmoins utiliser la suppression avec prudence!

---

# Les variables 

## Quid de la constante

La constante est un nom donné à une valeur qui ne doit pas changer au cours du temps.

On ne peut pas déclarer une *vrai* constante en python.

Par convention on crée juste une variable avec le nom en majuscule:

````python
MA_SUPER_CONSTANTE = 35 # DO NOT TOUCH OR JUST DIE
````

Et surtout on y touche pas!

---

# Les types primitifs

---

# Les opérateurs

## Les opérateurs mathématiques


---

# Les opérateurs

## Les opérateurs de comparaisons


---


# Introduction 

## Les fonctions built-in 

De nombreuses fonctions ou types sont disponibles par défaut dans le namespace (ou scope) de python, ce sont les **built-in functions**.

Par exemple, la fonction `print` est une fonction built-in.

La liste non exhaustive des built-in functions est disponible ici: https://docs.python.org/3/library/functions.html 

---

# Introduction 

## Les modules

Parfois on veut utiliser du code prêt à l'emploi autre que les built-ins. Ce sont les modules (1 module ~= 1 fichier python).

On peut ainsi importer différents modules dans son programme pour ajouter des fonctionnalités.

Certains modules sont préinstallés avec python: https://docs.python.org/3/py-modindex.html

---

# Introduction

## Importer un module

On peut importer un module dans son intégralité:
````python3
import math
print(math.pi)
````

Ou importer quelques parties du module:

````python3
from math import pi
print(pi)
````

Ou même tout importer d'un module:  **\/!\\**

````python3
from math import *
print(pi)
````

---

# Introduction

## Importer un module (2)

On peut aussi utiliser le système de modules pour découper son programme en plusieurs fichiers:

````python3
from .my_folder.my_file import my_function
````

On peut alors créer une arborescence de fichier `.py` contenant chacun une petite partie du code, que l'on importera au besoin.


---


# Introduction

## Comprendre les namespaces

Quand une fonction, une variable, ou un module est utilisable dans python, on dit qu'elle est présente dans le namespace (ou scope).

Les built-ins par exemple sont présents par défaut.

Pourcomprendre on utilise la fonction `dir` qui liste tout ce qui est dans le namespace:

````
print(dir())
````

`['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']`


---


# Introduction

## Comprendre les namespaces

Quand une fonction, une variable, ou un module est utilisable dans python, on dit qu'elle est présente dans le namespace (ou scope).

Les namespaces sont (~) une liste de noms de ce qui est accessible à un endroit donné du programme.

Les built-ins par exemple sont présents par défaut dans le namespace.

---


# Introduction

## Comprendre les namespaces (2)


Pour visualiser un namespace, on utilise la fonction `dir` qui liste tout ce qui est dans le namespace local:

````python3
print(dir())
````

`['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']`

Ainsi on voit que nos built-ins sont en effet présent dans le programme.

On peut même en voir le contenu: `print(dir(__builtins__))`

---

# Introduction

## Comprendre les namespaces (3)

Si on essaye d'accéder à une variable qui n'est pas présent dans le namespace local: 

````python3
print(pi)
````

Python nous signal que le nom `pi` n'est pas présent dans le namespace local: `NameError: name 'pi' is not defined`.

---

# Introduction

## Comprendre les namespaces (4)

Lorsque l'on importe un module, ou que l'on déclare une variable, python l'ajoute alors au namespace:

````python3
from math import pi
print(pi)
print(dir())
````
Ce qui rend l'accés à une variable ou à une fonction possible:
````
3.141592653589793
[..., 'pi']
````

---
