<!-- page_number: true -->
<!-- footer: Débuter en python - Partie 2 - https://git.io/vbY68 -->

# Débuter en python - Partie 2


###### Présenté par Guillaume Mousnier

<img src="./assets/python.png" style="width: 40%; margin-left: 8em;">

---


# Plan

1. Les erreurs
2. Les modules et les namespaces
3. Les fichiers
4. Structure d'un projet

---

# Les erreurs

## Les types d'erreurs / exceptions

Python est très expressif et n'hésite pas à lever des erreurs:
````
SyntaxError # Erreur de parsing
IndentationError # Mauvaise indentation
NameError # Variable non définie
TypeError # Erreur de typage
IndexError # Index inexistant
KeyError # Clef inexistante .....
````

Python en a beaucoup déjà définies, ce sont les built-in exceptions: https://docs.python.org/3/library/exceptions.html

---

# Les erreurs

## Les types d'erreurs / exceptions (2)


Tout ces types d'erreurs ont un type commun: `Exception`. On dit que ces erreurs héritent de la classe ou du type `Exception`. (cf partie 2).

Il est également possible d'en créer de nouvelles, mais également des dérivés (cf partie 2).

Ainsi les modules et les librairies (modules externes) amènent leurs lots de nouveaux types d'erreurs.

---

# Les erreurs

## Gérer les erreurs

Lorsqu'une erreur est levée, elle met fin à l'éxecution du programme. Il faut les gérer pour garantir la continuité de notre programme.

On utilise alors les déclarations `try` et `except` pour les gérer.

Le `try` entoure du code à risque (susceptible de lever une exception).
Si il y a une erreur (attendue), `except` va éxecuter du code qui lui a été fourni. Le programme continue.

---

# Les erreurs

## Gérer les erreurs (2)

Programme sans try / except:
````python
dict_students = {"John": 18.65, "Jacques": 10.00}
print(dict_students["Martine"])
# KeyError; Le programme s'arrête.
# Le code dessous ne s'exécute pas.
print(dict_students["John"])
````

Programme avec try / except gérant les KeyError:
````python
try:
    dict_students = {"John": 18.65, "Jacques": 10.00}
    print(dict_students["Martine"])
except KeyError:
    # Le programme continue.
    print(dict_students["John"])
````

---

## Gérer les erreurs (3)


On peut chaîner les `except` pour gérer différents types d'erreurs:
````python
students_name = ["John", "Gilles", "Jacques", "Jean Charles"]
students_notes = {"John": 18.65, "Jacques": 10.00, "Gilles": None}
for student in students_name:
    try:
        students_notes[student] += 1.00
    except TypeError:
        print(student, "'s score is wrong!")
        del students_notes[student]
    except KeyError:
        print(student, " doesn't have score!")

print(students_notes)
````

````
Gilles 's note is wrong!
Jean Charles  doesn't have score!
{'John': 19.65, 'Jacques': 11.0}
````

---


## Gérer les erreurs (4)


**\/!\\** Evitez d'utiliser le type Exception:
````python
for student in students_name:
    try:
        students_notes[student] += 1.00
    except Exception: # Chaque erreur est une exception
         print("Il y a eu une erreur !!")
    except TypeError: # On ne passe plus ici
        print(student, "'s score is wrong!")
        del students_notes[student]
    except KeyError:  # On ne passe plus ici
        print(student, " doesn't have score!")

print(students_notes)
````

````
Il y a eu une erreur !!
Il y a eu une erreur !!
{'John': 19.65, 'Jacques': 11.0}
````

---

# Les erreurs

## Lever une erreur

Lorsque l'on écrit un programme, il peut être intéressant de lever des erreurs pour communiquer avec l'utilisateur (développeur ou autres).

On peut utiliser `raise` pour lever une erreur:
````python
if value < 0:
   # on choisit de lever une erreur avec un message personnalisé.
   raise ValueError("The value can't be negative!")
````

---


# Les modules et les namespaces

## Les built-ins

De nombreuses fonctions ou types sont disponibles par défaut dans le namespace global de python, ce sont les **built-in**.

Par exemple, la fonction `print` est une fonction built-in.

La liste non exhaustive des built-ins est disponible ici: https://docs.python.org/3/library/index.html

---

# Les modules et les namespaces

## Les modules

Parfois on veut utiliser du code prêt à l'emploi autre que les built-ins. Ce sont les modules (1 module ~= 1 fichier python).

