#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercices pratiques autour des itérations.

Chaque exercice suivra les concepts du tdd (test driven development).
Dans chaque éxercices vous aurez accés aux réponses (résultats attendus).
Reste à coder et vérifier si les résultats réels suivent les résultats attendus.

Pour faire cet exercice, copiez ce fichier sur votre ordinateur.
Rendez vous dans chaque fonction commençant par test_.
A l'intérieur vous y trouverez un énoncé, une partie pour coder, et les réponses

Vous y trouverez 2 indicateurs:
# CODE HERE

# STOP HERE

Vous pourrez résoudre chaque exercice entre ces balises.
Ne touchez à rien d'autre que le code entre ces deux balises (ou alors vous trichez :D).

A chaque exercice vous pouvez éxecuter ce fichier comme ceci:
python3 iterations_test.py

Le script vous affichera alors si vous avez bon à chaque exercice.

"""
import unittest


class Test_iterations(unittest.TestCase):

    def test_treat_records(self):
        """
        Vous êtes scientifique et vous devez traiter des données pour les interpréter.

        Différentes variables seront déjà disponibles:
            - daily_records: une liste de dictionnaires contenant les résultats d'analyses journalières.
            Pour chaque analyse, la date est précisée ainsi
            que les résultats d'une analyse répétée 4 fois (pour plus de précision).
            Les résultats
            Exemple: [{"day": "2017-10-19", "result": (0, 0.2, 0.4, 0)}]

        Vous devez donc:
          - Filtrer les analyses si aucun résultat n'est enregistré (None) ou
            si le nombre de répétitions n'est pas 4.
          - Pour chaque analyse filtrée (chaque jour), calculer la moyenne des 4 résultats.
          Arrondissez les résultats à 2 chiffres après la virgule.
          Enregistrer les résultats (gardez le même format!!!) dans une variable daily_results.
          - Calculer la moyenne des résultats moyens journaliers (daily_results)
          et stocker le résultat dans une variable mean_result.

        Différents scénarios vont être testé dans cet exercice !
        Veiller donc à respecter l'indentation.
        """

        def analyze(daily_records):

            # CODE HERE

            # STOP HERE

            print("Mean result: ", mean_result)
            return daily_results, mean_result

        self.assertEqual(
            analyze([
                {"day": "2017-10-19", "result": (0, 0.2, 0.4, 0)},
                {"day": "2017-10-18", "result": (0.8, 0.2, 0.4, 0.4)},
                {"day": "2017-10-22", "result": None},
                {"day": "2017-10-17", "result": (0, 0.2, 0.2, 0.1)},
                {"day": "2017-10-20", "result": (0, 0.4, 0.4, 0.4)},
                {"day": "2017-10-21", "result": (0, 0.1, 0.4, 0.2)}
            ]),
            ([
             {"day": "2017-10-19", "result": 0.15},
             {"day": "2017-10-18", "result": 0.45},
             {"day": "2017-10-17", "result": 0.125},
             {"day": "2017-10-20", "result": 0.3},
             {"day": "2017-10-21", "result": 0.175}],
             0.24)
        )
        self.assertEqual(
            analyze([
                {"day": "2017-11-19", "result": (0, 0.2, 0.4, 0)},
                {"day": "2017-11-18", "result": (0.8, 0.2, 0.4, 0.4)},
                {"day": "2017-11-17", "result": (0.8, 0.2, 0.4, 0.4, 1.8)},
                {"day": "2017-11-16", "result": (0.8, 0.2)},
                {"day": "2017-11-15", "result": None},
            ]),
            ([
             {"day": "2017-11-19", "result": 0.15},
             {"day": "2017-11-18", "result": 0.45}],
             0.3)
        )


if __name__ == "__main__":
    unittest.main()
