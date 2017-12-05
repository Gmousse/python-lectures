#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from random import random


def main(manches):
    manches_jouees = 0
    score = 0
    historique = []

    while manches_jouees < manches:
        # CODE HERE

        # STOP HERE
        manches_jouees += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Jeu de pierre papier ciseaux.')
    parser.add_argument('--manches', type=int, default=15,
                        help='Nombre de manches. 15 par défaut.')
    args = parser.parse_args()
    main(args.manches)
