#!/usr/bin/python3.6
# -*-coding:utf-8-*

from TP_3_Dictionnaire_ordonne import *


""" Fonction permettrant de tester la class DictionnaireOrdonne """

print("""
Cas 1, dictionnaire vide : """)
dicvide = DictionnaireOrdonne({})
print(dicvide)


print("""
Cas 2, dictionnaire comportant 2 fruitss""")

extdicfruits = {'pomme': 52, 'poire': 34}
fruits = DictionnaireOrdonne(extdicfruits)
print(fruits)


print("""
Affichage les clés d'un dictionnaire""")

fruits.keys()


print("""
Affichage les valeurs d'un dictionnaire""")

fruits.values()


print("""
On va afficher la valeur liée à une clé (ici pomme)""")

fruits["pomme"]


print("""
On va tenter d'afficher la valeur liée à une clé inconnue (ici bière)""")
fruits["biere"]


print("""
On va ajouter une valeur liée à une nouvelle clé (ici banane)""")

fruits["banane"] = 25
print(fruits)


print("""
On va modifier la valeur liée à une clé existante (ici pomme)""")

fruits["pomme"] = 13
print(fruits)


print("""
On va supprimer la clé pomme""")

del fruits["pomme"]
print(fruits)


print("""
On va demander la taille du dictionnaire""")

len(fruits)


print("""
On va demander si 'haricot' est dans le dictionnaire fruits""")

'haricot' in fruits


print("""
On va demander si 'poire' est dans le dictionnaire fruits""")

'poire' in fruits


print("""
On va trier le dictionnaire fruits""")

fruits["prune"] = 128
fruits["melon"] = 15

fruits.sort()
print(fruits)


print("""
On va inverser le dictionnaire fruits""")

fruits["raisin"] = 1256

fruits.reverse()
print(fruits)


print("""
On va parcourir les clés du dictionnaire fruits""")

for cle in fruits:
	print(cle)



print("""
On va ajouter deux dictionnaires""")

legumes = DictionnaireOrdonne({"carotte": 26, "haricot": 48})
print("On va ajouter à fruit le dictionnaire legumes : " + str(legumes))

fruits = fruits + legumes

print(fruits)
