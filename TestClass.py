#!/usr/bin/python3.6
# -*-coding:utf-8-*

from TP_3_Dictionnaire_ordonne import *


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
Affichage les clés d'un dictionnaire""")

fruit.keys()


print("""
Affichage les valeurs d'un dictionnaire""")

fruit.values()


print("""
On va afficher la valeur liée à une clé (ici pomme)""")

fruit["pomme"]


print("""
On va tenter d'afficher la valeur liée à une clé inconnue (ici bière)""")
fruit["biere"]


print("""
On va ajouter une valeur liée à une nouvelle clé (ici banane)""")

fruit["banane"] = 25
print(fruit)


print("""
On va modifier la valeur liée à une clé existante (ici pomme)""")

fruit["pomme"] = 13
print(fruit)


print("""
On va supprimer la clé pomme""")

del fruit["pomme"]
print(fruit)


print("""
On va demander la taille du dictionnaire""")

len(fruit)


print("""
On va demander si 'haricot' est dans le dictionnaire fruit""")

'haricot' in fruit


print("""
On va demander si 'poire' est dans le dictionnaire fruit""")

'poire' in fruit


print("""
On va trier le dictionnaire fruit""")

fruit["prune"] = 128
fruit["melon"] = 15

fruit.sort()
print(fruit)


print("""
On va inverser le dictionnaire fruit""")

fruit["raisin"] = 1256

fruit.reverse()
print(fruit)


print("""
On va parcourir les clés du dictionnaire fruit""")

for cle in fruit:
	print(cle)
