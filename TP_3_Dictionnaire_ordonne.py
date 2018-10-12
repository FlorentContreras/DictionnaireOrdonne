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


    def __getitem__(self, cleAAfficher):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""

        print(self._valeur[self._cle.index(cleAAfficher)])


    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        
        if self._cle.count(index) == 0:
            print("Création de l'indice {} avec la valeur {}. ".format(index, valeur))
            self._cle.append(index)
            self._valeur.append(valeur)

        else: 
            print("Mise à jour de l'indice {} avec la valeur {}. ".format(index, valeur))
            self._valeur[self._cle.index(index)] = valeur


    def __delitem__(self, cleASupprimer):
        """ Cette méthode permet de supprimer un couple clé/valeur 
        à partir de sa clé """

        indice = self._cle.index(cleASupprimer)
        #del self._valeur.index(indice)
        #del self._cle.index(indice)


"""
    On doit pouvoir créer le dictionnaire de plusieurs façons :


        Pré-rempli grâce à des clés et valeurs passées en paramètre : 
        comme les dictionnaires usuels, on doit ici avoir la possibilité 
        de pré-remplir notre objet avec des couples clés-valeurs 
        passés en paramètre (constructeur(cle1 = valeur1, cle2 = valeur2, …)).


    Les clés et valeurs doivent être couplées. Autrement dit, 
    si on cherche à supprimer une clé, la valeur correspondante 
    doit également être supprimée. Les clés et valeurs se trouvant 
    dans des listes de même taille, il suffira de prendre l'indice 
    dans une liste pour savoir quel objet lui correspond dans l'autre. 
    Par exemple, la clé d'indice 0 est couplée avec la valeur d'indice 0.


    On doit pouvoir interagir avec notre objet conteneur grâce aux crochets, 
    pour récupérer une valeur (objet[cle]), pour la modifier (objet[cle] = valeur) 
    ou pour la supprimer (del objet[cle]).


    Quand on cherche à modifier une valeur, si la clé existe 
    on écrase l'ancienne valeur, si elle n'existe pas on ajoute le couple clé-valeur 
    à la fin du dictionnaire.


    On doit pouvoir savoir grâce au mot-clé in si une clé se trouve 
    dans notre dictionnaire (cle in dictionnaire).


    On doit pouvoir demander la taille du dictionnaire grâce à la fonction len.


    On doit pouvoir afficher notre dictionnaire directement dans l'interpréteur 
    ou grâce à la fonction print. L'affichage doit être similaire à celui 
    des dictionnaires usuels ({cle1: valeur1, cle2: valeur2, …}).


    L'objet doit définir les méthodes sort pour le trier et reverse pour l'inverser. 
    Le tri de l'objet doit se faire en fonction des clés.


    L'objet doit pouvoir être parcouru. Quand on écrit for cle in dictionnaire, 
    on doit parcourir la liste des clés contenues dans le dictionnaire.


    À l'instar des dictionnaires, trois méthodes keys() 
    (renvoyant la liste des clés), values() (renvoyant la liste des valeurs) 
    et items() (renvoyant les couples (clé, valeur)) doivent être mises en œuvre. 
    Le type de retour de ces méthodes est laissé à votre initiative : 
    il peut s'agir d'itérateurs ou de générateurs (tant qu'on peut les parcourir).


    On doit pouvoir ajouter deux dictionnaires ordonnés (dico1 + dico2) ; 
    les clés et valeurs du second dictionnaire sont ajoutées au premier."""

