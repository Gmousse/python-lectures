#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercices pratiques autour des dictionnaires.

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
python3 dists.py

Le script vous affichera alors si vous avez bon à chaque exercice.

"""
import unittest

raw_students = ["Jean", "Gilles", "Romain", "Arthur", "Sylvie", "Marine", "Simon", "Robert"]
raw_students2 = ["Charles", "Gilles", "Marcel", "Arthur", "Georges", "Marine", "Jacques"]
raw_scores = [12.6, 4.68, 18.6, 10.00, 15.5, 19.6, 9.99, 2.0]
raw_scores2 = [10.6, 4.3, 18.4, 10.00, 15.6, 9.6, 12.10]


class Test_dicts(unittest.TestCase):

    def test_students_notes(self):
        """
        Vous êtes professeur de math.
        Vous souhaitez créer un format de donnée pour facilement consulter ou modifier la moyenne de vos étudiants.
        Vous optez alors pour la création d'un dictionnaire.

        Ce format dois vous permettre de:
            - Compter le nombres d'étudiants.
            - Rechercher la moyenne d'un étudiant par son nom.
            - Modifier la moyenne d'un étudiant.
            - Récupérer la meilleure et la plus mauvaise note.

        Différentes variables seront déjà disponibles:
            - students: Une liste des noms de vos étudiants.
            - scores: Le score de chaque élève (students).
            - student_to_find: Le nom d'un étudiant à chercher dans le dictionnaire.
            - student_new_score: La nouvelle note à donner à l'étudiant (student_to_find).
            Cette valeur est optionnel. Si elle n'est pas renseignée elle est None.
            Si la valeur n'est pas None, la note doit être mise à jour.

        Vous devez donc:
          - Utiliser les 2 listes fournies pour créer un dictionnaire stocké dans une variable students_scores.
          - Récupérer le nombre d'étudiants et l'enregistrer dans students_count.
          - Modifier la note de l'étudiant précisé dans student_to_find par student_new_score si elle est définit.
          - Chercher la note de l'étudiant précisé dans student_to_find et l'enregistrer dans score_to_find.
          - Récupérer la meilleure note et la moins bonne (cet ordre) dans une liste
            et la stocker dans best_worst_scores.

        Différents scénarios vont être testé dans cet exercice !
        Veillez donc à respecter l'indentation.
        """

        def format_students(students, scores, student_to_find, student_new_score=None):

            # CODE HERE

            # STOP HERE

            print(
                "Number of students: ", students_count,
                "{} score: ".format(student_to_find), score_to_find,
                "Students scores: ", students_scores,
                "Best and worst scores: ", best_worst_scores)
            return students_count, score_to_find, best_worst_scores, len(students_scores)

        self.assertEqual(format_students(raw_students, raw_scores, "Simon"), (8, 9.99, [19.6, 2.0], 8))
        self.assertEqual(format_students(raw_students, raw_scores, "Sylvie"), (8, 15.5, [19.6, 2.0], 8))
        self.assertEqual(format_students(raw_students, raw_scores, "Sylvie", 8.80), (8, 8.80, [19.6, 2.0], 8))
        self.assertEqual(format_students(raw_students2, raw_scores2, "Charles"), (7, 10.6, [18.4, 4.3], 7))
        self.assertEqual(format_students(raw_students2, raw_scores2, "Joseph", 20.00), (7, 20.00, [20.00, 4.3], 8))


if __name__ == "__main__":
    unittest.main()
