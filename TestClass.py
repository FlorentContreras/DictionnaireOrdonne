#!/usr/bin/python3.6
# -*-coding:utf-8-*

from TP_3_Dictionnaire_ordonne import *

def testclass():
	""" Fonction permettrant de tester la class DictionnaireOrdonne """

	print("""
Cas 1, dictionnaire vide : """)
	dicvide = DictionnaireOrdonne({})
	print(dicvide)


	print("""
Cas 2, dictionnaire comportant 2 fruits""")

	extdicfruit = {'pomme': 52, 'poire': 34}
	fruit = DictionnaireOrdonne(extdicfruit)
	print(fruit)


	print("""
Affichage des clés d'un dictionnaire""")

	fruit.keys()


	print("""
On va afficher la valeur liée à une clé""")

	fruit["pomme"]


	print("""
On va supprimer une clé""")

	del fruit["pomme"]
	fruit.keys()


	#fruit['banane'] = 25
	#print(fruit)

testclass()
