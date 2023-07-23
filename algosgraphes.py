"""
Auteur : Nate
Date création : le Ma 07/03/2023 à 12h27
Nom : algosgraphes.py
"""

from dictionnaireadjacenceoriente import *
from dictionnaireadjacenceorientepondere import *
from queue import Queue
from queue import LifoQueue as Stack
import numpy as np


"""
Ce programme contient les sections et algorithmes suivants :
    ¤ Constantes
        _ init_dico(cles, val_init)
    ¤ Parcours en profondeur récursif
        _ profondeur_r(G)
    ¤ Détection de cycle récursif (profondeur)
    ¤ Parcours en profondeur itératif
    ¤ Parcours en largeur (itératif)
    ¤ Fermeture transitive
    ¤ Composantes Fortement Connexes (CFC)
    ¤ Tri topologique
    ¤ Plus court chemin
"""




## Constantes



green = vert = "green"
red = rouge = "red"
black = noir = "black"

def init_dico (cles, valeur) :
    """
    Créer et initialise un dictionnaire dont on fournit les clés et la valeur commune d'initialisation, puis le renvoie.
    """
    dico = {}
    for k in cles :
        dico[k] = valeur
    return dico



def init_mat (taille, valeur) :
    """
    Créer et initialise une matrice (np.array) carrée dont on fournit la taille et la valeur commune d'initialisation, puis la renvoie.
    """
    return np.full((taille, taille), valeur) #, dtype = int : empêche la valeur NaN (=+inf)



def convertir_sommets_decimaux (G) :
    """
    Copie un graphe et convertit ses sommets en nombres (si ce n'est pas déjà le cas).
    Type traité : DictionnaireAdjacenceOrientePondere
    DAGP2 ok / DAGP ok / DCGP ok / GP2 ok
    """
    n = G.nombre_sommets()
    som = sorted(G.sommets())
    nv_som = list(range(n))#correspondance entre les deux lors de l'ajout des arcs
    nv_G = type(G)()
    for i in nv_som :
        nv_G.ajouter_sommet(i)
    if type(G) == DictionnaireAdjacenceOrientePondere : # autres types à voir
        for i in nv_som :
            for j in nv_som :
                if G.contient_arc(som[i], som[j]) :
                    p = G.poids_arc(som[i], som[j])
                    nv_G.ajouter_arc(i, j, p)
        return nv_G
    



## Parcours en profondeur récursif



def profondeur_r (G) :
    """
    Parcours le graphe en profondeur de manière récursive.
    G : graphe à  parcourir.
    retour : liste des sommets parcourus (dans l'ordre de début de parcours).
    """
    resultat = []
    visites = init_dico(G.sommets(), green)
    for s in G.sommets() :
        if visites[s] == green :
            profondeur_rec(G, s, visites, resultat)
    return resultat



def profondeur_rec (G, sommet, visites, resultat) :
    """
    Parcours le graphe en profondeur et de manière récursive à partir du sommet fournit.
    G : graphe à parcourir;
    sommet : racine du parcours;
    visites : dictionnaire de l'état du parcours pour chaque sommet;
    resultat : liste des sommets déjà parcourus.
    retour : rien.
    """
    visites[sommet] = red
    resultat.append(sommet)
    for succ in G.successeurs(sommet) :
        if visites[succ] == green :
            profondeur_rec(G, succ, visites, resultat)
    visites[sommet] = black



## Détection de cycle récursif (profondeur)



def contient_cycle_oriente (G) :
    """
    Détecte un cycle orienté.
    G : graphe à parcourir.
    retour : True si un cycle orienté est détecté par un parcours en profondeur.
    """
    visites = init_dico(G.sommets(), green)
    for s in G.sommets() :
        if visites[s] == green :
            if contient_cycle_oriente_rec(G, s, visites) :
                return True
    return False



def contient_cycle_oriente_rec (G, sommet, visites) :
    """
    Détecte un cycle orienté à partir du sommet par un parcours en profondeur.
    G : graphe à parcourir;
    sommet : racine du parcours;
    visites : dictionnaire de l'état du parcours pour chaque sommet.
    retour : True si un cycle orienté est détecté par le parcours en profondeur depuis sommet, False sinon.
    """
    visites[sommet] = red
    for succ in G.successeurs(sommet) :
        if visites[succ] == green :
            if contient_cycle_oriente_rec(G, succ, visites) :
                return True
        if visites[succ] == red :
            return True
    visites[sommet] = black
    return False



