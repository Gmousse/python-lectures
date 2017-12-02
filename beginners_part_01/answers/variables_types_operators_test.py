#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercices pratiques autour des chapitres variables, types et opérateurs.

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
python3 variable_and_types.py

Le script vous affichera alors si vous avez bon à chaque exercice.

"""
import unittest


class Test_variables_types_operators(unittest.TestCase):

    def test_pi_from_circle(self):
        """
        Vous devez calculer la variable pi à partir de la circonférence et du diamètre d'un cercle.
        Pour rappel pi est égale à la circonférence d'un cercle divisé par son diamètre.

        Vous devez donc:
          - Déclarez une variable circle_diameter contenant le diamètre du cercle
            sachant que le rayon est égal à 13 (cm).
          - Déclarez une variable circle_circumference contenant la circonférence du cercle
            celle ci étant égale à 81.6814 (cm).
          - Calculez pi et enregistrez le résultat dans une variable pi.
          - (OPTIONAL) Essayez de deviner le type de la variable pi. Affichez son type dans la console.
        """
        # CODE HERE
        circle_rayon = 13
        circle_diameter = circle_rayon * 2
        circle_circumference = 81.6814
        pi = circle_circumference / circle_diameter
        print(type(pi))
        # STOP HERE

        print("pi: ", pi)

        self.assertTrue(isinstance(circle_diameter, int))
        self.assertTrue(isinstance(circle_circumference, int))
        self.assertTrue(round(pi, 4) == 3.1415)

    def test_pretty_text(self):
        """
        Un de vos client vous fais parvenir une liste de modification à appliquer au texte d'un email automatique.
        Vous devez donc modifiez le contenu de cet email.
        Vu que vous êtes féneant vous le faites en python.

        Le texte original est stocké dans la variable email_content.

        Voici la liste des modifications demandées:
          - On a oublié la majuscule en début de mail. Ajoutez là.
          - Quelqu'un a mis des émoticones :D partout. Retirez les.
          - Quelqu'un a utilisé le mot "trop super". Remplacez le par "quotidienne".
          - On a oublié la signature du mail. Rajoutez "L'équipe marketing" en fin du mail.

        Vous devez donc:
          - Traitez les demandes du client et enregistrez le nouveau mail dans une variable formated_email_content.
          /!\ Pour la dernière consigne, vous aurez besoin de rajouter un saut de ligne \n devant votre signature.
          - Vérifiez que le nouveau mail ne contienne plus d'émoticones :D. Enregistrez le résultat dans has_emots.
          - (OPTIONAL) Essayez de deviner quel est le type de has_emots. Affichez son type dans la console.
        """
        email_content = """cher client,  :D

merci de vous être inscrit à notre newsletter trop super.

nous vous remercions de votre confiance. :D
        """

        # CODE HERE
        formated_email_content = email_content.replace(":D", "")\
            .replace("trop super", "quotidienne")\
            .capitalize() + "\nL'équipe marketing"
        has_emots = ":D" in formated_email_content
        # STOP HERE

        print("New mail: ", formated_email_content)
        print("New mail has emoticones: ", has_emots)

        self.assertTrue(formated_email_content.startswith("Cher client"))
        self.assertTrue(formated_email_content.endswith("\nL'équipe marketing"))
        self.assertFalse(":D" in formated_email_content)
        self.assertFalse("newsletter trop super." in formated_email_content)
        self.assertTrue("newsletter quotidienne." in formated_email_content)
        self.assertFalse(has_emots)


if __name__ == "__main__":
    unittest.main()
