# Implementation de la classe décrite dans le TP https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/233322-tp-un-dictionnaire-ordonne

class DictionnaireOrdonne: # Définition de la class DictionnaireOrdonnee
    """ class définissant un dictionnaire 
        comprend 2 listes : 
        - cle
        - valeur 

    """ 

    def __init__(self, DictionnaireEntrant): # Notre méthode constructeur
        """ Constructeur de notre class qui stocke le DictionnaireEntrant
            Il devra ensuite stocker cela dans 2 listes   """

        # création de listes vides pour accueillir les clés et valeurs du dictionnaire
        self.cle = []
        self.valeur = []

        # Remplissage des listes à partir des données du dictionnaire
        for cle_temp, valeur_temp in DictionnaireEntrant.items(): 
            self.cle.append(cle_temp)
            self.valeur.append(valeur_temp)
            

    def __str__(self):
        """ Cette méthode se charge d'afficher un DictionnairePrint 
        reconstruit à partir des 2 listes"""
      
        DictionnairePrint = dict(zip(self.cle, self.valeur))

        return str(DictionnairePrint)



"""
On doit pouvoir créer le dictionnaire de plusieurs façons :

    Vide : on appelle le constructeur sans lui passer aucun paramètre et 
    le dictionnaire créé est donc vide.

    Copié depuis un dictionnaire : on passe en paramètre du constructeur 
    un dictionnaire que l'on copie par la suite dans notre objet. 
    On peut ainsi écrire constructeur(dictionnaire) et les clés et 
    valeurs contenues dans le dictionnaire sont copiées dans l'objet construit.

    Pré-rempli grâce à des clés et valeurs passées en paramètre : 
    comme les dictionnaires usuels, on doit ici avoir la possibilité de pré-remplir 
    notre objet avec des couples clés-valeurs passés en paramètre 
    (constructeur(cle1 = valeur1, cle2 = valeur2, …)).
    """