## Parcours en profondeur itératif



def profondeur_i (G) :
    """
    Parcours le graphe en profondeur de manière itérative.
    G : graphe à  parcourir.
    retour : liste des sommets parcourus (dans l'ordre de début de parcours).
    """
    resultat = []
    visites = init_dico(G.sommets(), False)
    for s in G.sommets() :
        if  not visites[s] :
            resultat += profondeur_iter(G, s, visites)
    return resultat



def profondeur_iter (G, depart, visites = None) :
    """
    Parcours le graphe en profondeur et de manière itérative à partir du sommet fournit.
    G : graphe à parcourir;
    depart : racine du parcours;
    visites : dictionnaire de l'état du parcours pour chaque sommet.
    retour : liste des sommets parcourus (atteignables depuis le sommet de départ).
    On peut utiliser cette fonction à partir d'un sommet au choix (en laissant visites par défaut) ou l'utiliser dans une fonction de parcours plus global qui fournira alors le dictionnaire visites.
    Remarques : 
    _ utiliser sorted au lieu de reversed pour parcourir dans l'ordre naturel (s'il existe) - meilleur visuel mmais plus coûteux
    _ utiliser reversed pour obtenir le même ordre que la version récursive - plus cohérent mais un peux coûteux
    _ sorted et reversed sont tous les deux facultatifs : le parcours sera différent mais ce sera bien en profondeur.
    """
    resultat = []
    if visites == None :
        visites = init_dico(G.sommets(), False)
    a_traiter = Stack()
    a_traiter.put_nowait(depart)
    while not a_traiter.empty() :
        sommet = a_traiter.get_nowait()
        if not visites[sommet] :
            resultat.append(sommet)
            visites[sommet] = True
            for succ in reversed(list(G.successeurs(sommet))) :#sorted, reverse = True
                if not visites[succ] :
                    a_traiter.put_nowait(succ)
    return resultat
    



## Parcours en largeur (itératif)



def largeur_i (G) :
    """
    Parcours le graphe en largeur de manière itérative.
    G : graphe à  parcourir.
    retour : liste des sommets parcourus (dans l'ordre de début de parcours).
    """
    resultat = []
    visites = init_dico(G.sommets(), False)
    for s in G.sommets() :
        if  not visites[s] :
            resultat += largeur_iter(G, s, visites)
    return resultat



def largeur_iter (G, depart, visites = None) :# à compléter avec une fonction de parcours sur les sommets de départ
    """
    Parcours le graphe en largeur et de manière itérative depuis le sommet de départ.
    G : graphe à parcourir;
    depart : sommet de départ de l'exploration;
    visites : dictionnaire de l'état du parcours pour chaque sommet (facultatif).
    retour : liste des sommets dans l'ordre du parcours.
    On peut utiliser cette fonction à partir d'un sommet au choix (en laissant visites par défaut) ou l'utiliser dans une fonction de parcours plus global qui fournira alors le dictionnaire visites.
    """
    resultat = []
    if visites == None :
        visites = init_dico(G.sommets(), False)
    a_traiter = Queue()
    a_traiter.put_nowait(depart)
    while not a_traiter.empty() :
        sommet = a_traiter.get_nowait()
        if not visites[sommet] :
            resultat.append(sommet)
            visites[sommet] = True
            for succ in G.successeurs(sommet) :
                if not visites[succ] :
                    a_traiter.put_nowait(succ)
    return resultat



## Fermeture transitive



def fermeture_transitive (G) :
    """
    Calcule la fermeture transitive du graphe.
    G : un graphe orienté (connexe ?).
    retour : la fermeture transitive de G.
    """
    F = type(G)()
    F.ajouter_sommets(G.sommets())
    for u in G.sommets() :
        for v in largeur_iter(G, u) :
            if u != v :
                F.ajouter_arc(u, v)
    return F



## Composantes Fortement Connexes (CFC)



