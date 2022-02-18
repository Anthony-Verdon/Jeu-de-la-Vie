def verification(tab):
    """
    #affichage du tableau avec les ajouts
    for x in range(len(tab)):
        print(tab[x])
    """
    #creation du tableau que l'on va faire évolué 
    tab2 = [ line[:] for line in tab]

    #boucle de verification des valeurs + modification de tab2  
    for x in range(1,len(tab)-1):
    
        for y in range(1,len(tab[x])-1):
            valeurs=0
            x+1
            y+1
            #verification dans la ligne au dessus
            for i in range(-1,2):
                if tab[x-1][y+i]==1:
                    valeurs+=1
                        
            #verification dans la ligne en dessous
            for i in range(-1,2):
                if tab[x+1][y+i]==1:
                    valeurs+=1
        
            #verification du voisin gauche
            if tab[x][y-1]==1:
                valeurs+=1
        
            #verification du voisin droit
            if tab[x][y+1]==1:
                valeurs+=1
        
            #modification du tab2
            if tab2[x][y]==0:
                if valeurs==3:
                    tab2[x][y]=1
                    
            elif tab2[x][y]==1:
                if valeurs==1:
                    tab2[x][y]=0
                elif valeurs>3:
                    tab2[x][y]=0
    
    if tab==tab2:
        print("égal")
    else:      
        tab=tab2
    return tab

"""
#affichage de tab2 modifié
print("---------------")    

for x in range(len(tab2)):
    print(tab2[x])
"""
def voisins(x,y,tab):
        #ajout des colonnes de 0 a droite et a gauche 
        
        valeurs=0
        x+=1
        y+=1
       #verification dans la ligne au dessus
        for i in range(-1,2):
            if tab[x-1][y+i]==1:
                valeurs+=1
                        
        #verification dans la ligne en dessous
        for i in range(-1,2):
            if tab[x+1][y+i]==1:
                valeurs+=1
        
        #verification du voisin gauche
        if tab[x][y-1]==1:
            valeurs+=1
        
        #verification du voisin droit
        if tab[x][y+1]==1:
            valeurs+=1
        return valeurs
"""
print(voisins(1,1))
"""



            
                
        