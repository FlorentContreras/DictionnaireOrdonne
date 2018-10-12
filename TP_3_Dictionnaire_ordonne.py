# Implementation de la classe décrite dans le TP https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/233322-tp-un-dictionnaire-ordonne

class DictionnaireOrdonne: # Définition de la class DictionnaireOrdonnee
    """ class définissant un dictionnaire 
        comprend 2 listes : 
        - _cle
        - _valeur 

    """ 

    def __init__(self, DictionnaireEntrant): # Notre méthode constructeur
        """ Constructeur de notre class qui stocke le DictionnaireEntrant
            Il devra ensuite stocker cela dans 2 listes   """

        # création de listes vides pour accueillir les clés et valeurs du dictionnaire
        self._cle = []
        self._valeur = []

        # Remplissage des listes à partir des données du dictionnaire
        for cle_temp, valeur_temp in DictionnaireEntrant.items(): 
            self._cle.append(cle_temp)
            self._valeur.append(valeur_temp)
            

    def __str__(self):
        """ Cette méthode se charge d'afficher un DictionnairePrint 
        reconstruit à partir des 2 listes"""
      
        DictionnairePrint = dict(zip(self._cle, self._valeur))

        return str(DictionnairePrint)


    def keys(self):
        """ Cette méthode affiche les clés du dictionnaire, 
        soit la liste comportant les clés """

        print(str(self._cle))
        return list(self._cle)


    def values(self):
        """ Cette méthode affiche les valeurs du dictionnaire, 
        soit la liste comportant les valeurs """

        print(str(self._valeur))
        return list(self._valeur)


    def __getitem__(self, cleAAfficher):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        try:
            print(self._valeur[self._cle.index(cleAAfficher)])
        except ValueError: 
            print("Indice {} inconnu du dictionnaire. ".format(cleAAfficher))


    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        
        if index in self._cle:
            print("Mise à jour de l'indice {} avec la valeur {}. ".format(index, valeur))
            self._valeur[self._cle.index(index)] = valeur

        else:
            print("Création de l'indice {} avec la valeur {}. ".format(index, valeur))
            self._cle.append(index)
            self._valeur.append(valeur)


    def __delitem__(self, cleASupprimer):
        """ Cette méthode permet de supprimer un couple clé/valeur 
        à partir de sa clé """

        try: 
            indice = self._cle.index(cleASupprimer)

            del self._valeur[indice]
            del self._cle[indice]

        except ValueError: 
            print("L'indice {} a supprimer n'existe pas. ".format(cleASupprimer))


    def __len__(self):
        """ Cette méthode permet de connaitre la taille de notre dictionnaire """

        print(len(self._cle))
        return 0


    def __contains__(self, cleAChercher):
        """ Cette méthode permet de savoir si une clé se trouve dans le dictionnaire """

        if cleAChercher in self._cle:
            print(True)

        else:
            print(False)


    def sort(self):
        """ Cette méthode va trier le dictionnaire en fonction des clés """
        
        # on cré un dict temporaire pour garder la correspondance clé/valeur
        DictTemp = dict(zip(self._cle, self._valeur)) 

        self._cle.sort()    # tri
        
        listValeurTemp = []

        for cle in self._cle:       # remplissage des valeurs correspondante à la clé
            listValeurTemp.append(DictTemp[cle])

        self._valeur = listValeurTemp
        return 0


    def reverse(self):
        """ Cette méthode va inverser le dictionnaire """
        
        # on cré un dict temporaire pour garder la correspondance clé/valeur
        DictTemp = dict(zip(self._cle, self._valeur))

        self._cle = sorted(self._cle, reverse=True) # tri inverse

        listValeurTemp = []

        for cle in self._cle:       # remplissage des valeurs correspondante à la clé
            listValeurTemp.append(DictTemp[cle])

        self._valeur = listValeurTemp
        return 0


    def __iter__(self):
        """Méthode de parcours de l'objet. On renvoie l'itérateur des clés"""
        return iter(self._cle)


    def items(self):
        """Renvoie un générateur contenant les couples (cle, valeur)"""
        for i, cle in enumerate(self._cle):
            valeur = self._valeur[i]
            yield (cle, valeur)


    def __add__(self, dictAAjouter):
        """ Méthode permettant d'ajouter 2 dictionnaires"""
        
        nouveau = DictionnaireOrdonne({})

        # On commence par copier self dans le dictionnaire
        for cle, valeur in self.items():
            nouveau[cle] = valeur
        
        # On copie ensuite autre_objet
        for cle, valeur in dictAAjouter.items():
            nouveau[cle] = valeur
        
        return nouveau