def profondeur_dates (G) :
    """
    Renvoie une pile des sommets parcourus en profondeur.
    """
    pile = Stack()
    visite = init_dico(G.sommets(), False)
    for s in G.sommets() :
        if not visite[s] :
            profondeur_dates_rec(G, s, visite, pile)
    return pile



def profondeur_dates_rec (G, depart, visite, pile) :
    """
    Empile les sommets au fur et à mesure de leur parcours en profondeur à partir d'un sommet de départ.
    """
    visite[depart] = True
    for succ in G.successeurs(depart) :
        if not visite[succ] :
            profondeur_dates_rec(G, succ, visite, pile)
    pile.put_nowait(depart)



def renverser_arcs (G) :
    """
    Renvoie un graphe dont toutes les arêtes sont les inversées du graphe fournit.
    """
    G_inv = type(G)()
    G_inv.ajouter_sommets(G.sommets())
    G_inv.ajouter_arcs([(v, u) for (u,v) in G.arcs()])
    return G_inv



def kosaraju_sharir (G) :
    """
    Renvoie la liste des Composantes Fortement Connexes.
    Une CFC étant une liste de sommets.
    """
    cfc = []
    pile = profondeur_dates(G)
    Gprime = renverser_arcs(G)
    visites = init_dico(G.sommets(), False)
    while not pile.empty() :
        v = pile.get_nowait()
        if not visites[v] :
            composante = profondeur_iter(Gprime, v, visites)
            cfc.append(composante)
    return cfc



## tri topologique



def kahn (G) :
    """
    Renvoie la liste des sommets en suivant un ordre topologique.
    Un ordre topologique n'étant pas unique.
    """
    resultat = []
    sources = Stack()
    degres_entrants = init_dico(G.sommets(), 0)
    for s in G.sommets() :
        degres_entrants[s] = G.degre_entrant(s)
        if degres_entrants[s] == 0 :
            sources.put_nowait(s)
    while not sources.empty() :
        u = sources.get_nowait()
        resultat.append(u)
        for v in G.successeurs(u) :
            degres_entrants[v] -= 1
            if degres_entrants[v] == 0 :
                sources.put_nowait(v)
    return resultat



## plus courts chemins



def extraire_sommet_le_plus_proche (S, distances) :
    """
    Extrait le sommet le plus proche du sommet de base choisit, parmis l'ensemble S des sommets fournits.
    L'extraction se fait à l'aide d'un dictionnaire des distances au sommet de base fournit en argument.
    """
    sommet = None
    distance_min = None
    for candidat in S :
        if distance_min == None or (distances[candidat] != None and distances[candidat] < distance_min) :
            sommet = candidat
            distance_min = distances[candidat]
    if sommet != None :
        S.remove(sommet)
    return sommet



def dijkstra (G, source) :
    """
    Renvoie un dictionnaire des plus courtes distances du sommet source choisit à chacun des sommets.
    Le sommet "source" fourni en argument sert de point de départ au calcul des distances. Ce n'est pas forcément réellement un sommet source au sens mathématiques.
    Nécessite un graphe orienté pondéré avec uniquement des poids positifs.
    """
    a_traiter = G.sommets()
    distances = init_dico(G.sommets(), None)
    distances[source] = 0
    while len(a_traiter) > 0 :
        u = extraire_sommet_le_plus_proche(a_traiter, distances)
        if u == None :
            return distances
        for v in G.successeurs(u) :
            if distances[v] == None :
                distances[v] = distances[u] + G.poids_arc(u, v)
            else :
                distances[v] = min(distances[v], distances[u] + G.poids_arc(u, v))
    return distances



