#! /usr/bin/env python3
# -*- coding: utf-8 -*-
cars_stock = ['c4', 'c4', 'yaris', 'c4', 'c4', 'laguna', 'yaris', 'laguna', 'c4', 'c4', 'c4', 'laguna', 'c4', 'c4', 'yaris', 'laguna', 'c4', 'laguna', 'laguna', 'yaris', 'yaris', 'yaris', 'laguna', 'laguna', 'c4', 'laguna', 'c4', 'yaris', 'c4', 'laguna', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'yaris', 'yaris', 'crz', 'crz', 'c4', 'laguna', 'c4', 'c4', 'c4', 'crz', '500', 'c4', 'yaris', 'crz', 'crz', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'crz', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'laguna', 'yaris', 'c4', 'laguna', '500', 'c4', 'c4', 'c4', 'yaris', '500', 'c4', 'crz', 'crz', 'yaris', 'c4', 'c4', 'c4', 'laguna', 'yaris', 'c4', 'laguna', 'c4', 'laguna', 'laguna', 'laguna', 'crz', 'c4', 'yaris', '500', 'yaris', 'yaris', 'c4', 'c4', 'crz', 'c4', 'yaris', '500', 'c4', 'yaris', 'laguna', 'laguna', 'yaris', 'yaris', 'c4', 'crz', 'yaris', '500', 'c4', 'c4', 'laguna', 'crz', 'c4', 'yaris', 'c4', 'laguna', 'laguna', 'laguna', 'c4', 'c4', 'yaris', 'yaris', 'crz', 'c4', 'c4', 'c4', 'c4', 'yaris', 'c4', 'c4', 'c4', 'laguna', 'yaris', 'yaris', 'yaris', 'yaris', 'yaris', 'laguna', 'yaris', 'laguna', '500', 'crz', 'c4', 'laguna', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'c4', 'c4', 'c4', 'laguna', 'yaris', 'c4', '500', 'yaris', 'crz', 'yaris', 'laguna', 'laguna', 'yaris', 'c4', 'c4', 'laguna', 'yaris', 'laguna', 'yaris', 'yaris', 'yaris', 'c4', 'laguna', 'c4', 'c4', 'c4', 'c4', 'yaris', 'laguna', 'crz', 'c4', 'crz', 'yaris', '500', 'crz', 'yaris', 'yaris', 'laguna', 'yaris', 'yaris', 'yaris', 'yaris', 'crz', 'yaris', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'laguna', 'yaris', 'yaris', 'yaris', 'laguna', 'yaris', 'c4', 'yaris', 'laguna', 'yaris', 'c4', '500', 'yaris', 'yaris', 'c4', 'yaris', 'yaris', 'laguna', 'yaris', 'laguna', '500', 'c4', 'yaris', 'c4', 'yaris', 'crz', 'c4', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'laguna', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'c4', '500', 'crz', 'c4', 'laguna', 'c4', 'c4', 'yaris', 'laguna', 'laguna', 'yaris', 'yaris', 'yaris', 'c4', 'c4', '500', 'c4', '500', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'crz', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'c4', 'laguna', 'laguna', 'laguna', 'yaris', 'crz', 'c4', 'laguna', 'c4', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'c4', 'laguna', 'yaris', 'laguna', 'c4', 'laguna', 'yaris', 'yaris', 'laguna', 'yaris', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'yaris', '500', 'yaris', 'c4', 'c4', 'crz', 'c4', 'yaris', 'c4', 'c4', 'c4', 'c4', 'c4', 'yaris', 'crz', 'yaris', 'yaris', 'crz', 'laguna', 'c4', 'yaris', 'laguna', 'yaris', 'yaris', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'c4', 'yaris', 'laguna', 'yaris', 'yaris', 'laguna', 'yaris', 'yaris', 'yaris', 'laguna', 'c4', 'laguna', 'c4', 'crz', 'c4', 'yaris', 'c4', 'laguna', 'yaris', 'laguna', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'laguna', 'c4', 'c4', 'yaris', 'laguna', '500', 'c4', 'c4', 'yaris', '500', 'crz', 'c4', 'yaris', 'laguna', 'yaris', 'laguna', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'yaris', 'c4', 'c4', 'laguna', 'yaris', 'crz', 'crz', 'yaris', 'c4', 'c4', 'yaris', '500', 'laguna', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'laguna', 'c4', 'yaris', 'crz', 'yaris', 'laguna', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'laguna', 'yaris', 'c4', 'crz', 'c4', 'laguna', 'c4', 'c4', 'c4', 'c4', 'laguna', 'yaris', 'yaris', 'laguna', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'laguna', 'c4', 'laguna', 'laguna', 'laguna', 'c4', 'yaris', 'c4', '500', 'yaris', 'crz', 'crz', 'laguna', 'laguna', 'c4', 'c4', 'yaris', 'laguna', '500', 'yaris', 'yaris', 'laguna', 'yaris', 'yaris', 'laguna', 'c4', 'c4', 'laguna', 'c4', 'crz', 'c4', 'yaris', 'c4', 'laguna', 'crz', 'c4', 'crz', 'yaris', 'laguna', 'yaris', '500', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'crz', 'yaris', 'yaris', 'yaris', 'c4', 'yaris', '500', 'c4', 'yaris', 'c4', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'laguna', 'yaris', 'crz', 'laguna', 'c4', 'yaris', 'c4', '500', 'c4', 'yaris', 'yaris', 'laguna', 'yaris', 'c4', 'c4', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'crz', 'yaris', 'yaris', 'laguna', 'crz', 'yaris', 'c4', 'c4', 'laguna', 'yaris', 'laguna', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'laguna', 'yaris', 'crz', 'yaris', 'laguna', 'c4', 'c4', 'yaris', 'yaris', 'laguna', 'laguna', 'yaris', 'laguna', 'yaris', 'c4', 'c4', 'crz', 'laguna', 'yaris', 'laguna', 'c4', 'c4', 'c4', 'crz', 'yaris', 'yaris', 'c4', 'yaris', 'c4', 'c4', '500', 'c4', 'laguna', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'c4', '500', 'crz', 'crz', 'c4', 'yaris', '500', 'yaris', 'c4', 'c4', 'c4', 'c4', 'c4', '500', 'yaris', 'c4', 'laguna', 'crz', 'yaris', 'laguna', 'c4', 'yaris', 'c4', 'laguna', 'laguna', 'c4', 'yaris', 'crz', 'yaris', 'c4', 'c4', 'c4', 'laguna', 'c4', 'c4', 'c4', 'c4', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'yaris', 'laguna', 'yaris', 'c4', 'c4', 'c4', 'c4', '500', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'laguna', 'c4', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'laguna', 'crz', 'yaris', 'laguna', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'c4', 'c4', 'yaris', 'c4', 'laguna', 'c4', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'crz', 'yaris', 'c4', 'c4', '500', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'crz', 'yaris', 'c4', 'crz', 'yaris', 'c4', 'yaris', 'yaris', 'c4', 'yaris', 'c4', 'yaris', 'laguna', 'c4', '500', 'yaris', 'crz', 'yaris', 'c4', 'c4', 'c4', 'c4', 'c4', 'crz', '500', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'laguna', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'crz', 'crz', 'laguna', 'laguna', 'laguna', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'laguna', '500', 'c4', '500', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'c4', 'laguna', 'crz', 'c4', '500', 'crz', 'c4', 'laguna', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'c4', '500', 'laguna', 'c4', '500', '500', 'yaris', 'c4', 'c4', 'yaris', '500', 'yaris', 'yaris', 'yaris', 'laguna', 'c4', 'yaris', 'laguna', 'yaris', 'laguna', 'laguna', 'yaris', 'c4', 'c4', 'crz', 'c4', 'c4', 'c4', 'crz', 'laguna', 'c4', 'yaris', 'c4', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'laguna', 'laguna', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'crz', 'crz', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'crz', 'laguna', 'c4', 'c4', 'c4', '500', '500', 'laguna', 'yaris', 'c4', 'c4', 'yaris', 'crz', 'yaris', 'laguna', '500', 'c4', 'yaris', 'crz', 'yaris', 'crz', 'crz', 'laguna', 'laguna', 'crz', 'c4', 'c4', '500', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'c4', 'c4', 'yaris', 'laguna', 'c4', 'crz', 'yaris', 'yaris', 'c4', 'laguna', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'c4', 'c4', 'yaris', 'c4', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'yaris', 'crz', 'c4', 'c4', 'yaris', 'yaris', 'laguna', 'laguna', 'c4', 'laguna', 'c4', 'laguna', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'crz', 'yaris', 'laguna', 'laguna', 'crz', 'laguna', 'laguna', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'yaris', 'c4', 'c4', 'c4', 'laguna', 'yaris', 'c4', 'c4', 'c4', 'yaris', 'laguna', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'laguna', 'c4', 'laguna', 'yaris', 'laguna', 'yaris', 'yaris', 'c4', '500', 'laguna', '500', 'laguna', 'c4', 'laguna', 'c4', 'yaris', 'laguna', 'c4', 'c4', 'crz', 'c4', 'laguna', 'yaris', 'c4', 'c4', 'c4', 'laguna', 'c4', 'c4', 'c4', 'laguna', 'c4', 'laguna', 'laguna', 'crz', 'laguna', 'c4', 'yaris', 'laguna', 'laguna', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'yaris', 'yaris', 'c4', 'yaris', 'c4', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'laguna', 'c4', 'c4', 'c4', 'c4', 'laguna', 'yaris', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'laguna', 'c4', 'yaris', 'c4', 'c4', 'c4', 'c4', 'yaris', 'laguna', 'c4', 'yaris', 'crz', 'c4', 'laguna', 'yaris', 'c4', 'c4', 'crz', 'crz', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'crz', '500', 'laguna', 'c4', 'laguna', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'laguna', 'laguna', 'crz', 'c4', 'yaris', 'yaris', 'yaris', 'crz', 'c4', '500', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'laguna', 'yaris', 'yaris', 'c4', 'laguna', 'c4', 'c4', 'crz', 'yaris', 'yaris', 'c4', 'laguna', 'c4', 'laguna', 'laguna', 'laguna', 'yaris', 'yaris', 'crz', 'yaris', '500', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'c4', 'laguna', '500', 'c4', 'c4', 'yaris', 'crz', 'laguna', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'crz', 'c4', 'crz', 'laguna', '500', 'laguna', 'yaris', 'yaris', 'yaris', 'laguna', 'yaris', 'laguna', 'yaris', 'c4', 'yaris', 'crz', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'crz', 'laguna', 'c4', 'crz', 'yaris', 'c4', 'c4', 'yaris', 'crz', 'yaris', 'yaris', 'yaris', 'c4', 'yaris', 'laguna', 'c4', 'laguna', 'c4', 'yaris', '500', 'c4', '500', 'crz', '500', 'yaris', 'laguna', 'c4', 'laguna', 'yaris', 'c4', 'laguna', 'crz', 'c4', 'yaris', 'c4', 'c4', 'c4', 'c4', 'yaris', 'yaris', 'laguna', 'crz', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'laguna', 'c4', 'yaris', 'c4', '500', 'c4', 'crz', 'yaris', 'laguna', 'c4', 'laguna', 'laguna', 'c4', 'yaris', 'laguna', 'crz', 'yaris', 'c4', 'yaris', 'yaris', 'laguna', 'c4', 'c4', 'laguna', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'laguna', '500', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'yaris', 'c4', 'c4', 'c4', 'yaris', 'crz', 'c4', 'laguna', 'yaris', '500', 'c4', 'c4', 'yaris', 'laguna', 'laguna', 'laguna', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'laguna', 'yaris', '500', 'laguna', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'crz', 'c4', 'laguna', 'c4', 'yaris', 'c4', 'c4', 'c4', 'crz', 'c4', 'laguna', 'c4', 'crz', 'c4', 'yaris', 'crz', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'laguna', '500', 'crz', '500', 'c4', 'yaris', 'c4', 'laguna', 'yaris', 'yaris', 'crz', 'yaris', 'c4', 'laguna', 'laguna', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'crz', 'laguna', 'crz', 'c4', 'laguna', 'crz', 'laguna', 'c4', 'c4', 'c4', 'yaris', 'c4', 'c4', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'crz', 'yaris', 'c4', 'yaris', 'laguna', 'laguna', 'c4', 'yaris', 'yaris', 'c4', 'c4', '500', 'yaris', 'laguna', 'yaris', 'yaris', 'yaris', 'c4', '500', 'c4', 'c4', 'laguna', 'yaris', 'c4', '500', 'yaris', 'c4', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'c4', 'crz', 'laguna', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'yaris', 'crz', 'yaris', '500', '500', 'c4', 'yaris', 'yaris', 'laguna', 'laguna', 'yaris', 'crz', 'yaris', 'laguna', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'yaris', 'yaris', 'crz', 'c4', 'yaris', 'yaris', 'laguna', 'yaris', 'c4', 'yaris', 'yaris', 'laguna', 'yaris', 'yaris', 'c4', 'c4', 'c4', 'crz', 'laguna', 'laguna', 'laguna', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'c4', '500', 'c4', 'crz', 'c4', 'yaris', 'crz', 'yaris', 'c4', 'laguna', 'crz', 'crz', 'c4', 'c4', 'crz', 'yaris', 'yaris', 'c4', 'yaris', '500', '500', 'c4', 'yaris', 'crz', 'c4', 'laguna', 'yaris', 'yaris', 'laguna', 'yaris', 'yaris', 'laguna', 'yaris', 'crz', 'laguna', 'c4', 'crz', 'yaris', 'crz', '500', 'laguna', 'c4', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'crz', 'c4', 'c4', 'c4', 'c4', 'yaris', 'laguna', 'c4', 'yaris', 'c4', 'yaris', 'c4', 'yaris', 'laguna', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'c4', 'yaris', 'yaris', 'yaris', 'laguna', '500', 'yaris', 'c4', 'yaris', 'laguna', 'c4', 'laguna', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'laguna', 'laguna', 'yaris', 'c4', 'c4', 'laguna', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'c4', 'yaris', 'c4', 'laguna', 'yaris', 'c4', 'c4', 'laguna', 'laguna', 'laguna', 'crz', 'yaris', 'yaris', 'c4', 'c4', 'laguna', 'c4', 'laguna', 'crz', 'c4', 'crz', 'c4', 'yaris', '500', 'yaris', 'c4', 'c4', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'crz', 'laguna', 'yaris', 'laguna', 'laguna', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'laguna', '500', 'yaris', 'yaris', 'c4', 'yaris', 'yaris', 'laguna', 'yaris', 'yaris', 'c4', 'c4', '500', 'c4', '500', 'laguna', 'laguna', 'c4', 'laguna', 'c4', 'yaris', 'laguna', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'crz', 'yaris', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'laguna', 'c4', 'c4', 'yaris', 'c4', 'yaris', 'yaris', 'laguna', 'yaris', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'yaris', 'c4', 'c4', 'yaris', 'c4', 'laguna', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'yaris', 'yaris', 'laguna', 'crz', 'c4', 'laguna', 'c4', 'yaris', 'laguna', 'laguna', 'laguna', 'crz', 'c4', 'c4', 'laguna', 'c4', 'c4', 'laguna', 'crz', 'yaris', 'c4', 'c4', '500', 'c4', 'yaris', 'laguna', 'yaris', 'yaris', 'laguna', 'laguna', 'yaris', '500', 'c4', 'laguna', 'yaris', 'yaris', 'laguna', 'yaris', 'yaris', 'yaris', 'yaris', 'c4', 'c4', 'yaris', 'yaris', 'crz', 'yaris', '500', 'laguna', 'yaris', 'yaris', 'c4', 'laguna', 'laguna', 'laguna']

