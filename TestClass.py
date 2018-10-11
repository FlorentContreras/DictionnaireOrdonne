#!/usr/bin/python3.6
# -*-coding:utf-8-*

from TP_3_Dictionnaire_ordonne import *

def testclass():
	""" Fonction permettrant de tester la class DictionnaireOrdonne """

	extdicfruit = {'pomme': 52, 'poire': 34}

	fruit = DictionnaireOrdonne(extdicfruit)
	print(fruit)

testclass()
