import time
from fonctions import verification,voisins

class Jeu:
    
    def __init__(self,tableau):
        """
        Affecte un tableau à deux dimensions à l'attribut tableau.
        
        :param tableau: tableau à deux dimensions
        """
        self._tableau=tableau
        
    def affichage(self):
        """
        Affiche un tableau à deux dimensions.
        
        :param tableau: tableau à dimensions.
        """
        
        for x in range(len(self._tableau)):
            print (self._tableau[x])
        
    def run(self,nombre_tours,delai):
        """
        Méthode principale du jeu.
        
        Fait tourner le jeu de la vie pendant nombre_tours.
        Elle rafraîchit l'affichage à chaque tour 
        et attend un délai entre chaque tour.
        
        :param nombre_tours: nombre de tours à effectuer
        :param delai: temps d'attente en secondes entre chaque tour
        """
        #ajout des colonnes de 0 a droite et a gauche 
        for x in range(len(self._tableau)):
            self._tableau[x].insert(0,0)
            self._tableau[x].insert(len(self._tableau[x]),0)

        #ajout des lignes de 0 en haut et en bas
        self._tableau.insert(0,[0 for p in range(len(self._tableau[x]))])
        self._tableau.insert(len(self._tableau[x]),[0 for p in range(len(self._tableau[x]))])
        
        for x in range(nombre_tours):
            self.clear()
            self.tour()
            self.affichage()
            time.sleep(delai)
        
    def tour(self):
        """
        Met à jour toutes les cellules du tableau en respectant les règles 
        du jeu de la vie
        """
        self._tableau=verification(self._tableau)
        
    def valeur_case(self,i,j):
        """
        Renvoie la valeur de la case [i][j] ou 0 si la case n'existe pas.
        """
        self._i=i
        self._j=j
        return self._tableau[self._i][self._j]
        
    def total_voisins(self,i,j):
        """
        Renvoie la somme des valeurs des voisins de la case [i][j].
        """
        
        self._i=i
        self._j=j
        for x in range(len(self._tableau)):
            self._tableau[x].insert(0,0)
            self._tableau[x].insert(len(self._tableau[x]),0)

        #ajout des lignes de 0 en haut et en bas
        self._tableau.insert(0,[0 for p in range(len(self._tableau[x]))])
        self._tableau.insert(len(self._tableau[x]),[0 for p in range(len(self._tableau[x]))])
        
        return voisins(self._i,self._j,self._tableau)
        
    def résultat(self,i,j):
        """
        Renvoie la valeur suivante d'une cellule.
        
        :param valeur_case: la valeur de la cellule(0 ou 1)
        :param total_voisins: la somme des valeurs des voisins
        :return: la valeur de la cellule au tour suivant
        """
        
        self._valeur_case=self.valeur_case(i,j)
        self._total_voisins=self.total_voisins(i,j)
        if self._valeur_case==0:
            if self._total_voisins==3:
                self._valeur_case=1
        else:
            if self._total_voisins==1:
                 self._valeur_case=0
            elif self._total_voisins>3:
                self._valeur_case=0
        
        return self._valeur_case
    
    def clear(self):
        """ 
        Renvoie le shell nettoyé
        """
        return print('\n' * 150)


tableau=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


mon_jeu=Jeu(tableau)
#test à faire 1 par 1

"""
mon_jeu.run(100,1)
print(mon_jeu.valeur_case(16,13))
print(mon_jeu.total_voisins(16,13))
print(mon_jeu.résultat(16,13))
"""



    