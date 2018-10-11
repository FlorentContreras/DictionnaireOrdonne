# Implementation de la classe décrite dans le TP https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/233322-tp-un-dictionnaire-ordonne

class DictionnaireOrdonne: # Définition de la class DictionnaireOrdonnee
    """ class définissant un dictionnaire 

    """ 

    def __init__(self, dictionnaire): # Notre méthode constructeur

        """ Constructeur de notre class qui stocke le dictionnaire
            Il devra ensuite stocker cela dans 2 listes   """

        self.dictionnaire = dictionnaire

        """for 
        self.cle
        self.valeur """


    def __str__(self):

        """ Cette méthode se charge d'afficher le dictionnaire """
      
        return str(self.dictionnaire)


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