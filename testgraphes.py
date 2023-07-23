"""
Auteur : Nate
Date de création : le Ma 07/03/2023 à 17h22
Nom : testgraphes.py
"""
from dictionnaireadjacenceoriente import *
from dictionnaireadjacenceorientepondere import *
from queue import Queue

from algosgraphes import *




# graphe orienté - TD2 exo 1 :
G = DictionnaireAdjacenceOriente()
G.ajouter_sommets(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
G.ajouter_arcs([('A', 'B'), ('A', 'F'), ('A', 'G'), ('C', 'A'), ('D', 'F'), ('E', 'D'), ('F', 'E'), ('G', 'C'), ('G', 'E'), ('G', 'J'), ('H', 'G'), ('H', 'I'), ('I', 'H'), ('J', 'K'), ('J', 'L'), ('J', 'M'), ('L', 'G'), ('L', 'M'), ('M', 'L')])

# graphe orienté acyclique (dag) - TD3 exo 1 :
G2 = DictionnaireAdjacenceOriente()
G2.ajouter_sommets(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
G2.ajouter_arcs([('A', 'B'), ('A', 'F'), ('A', 'G'), ('C', 'A'), ('E', 'D'), ('F', 'E'), ('G', 'E'), ('G', 'J'), ('H', 'G'), ('I', 'H'), ('J', 'K'), ('J', 'L'), ('J', 'M'), ('L', 'M')])

# graphe pondéré (non orienté !!!) - TD4 exo 1 :
GP = DictionnaireAdjacenceOrientePondere()
GP.ajouter_sommets(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
GP.ajouter_arcs([('A', 'B', 8), ('A', 'C', 2), ('A', 'D', 5), ('B', 'D', 2), ('C', 'D', 2), ('C', 'E', 5), ('B', 'F', 13), ('D', 'E', 1), ('D', 'F', 6), ('D', 'G', 3), ('E', 'G', 1), ('F', 'G', 2), ('F', 'H', 3), ('G', 'H', 6), ('B', 'A', 8), ('C', 'A', 2), ('D', 'A', 5), ('D', 'B', 2), ('D', 'C', 2), ('E', 'C', 5), ('F', 'B', 13), ('E', 'D', 1), ('F', 'D', 6), ('G', 'D', 3), ('G', 'E', 1), ('G', 'F', 2), ('H', 'F', 3), ('H', 'G', 6)])

# graphe orienté pondéré acyclique (avec poids négatif) - TD3 exo 2 :
DAGP = DictionnaireAdjacenceOrientePondere()
DAGP.ajouter_sommets(['A', 'B', 'C', 'D', 'E'])
DAGP.ajouter_arcs([('A', 'B', 2), ('A', 'C', 5), ('A', 'D', 4), ('B', 'C', 1), ('B', 'E', 2), ('C', 'E', 1), ('D', 'C', -5)])

# graphe orienté pondéré acyclique bis - TD3 exo 2 :
DAGP2 = DictionnaireAdjacenceOrientePondere()
DAGP2.ajouter_sommets(['A', 'B', 'C', 'D', 'E', 'F'])
DAGP2.ajouter_arcs([('A', 'B', 1), ('A', 'C', 2), ('A', 'D', 5), ('B', 'C', 3), ('B', 'D', 5), ('C', 'D', 3), ('D', 'E', 2), ('D', 'F', 4), ('E', 'F', 1)])

# graphe orienté pondéré avec cycle et poids négatifs - TD3 exo 2 :
DCGP = DictionnaireAdjacenceOrientePondere()
DCGP.ajouter_sommets(['A', 'B', 'C', 'D', 'E'])
DCGP.ajouter_arcs([('A', 'B', 2), ('A', 'C', 5), ('B', 'C', 1), ('B', 'E', 2), ('C', 'D', 4), ('C', 'E', 1), ('D', 'C', -5)])

# graphe orienté pondéré avec cycles et poids négatifs non trivial - TD3 exo 4 :
GP2 = DictionnaireAdjacenceOrientePondere()
GP2.ajouter_sommets(['A', 'B', 'C', 'D', 'E', 'F'])
GP2.ajouter_arcs([('A', 'B', 4), ('A', 'C', 2), ('A', 'D', 5), ('A', 'E', 4), ('B', 'A', -2), ('B', 'C', 5), ('B', 'E', -8), ('C', 'D', 2), ('C', 'E', -1), ('D', 'B', 9), ('D', 'F', 3), ('E', 'D', 1), ('F', 'C', -3), ('F', 'E', 15)])

# graphe orienté pondéré non trivial avec cycle négatif - TD3 exo 4 b) : -> E-D-B de poids -1
GP2inf = DictionnaireAdjacenceOrientePondere()
GP2inf.ajouter_sommets(['A', 'B', 'C', 'D', 'E', 'F'])
GP2inf.ajouter_arcs([('A', 'B', 4), ('A', 'C', 2), ('A', 'D', 5), ('A', 'E', 4), ('B', 'A', -2), ('B', 'C', 5), ('B', 'E', -8), ('C', 'D', 2), ('C', 'E', -1), ('D', 'B', 6), ('D', 'F', 3), ('E', 'D', 1), ('F', 'C', -3), ('F', 'E', 15)])

# graphe orienté pondéré cyclique - cours ch4 - "tous les plus courts chemins" - floyd-warshall :
fw = DictionnaireAdjacenceOrientePondere()
fw.ajouter_sommets([1,2,3,4])
fw.ajouter_arcs([(1,3,-2), (2,1,4), (2,3,3), (3,4,2), (4,2,-1)])