On peut importer différents modules dans son programme pour ajouter des fonctionnalités.

Certains modules sont préinstallés avec python: https://docs.python.org/3/py-modindex.html

---

# Les modules et les namespaces

## Importer un module

On peut importer un module dans son intégralité:
````python
import math
print(math.pi)
````

Ou importer quelques parties du module:

````python
from math import pi
print(pi)
````

Ou même tout importer d'un module:  **\/!\\**

````python
from math import * # charge tout dans le namespace
print(pi)
````

---

# Les modules et les namespaces

## Importer un module (2)


On peut aussi utiliser le système de modules pour découper son programme en plusieurs fichiers:

````python
from .my_folder.my_file import my_function
# On importe my_function du sous-module my_file
````

On peut alors créer une arborescence de fichier `.py` contenant chacun une petite partie du code, que l'on importera au besoin.

**Pour que python sache reconnaître un fichier comme un module, le dossier doit contenir un fichier `__init__.py` !**


---

## Les modules internes indispensables

- [`datetime`](https://docs.python.org/3/library/datetime.html): gestion des dates (formatage, types, calculs...)
- [`math`](https://docs.python.org/3/library/math.html): fonctions de calculs et constantes
- [`os`](https://docs.python.org/3/library/os.html), [`sys`](https://docs.python.org/3/library/sys.html), [`suprocess`](https://docs.python.org/3/library/subprocess.html), [`shutil`](https://docs.python.org/3/library/shutil.html): dialoguer avec l'os, avoir des infos du système, éxecuter des commandes, gérer les fichiers
- [`random`](https://docs.python.org/3/library/random.html): génération aléatoire (nombres, mélange...)
- [`collection`](https://docs.python.org/3/library/collections.html): structures de données additionnelles
- [`logging`](https://docs.python.org/3/library/logging.html): gestionnaire de log / print
- [`json`](https://docs.python.org/3/library/json.html), [`csv`](https://docs.python.org/3/library/csv.html): lecture, écriture de fichiers (json, csv)


---

## Les modules internes indispensables (2)

- **EXTERNE** [`requests`](http://docs.python-requests.org/en/master/): requêtes HTTP (intéractions avec apis web...)
- [`argparse`](`https://docs.python.org/3/library/argparse.html`): gestionnaire de paramètres de script
- [`threading`](https://docs.python.org/3/library/threading.html), [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html): parallélisation de calculs
- [`itertools`](https://docs.python.org/3/library/itertools.html), [`functools`](https://docs.python.org/3/library/functools.html): programmation fonctionnelle
- [`string`](`https://docs.python.org/3/library/string.html`), [`re`](https://docs.python.org/3/library/re.html): templating, formattage et regexp
- [`operator`](https://docs.python.org/3/library/operator.html): tout les opérateurs en fonctions
- [`configparser`](https://docs.python.org/3/library/configparser.html): gestionnaire de configuration
- [`unittest`](https://docs.python.org/3/library/unittest.html): utilitaires pour tests unitaires
---

---

## Appartée - pip

[`pip`](https://pip.pypa.io/en/stable/) est un gestionnaire de paquets ultra complet pour python. Il permet d'installer et de gérer des modules / librairies externes pour python (dépôt `pypa`). 
Sur votre système vous pouvez par exemple installer le module `requests`:
````
pip3 install requests
pip3 install requests==2.18.4
````

Mais il permet également de gérer les paquets:
````
pip3 install --upgrade requests
pip3 uninstall requests
````

**Il est normalement installé par défaut**. Si ce n'est pas le cas: [installez le !](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip)

---

## Quelques modules / librairies externes

- **INDISPENSABLE** [`requests`](http://docs.python-requests.org/en/master/): requêtes HTTP (intéractions avec apis web...)
- [`sqlalchemy`](http://www.sqlalchemy.org/): ORM pour bases de données sql (et autres)
- [`numpy`](http://www.numpy.org/): structures (Array) et calculs scientifiques
- [`pandas`](https://pandas.pydata.org/): structures (DataFrame) et calculs scientifiques
- [`matplotlib`](http://matplotlib.org/): visualisation de données
- [`scikit-learn`](http://scikit-learn.org/stable/index.html): machine learning pour python
- [`flask`](http://flask.pocoo.org/): création d'api HTTP (rest et autres)
---


# Les modules et les namespaces

## Comprendre les namespaces

Quand une fonction, une variable, ou un module est utilisable dans python, elle est présente dans le *namespace* (ou *scope*) courant.

On a deux types de namespaces:
- global (son contenu est accessible partout)
- local (son contenu est accessible dans une partie du code)

Les built-ins par exemple sont présents par défaut dans le namespace global.

---

# Les modules et les namespaces

## Comprendre les namespaces (2)


Pour visualiser un namespace, on utilise les fonctions `globals` ou `locals` (ou `dir`) qui liste tout ce qui est dans le namespace global et local:

````python
print(globals())
print(locals()) # ou dir()
````

`['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']`

Ainsi on voit que nos built-ins sont en effet présent dans le programme.

On peut même en voir le contenu: `print(dir(__builtins__))`

---

# Les modules et les namespaces

## Comprendre les namespaces (3)

Si on essaye d'atteindre une variable qui n'est pas présent ni dans le namespace local, ni dans le global, on dit qu'elle n'est pas à portée (pas dans le scope):

````python
print(pi)
````

Python nous signal que le nom `pi` n'est pas présent dans le namespace: `NameError: name 'pi' is not defined`.

---

# Les modules et les namespaces

## Comprendre les namespaces (4)

Lorsque l'on importe un module, ou que l'on déclare une variable, python l'ajoute alors au namespace courant (local):

````python
from math import pi
print(pi)
print(locals())
````
Ce qui rend l'accés à une variable ou à une fonction possible:
````
3.141592653589793
[..., 'pi']
````

---

## La portée d'une variable

En raison de l'existende de namespaces locaux ou global, on dit qu'une variable a une portée (scope):
- globale si la variable est atteignable de partout (scope global)
- locale si la variable est atteignable dans une partie du programme uniquement (scope local).

Exemple avec `globals` et `locals`:

````python
a = 1
print(globals(), locals())
````
````
{..., 'a': 1} {..., 'a': 1}
````
On est à ici à la racine du programme, ce qu'on déclare est global.

---

## La portée d'une variable (2)

Une fonction a son propre namespace local. 
Depuis l'intérieur d'une fonction, on peut accéder au namespace global. 
En revanche, une variable déclarée dans la fonction n'est accessible que dans celle ci. 
La variable a une portée locale et n'est présente que dans le namespace local de cette fonction

---

````python
one = 1 # one est global

print(globals(), locals())

def addOne(number): # Fonction closure !
    result = one + number
    print(globals(), locals())
    return result


print(addOne(4))
print(globals(), locals())
````

````
{..., 'one': 1} {..., 'one': 1}
{..., 'one': 1, 'addOne': <function addOne>} 
   {'result': 5, 'number': 4}
5
{..., 'one': 1, 'addOne': <function addOne>} 
   {..., 'one': 1, 'addOne': <function addOne>} 
````

---


Quand on déclare une fonction dans une fonction, on ajoute le contenu du namespace local de la fonction "parente" à celui de la fonction "enfant" (et pas l'inverse):
````python
def addOneToNumbers(*numbers):
    one = 1
    def addOne(number): # Fonction closure !
        return one + number
    results = []
    for number in numbers:
        results.append(addOne(number))
    return results

````

`addOne` a accés aux variables du scope global mais aussi à celles déclarées dans `addOneToNumbers` (qui se retrouvent dans son namespace local).

---



# Les fichiers

## La fonction open

Pour lire ou écrire un fichier, on utilise la fonction open (qui ouvre un flux vers ce fichier).

Un flux s'ouvre et se ferme (quand on a terminé avec lui):
````python
file = open("myfile.txt")
print(file)
print(file.read())
file.close()
print(file.read())
````

````
<_io.TextIOWrapper name='myfile.txt' mode='r'
                   encoding='UTF-8'>
'HELLO WORLD!'
ValueError: I/O operation on closed file.
````

---

## Appartée - La déclaration with

Si on peut automatiser la fermeture d'un fichier (ou de tout flux) on peut utiliser la déclaration `with`:

````python3
with open("myfile.txt") as file:
   print(file.read())
````

Le flux se fermera de lui même une fois le bloc de code terminé.

Il est conseillé d'utiliser cette notation plutôt que la méthode `.close`.

---


# Les fichiers

## Lire un fichier

On peut lire un fichier en précisant un mode d'ouverture read `r` (mode par défaut):

````python
with open("myfile.txt", mode="r") as file:
   print(file.read())
````

Différentes méthodes sont utilisable sur fichier pour le lire: 
````python
file.read() # Lit tout le fichier
file.readline() # Retourne la première ligne du flux
file.readlines() # Retourne une liste avec chaque ligne
````

---

# Les fichiers

## Lire un fichier (2)


On ne peut lire un fichier inexistant:
````python
with open("nanananana.txt", mode="r") as file:
   print(file.read())
````

Python nous l'indique par une erreur:
````
FileNotFoundError: [Errno 2] No such file or directory: 'nanana.txt'

````

---


## Lire un fichier (3)

Un flux se consomme (on ne le lit qu'une fois):

````python3
with open("myotherfile") as file:
   print(file.read())
   print(file.read()) # On a déjà consommé le flux
````

````
"Hello\nMy Name is Guillaume\nNice to meet you"
````


````python3
with open("myotherfile") as file:
   print(file.readline()) # la premère ligne
   print(file.readline()) # la deuxième ligne
   print(file.readlines()) # on consomme le reste
````

````
"Hello\n"
"My Name is Guillaume\n"
["Nice to meet you"]
````

---

# Les fichiers

## Ecrire un fichier

On peut écrire un fichier et écraser son contenu avec le mode overwrite `w`:

````python3
with open("myotherfile", "w") as file:
   file.write("I overwrite ")
   file.write("what I want !!") # Ecrit à la suite
   file.write("\nWhen I want !!") # Ecrit à la suite


with open("myotherfile", "r") as file:
   print(file.readlines())
````

````
['I overwrite what I want !!\n', 'When I want !!']
````

---

# Les fichiers

## Ecrire un fichier (2)

On peut écrire un fichier et compléter son contenu avec le mode append `a`:

````python
with open("myotherfile", "a") as file:
   file.write("I append something")
   file.write("\nWhen I want !!") # Ecrit à la suite


with open("myotherfile", "r") as file:
   print(file.readlines())
````

````
['I overwrite what I want !!\n',
'When I want !!I append something\n',
'When I want !!']
````

---

# Les fichiers

## Les fichiers binaires

On peut lire ou écrire un fichier en binaire en ajoutant le mode binaire `b` au modes existants:
- `rb`
- `wb`
- `ab`
...


---


# Les fichiers

## Ouvrir un csv

On peut utiliser module `csv` et la fonction `open` pour lire ou écrire du csv:

````python
import csv
with open('eggs.csv') as file:
    eggs = list(csv.reader(file, delimiter=','))
        
with open('eggs.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['Spam', 'Baked Beans'])
    spamwriter.writerow(['Spam', 'Wonderful Spam'])
````

---


# Les fichiers

## Ouvrir un json

On peut utiliser module `json` et la fonction `open` pour lire ou écrire du csv:

````python
import json
with open('students.json') as file:
    students = json.load(file)
    
students_scores = {"jean michel": 19.5,
                   "jean gilles": 10.5}
with open('students_scores.json', 'w') as file:
    json.dump(students_scores, file)
````

---

# Structure d'un projet

## Les conditions d'un bon projet

Un projet python (lib ou app) doit avoir:
- Un `README` (**md** or rst) pour expliquer le projet
- Un système de versionnement (**git** ou mercurial ou svn)
- Un `CHANGELOG` (**md** ou rst) pour expliquer les changements
- Un point d'entrée (un fichier .py ou un raccourci système)
- Un code source avec une arborescence clair
- Un fichier contenant les versions des modules externes
- **Idéalement** des tests unitaires
- **Idéalement** une configuration de linter

---

# Structure d'un projet

## Structure basique

Rendez vous sur https://git.io/vbY68 dans `projects/simple-project` pour voir un exemple de projet basique.

`README.md` contient la documentation pour installer et lancer le project.
`CHANGELOG.md` contient les différentes versions et modifications.
`simple_project.py` contient le point d'entrée du projet.
`src` contient le code source utilisé par le point d'entrée. Le fichier `__init__.py` permet à python d'importer le contenu du dossier comme des modules.
`requirements.txt` contient la liste des dépendances externes utilisées (et leurs versions).

---

# Structure d'un projet

## Structure avancée

On peut créer une structure de projet plus élaborée qui permet d'installer son applicatif via `pip` (et le publier sur le dépôt `pypa`) voir d'y ajouter des test unitaires et un linter (via `tox`).

Un bon exemple est le projet fourni par `pypa` et disponible ici: https://github.com/pypa/sampleproject.

Il peut servir de base à tout projet python (application ou librairie).

Il regroupe toutes les bonnes pratiques.