raw_students = ["Jean", "Gilles", "Romain", "Arthur", "Sylvie", "Marine", "Simon", "Robert"]
raw_scores = [12.6, 4.68, 18.6, 10.00, 15.5, 19.6, 9.99, 2.0]


"""
Exercices pratiques autour des listes.

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
python3 lists.py

Le script vous affichera alors si vous avez bon à chaque exercice.

"""
import unittest
from dat import cars_stock, students as raw_students, scores as raw_scores


class Test_lists(unittest.TestCase):

    def test_cars_lists(self):
        """
        Votre client est concessionnaire automobile. Il souhaiterait un petit programme comptant le nombre d'exemplaires
        d'un modèle de voiture parmis tout son stock.

        Il vous fournit:
            - Une liste contenant des noms de voitures.
            - La voiture à rechercher.

        Différentes variables seront déjà disponibles:
            - cars: Liste de voitures. Exemple: ["c4", "mini cooper"...]
            - car_to_count: Le nom de la voiture à rechercher dans son stock (str).

        Vous devez donc:
          - Vérifier que la voiture est en stock et enregistrer le résultat (TIPS: le booléen) dans la variable in_stock.
          - Compter le nombre de voitures dans la liste et l'enregistrer dans la variable count.

        Différents scénarios vont être testé dans cet exercice !
        Veillez donc à respecter l'indentation.
        """

        def count_cars(cars, car_to_count):

            # CODE HERE

            # STOP HERE

            print(
                "Number of cars in stock: ", len(cars),
                "{} is in stock: ".format(car_to_count), in_stock,
                "Number of {} in stock: ".format(car_to_count), count)
            return in_stock, count

        self.assertEqual(count_cars(cars_stock, "yaris"), (True, 579))
        self.assertEqual(count_cars(cars_stock, "c4"), (True, 602))
        self.assertEqual(count_cars(cars_stock, "laguna"), (True, 269))

    def test_students_notes(self):
        """
        Vous êtes professeur d'anglais. Vous souhaitez automatiser la préparation des conseils de classe.
        Ainsi vous voules:
            - Compter le nombres d'étudiants
            - Rechercher la note d'un élève en fonction de son nom.
            - Sortir leurs notes par ordre décroissant.
            - Récupérer la meilleur et la moins bonne note.

        Différentes variables seront déjà disponibles:
            - students: Une liste des noms de vos étudiants.
            - scores: Le score de chaque élève.
            - student_to_find: Le nom de l'étudiant à rechercher.

        !!!! Une note à un index dans scores correspond au nom ayant le même index dans students !!!!
        Exemple:
        students = ["jean charles", "jean simon"]
        scores = [12.68, 4.32]
        Jean Charles a 12.68, Jean Simon a 4.32.

        Vous devez donc:
          - Compter les étudiants et stocker le résultat dans students_count.
          - Chercher la note de l'étudiant précisé dans student_to_find et l'enregistrer dans score_to_find.
          - Trier les étudiants par ordre décroissant et stocker le résultat dans students_scores.
          - Récupérer la meilleure note et la moins bonne (cet ordre) dans une liste
            et la stocker dans best_worst_scores.

        Différents scénarios vont être testé dans cet exercice !
        Veillez donc à respecter l'indentation.
        """

        def organize_students(student_to_find):
            students = list(raw_students)
            scores = list(raw_scores)

            # CODE HERE

            # STOP HERE

            print(
                "Number of students: ", students_count,
                "{} score: ".format(student_to_find), score_to_find,
                "Students scores: ", students_scores,
                "Best and worst scores: ", best_worst_scores)
            return students_count, score_to_find, best_worst_scores, len(students_scores)

        self.assertEqual(organize_students("Simon"), (8, 9.99, [19.6, 2.0], 8))
        self.assertEqual(organize_students("Romain"), (8, 18.6, [19.6, 2.0], 8))
        self.assertEqual(organize_students("Robert"), (8, 2.0, [19.6, 2.0], 8))


if __name__ == "__main__":
    unittest.main()