def dijkstra_acyclique (G, source) :
    """
    Renvoie un dictionnaire des plus courtes distances du sommet source choisit à chacun des sommets.
    Le sommet "source" fourni en argument sert de point de départ au calcul des distances. Ce n'est pas forcément réellement un sommet source au sens mathématiques.
    Nécessite un graphe orienté pondéré avec uniquement des poids positifs.
    +inf à adapter... algo incomplet !
    G est acyclique : des sommets peuvent ne pas être atteints depuis la src : d'où le bordel.
    ok normalement !
    besoin d'un graphe orienté pondéré acyclique (mais peut avoir des poids négatifs). -> construire à partir de td3 exo2.
    Description à refaire...
    """
    distances = init_dico(G.sommets(), None)
    distances[source] = 0
    for u in kahn(G) :
        for v in G.successeurs(u) :
            if distances[u] == None :
                distances[v] = distances[v]
            elif distances[v] == None :
                distances[v] = distances[u] + G.poids_arc(u, v)
            else :
                distances[v] = min(distances[v], distances[u] + G.poids_arc(u, v))
    return distances



def bellman_ford (G, source) :
    """
    Renvoie un dictionnaire des plus courtes distances du sommet source choisit à chacun des sommets.
    Le sommet "source" fourni en argument sert de point de départ au calcul des distances. Ce n'est pas forcément réellement un sommet source au sens mathématiques.
    Nécessite un graphe orienté pondéré quelconque (renvoie None si un cycle de poids négatif est atteignable depuis le sommet de départ).
    parcours dans un ordre topo ?
    erreur si des sommets ne sont pas atteignables : TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' ?
    """
    distances = init_dico(G.sommets(), None)
    distances[source] = 0
    # parcours de chaque arc nb_sommmets-1 fois
    for i in range(1, G.nombre_sommets()) :
        # parcours de chaque arc
        for (u, v, p) in G.arcs() :
            if distances[u] == None :
                distances[v] = distances[v]
            elif distances[v] == None :
                distances[v] = distances[u] + p
            else :
                distances[v] = min(distances[v], distances[u] + p)
    # détection de cycle négatif
    for (u, v, p) in G.arcs() :
        #print("u : ", u, ", dist : ", distances[u], " / v : ", v, ", dist : ", distances[v])
        # soit u n'est pas atteignable : pas de test possible (si v est malgré tout atteignable par un autre arc, il sera traité avec celui-ci)
        if distances[u] == None :
            continue
        # soit u et v sont atteignables : on vérifie (si u est atteignable, alors forcément v aussi)
        if distances[v] > distances[u] + p :
            return None
    return distances



def floyd_warshall (G) :
    """
    Renvoie une matrice des plus courtes distances entre chaque couple de sommet.
    Nécessite un graphe orienté pondéré (algo identique pour graphe non-orienté).
    graphe(s) de test ? DAGP2, DAGP, DCGP puis plus durs GP2, GP2inf
    /!\ DAGP2 : bcp trop de nan -> seuls les poids des arcs directs sont maj /!\
    /!\ fw : les nan ne sont pas mis à jour (comparaison inefficiente) /!\
    comparaison avec nan ??? (et pas None)
    """
    G = convertir_sommets_decimaux(G)
    n = G.nombre_sommets()
    distances = init_mat(n, None)
    print("n = ", n)
    # distances des sommets à eux-mêmes
    for i in range(n) :
        distances[i, i] = 0
    print("distances sommets :\n", distances)
    # distances des sommets à leurs voisins
    for (u, v, p) in G.arcs() :
        print("u : ", u, " -> v : ", v, " => p : ", p)
        distances[u, v] = p
    print("distances voisins :\n", distances)
    # mises à jours successives
    for k in range(n) :
        print("k = ", k, " :\n", distances)
        if k == 1 :
            print("k = ", k)
        for i in range(n) :
            if i == 3 :
                print("i = ", i)
            for j in range(n) :
                if j == 0 :
                    print("j = ", j)
                if k == 1 and i == 3 and j == 0 :
                    print("(k, i, j) : ", k, i, j, "\n", "d(i,k) :\n", distances[i, k], "\nd(k,j) :\n", distances[k, j], "\nd(i,j) :\n", distances[i, j])
                if distances[i, k] == None or distances[k, j] == None :
                    if k == 1 and i == 3 and j == 0 :
                        print("pass")
                    pass
                elif distances[i, j] is np.nan :    # TEST !
                    if k == 1 and i == 3 and j == 0 :
                        print("remplace")
                    distances[i, j] = distances[i, k] + distances[k, j]
                else :
                    if k == 1 and i == 3 and j == 0 :
                        print("calcul")
                    distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])
    return distances
    
    




