#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercices pratiques autour des chapitres variables, types, opérateurs et conditions.

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
python3 comparisons_conditions_test.py

Le script vous affichera alors si vous avez bon à chaque exercice.

"""
import unittest


class Test_comparisons_conditions(unittest.TestCase):

    def test_cars_prices(self):
        """
        Votre client est concessionnaire automobile. Il souhaiterait un petit programme pour générer les prix des
        modèles suivant les différentes options. En effet, sa grille de prix est un peu farfelue.

        Il vous fournit une grille expliquant l'impact des options sur le prix:
            - Si la couleur est jaune ou verte, le prix diminue de 2 % du prix de base.
            - Si la voiture est tout équipée (gps, clim, ...), le prix augmente de 2000 euros.
              Sauf si elle est jaune ou verte, dans ce cas le prix augmente uniquement de 1000 euros.
            - Si le client demande de teinter les vitres, le prix augmente de 600 euros.
            - Si la voiture est une essence, le prix diminue de 3% du prix de base.
            - Si c'est une électrique, le prix augmente de 2000 euros.
            - Si la voiture n'est ni une essence ni une électrique (e.g. gazoil), le prix diminue de 150 euros.
            - Si le client est membre du club de la marque, le prix TOTAL diminue de 5%.

        Différentes variables seront déjà disponibles:
            - car_base_price: Prix de base de la voiture (float). Exemple: 8054.99
            - car_color: Couleur du modèle choisi par le client (str). Exemple: "yellow", "green", "red"...
            - car_type: Type de moteur (str). "gazoil" ou "essence" ou "electric"
            - car_is_fully_equiped: La voiture est toute équipée (bool).
            - car_is_tinted: La voiture est tintée (bool).
            - client_is_club_member: Le client est membre du club (bool).

        Vous devez donc:
          - Prendre en compte les différentes variables qui vous sont passées.
          - Prendre en compte les différents scénarios.
          - Utiliser les conditions pour calculer le prix final et l'attribué dans une variable car_sell_price.

        Le code généré sera moche.
        Ne vous inquiétez pas, avec la suite du cours et notamment les types de données complexes et les fonctions
        on verra comment refaire ce code proprement.

        Différents scénarios vont être testé dans cet exercice !
        Votre code est englobé dans une fonction (2 chapitres plus tard).
        Veillez donc à respecter l'indentation.
        """

        def compute_car_sell_price(car_base_price, car_color, car_type, car_is_fully_equiped,
                                   car_is_tinted, client_is_club_member):

            # CODE HERE

            # STOP HERE
            print("Car options: ",
                  "Price:", car_base_price,
                  "Color:", car_color,
                  "Carburant:", car_type,
                  "Fully equiped:", car_is_fully_equiped,
                  "Tinted:", car_is_tinted,
                  "Club member:", client_is_club_member)
            print("Car sell price: ", car_sell_price)
            return car_sell_price

        self.assertEqual(compute_car_sell_price(8050, "red", "gazoil", False, False, True), 7505)
        self.assertEqual(compute_car_sell_price(18000, "yellow", "electric", True, True, True), 20278)
        self.assertEqual(compute_car_sell_price(18000, "red", "gazoil", False, False, False), 17850)
        self.assertEqual(compute_car_sell_price(17000, "red", "essence", True, True, False), 19090)
        self.assertEqual(compute_car_sell_price(8050, "green", "essence", False, False, True), 7265.125)
        self.assertEqual(compute_car_sell_price(8050, "black", "gazoil", False, False, False), 7900)


if __name__ == "__main__":
    unittest.main()
