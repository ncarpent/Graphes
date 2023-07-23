"""
Créé le 22/02/2023 à 18h47
Auteur : Nate
graphe_naif.py
"""

from graphes_elements import *

class Graphe :
    
    """
    Cette classe définit une implémentation de graphes.
    Elle utilise une liste de sommets et une liste d'arrêtes.
    Cette implémentation correspond à la définition mathématique d'un graphe mais est à priori assez naïve et donc n'est pas optimale.
    
    Méthodes :
        ¤ Edition de l'objet :
            __init__                                        (ok)
            __repr__                                        (ok)
            (__str__?)
        ¤ Méthodes de conteneur ?
        ¤ Opérateurs mathématiques ?
        ¤ Méthodes de comparaison ?
        ¤ Autres :
        -> Ajout d'élément :
            ajouter_sommet(s)                               (ok) juste valeur
            ajouter_sommets(seq_s)                          (ok) juste valeurs
            ajouter_arete(u,v)                              (~ lever excep) juste val des somm
            ajouter_aretes(seq_a)                           (ok) juste valeurs des som
        -> Sous-graphe :
            sous_graphe_engendre (seq_s)                    (ok)
            sous_graphe (seq_s, seq_a)                      (ok)
            est_sous_graphe                                 (ok)
            est_super_graphe                                (ok)
        -> Cardinaux :
            nombre_sommets()                                (ok)
            nombre_aretes()                                 (ok)
            nombre_boucles()                                (ok)
            +nombre_aretes_multiples()                      (ok) intérêt ???
        -> Eléments :
            +sommet(val)                                    (ok) et si val est un sommet ?????!!!!!!
            sommets()                                       (ok) liste somm ou liste val ?
            +sommets_isoles()                               (ok)
            +arete(u,v)                                     (ok)
            aretes()                                        (ok) liste arr ou liste set(vals) ???
            +aretes_incidentes(s)                           (ok)
            +aretes_occurences()                            (ok)
            +aretes_multiples()                             (ok)
            boucles()                                       (ok)
            +boucles_multiples()                            (ok)
            +extraire_sommets(seq_num)                      (ok)
            +extraire_aretes(seq_num)                       (ok)
        -> Tests de contenance :
            contient_arete(u,v)                             (ok)
            +contient_aretes(seq_a)                         (ok) amel possible
            contient_sommet(s)                              (ok)
            +contient_sommets(seq_s)                        (ok) amel possible
            +indice_sommet(val)                             (ok)
            +indice_arete(u,v)                              (ok) intérêt limité...
        -> Voisinage :
            degre(s)                                        (ok)
            voisins(s)                                      (ok)
        -> Suppression d'élément :
            retirer_arete(u,v)                              (ok)
            +retirer_multiarete(u,v)                        (ok) option pour laisser une arete simple ok, amel : gestion mem de la lgr
            retirer_aretes(seq_a)                           (ok)
            retirer_sommet(s)                               (ok)
            retirer_sommets(seq_s)                          (ok)
            +retirer_aretes_multiples()                     (ok)
            +retirer_boucles()                              (ok)
            +retirer_sommets_isoles()                       (ok)
            +vider_aretes()                                 (ok)
            +vider_sommets()                                (ok)
            +est_simple()                                   (ok)
            +simplifier()                                   (ok) (arr mult et/ou boucles mais pas somm isol)
    Fonctions :
    Idées :
    _ bonus : retirer_k_multiarete (cpt au lieu de bool)
    _ Refaire la hashabilité des Sommets et définir l'égalité sur les valeurs. Les poids on vera plus tard... ?
    Remarques :
    """
    
    
    
    ## Edition de l'objet
    
    
    
    def __init__ (self) :
        """
        Construit un Graphe. Celui-ci contient une liste de sommets et une liste d'Aretes.
        """
        self.som = []
        self.are = []
    
    
    
    def __repr__ (self) :
        """
        Affiche un graphe. Liste tous ses Sommets et toutes ses Aretes.
        """
        som = [s.__repr__() for s in self.som]
        are = [a.__repr__() for a in self.are]
        return "graphe :\n" + "|-sommets : " + ", ".join(som) + "\n" + "|-aretes : " + ", ".join(are) + "\n"
    
    
    
    ## Autres :
    
    
    
    ### Ajout d'élément
    
    
    
    def ajouter_sommet (self, val) :
        """
        Ajoute au Graphe le Sommet s.
        Si le Sommet est déjà présent, il n'est pas ajouté.
        """
        if not self.contient_sommet(val) :
            s = Sommet(val)
            self.som.append(s)
    
    
    
    def ajouter_sommets (self, *vals) :
        """
        Ajoute au Graphe tous les Sommets de la séquence seq_s.
        Les Sommets déjà présents ne sont pas ajoutés.
        """
        for v in vals :
            self.ajouter_sommet(v)
    
    
    
    def ajouter_arete (self, val1, val2) :
        """
        Ajoute au graphe l'Arete en donnant les valeurs de ses extrémités.
        L'Arete n'est ajoutée que si le Sommets sont déjà présents. Il est possible d'ajouter plusieurs fois la même Arete.
        """
        s1 = self.sommet(val1)
        s2 = self.sommet(val2)
        if s1 != None and s2 != None :
            self.are.append(Arete(s1, s2))
    
    
    
    def ajouter_aretes (self, *vals) :
        """
        Ajoute au Graphe toutes les Aretes fournies en argument.
        Les Aretes doivent être sous la forme de couples de valeurs, correspondant aux extrémités.
        """
        for val1, val2 in vals :
            self.ajouter_arete(val1, val2)
    
    
    
    ### Sous-graphes
    
    
    
    def sous_graphe_engendre (self, *seq_s) :
        """
        Renvoie le sous-graphe engendré par la séquence de sommet(s) fournis.
        Peut recevoir 0, 1 ou plusieurs sommets. Les sommets sont transmis par leur valeur et doivent appartenir au Graphe d'origine.
        """
        ret = Graphe()
        if not self.contient_sommets(*seq_s) :
            raise ValueError("Le Graphe d'origine ne contient pas tous les sommets fournis dans " + str(seq_s) + ".")
        ret.ajouter_sommets(*seq_s)
        for a in self.are :
            s1 = a.valeur()
            s2 = a.autre_extremite(self.sommet(s1)).val
            if s1 in seq_s and s2 in seq_s :
                ret.ajouter_arete(s1, s2)
        return ret
    
    
    """
    def sous_graphe_a (self, seq_a) :
        
        Génère un sous-graphe comportant les mêmes Sommets et dont on spécifie les Aretes à conserver.
        
        ret = Graphe()
        for s in self.som :
            ret.ajouter_sommet(s.val)
        for a in seq_a :
            if not self.contient_arete(a[0], a[1]) :
                raise ValueError("Tentative de génération d'un sous-graphe avec une Arete qui n'est pas dans le graphe.")
            ret.ajouter_arete(a[0], a[1])
        return ret
    """
    
    
    def sous_graphe (self, seq_s = None, seq_a = None) :
        """
        seq_s : séquence de valeurs / seq_a : séquence de couples de valeurs.
        """
        if seq_s == None :
            seq_s = [s.val for s in self.som]
            print("seq_s : ", seq_s)
        if seq_a == None :
            return self.sous_graphe_engendre(*seq_s)
        ret = Graphe()
        if not self.contient_sommets(*seq_s) :
            raise ValueError("Le Graphe d'origine ne contient pas tous les Sommets de " + str(seq_s) + ".")
        ret.ajouter_sommets(*seq_s)
        if not self.contient_aretes(*seq_a) :
            raise ValueError("Le Graphe d'origine ne contient pas toutes les Aretes de " + str(seq_a) + ".")
        occ = self.aretes_occurences()
        occ_list = {}
        for a in seq_a :
            extrs = (self.sommet(a[0]), self.sommet(a[1]))
            ar = Arete(*extrs)
            occ_list[ar] = occ_list.setdefault(ar, 0) + 1
            if occ_list[ar] > occ[ar] :
                raise ValueError ("L'Arete " + str(ar) + " est présente dans le sous-graphe en plus d'exemplaires qu'elle ne l'est dans le graphe.")
        for a in seq_a :
            if not a[0] in seq_s :
                raise ValueError("Création d'un sous-graphe avec l'Arete " + str(a) + " alors que le sommet " + str(a[0]) + " n'appartient pas au sous-graphe.")
            if not a[1] in seq_s :
                raise ValueError("Création d'un sous-graphe avec l'Arete " + str(a) + " alors que le sommet " + str(a[1]) + " n'appartient pas au sous-graphe.")
            ret.ajouter_arete(*a)
        return ret
    
    
    
    def est_sous_graphe (self, graphe) :
        """
        Test si le Graphe est un sous-graphe du Graphe fourni.
        """
        test = True
        for s in self.sommets() :
            test = test and s in graphe.sommets()
        occ = self.aretes_occurences()
        g_occ = graphe.aretes_occurences()
        for a in self.aretes() :
            if a in graphe.aretes() :
                test = test and occ[a] <= g_occ[a]
            else :
                return False
        return test
    
    
    
    def est_sur_graphe (self, graphe) :
        """
        Teste si le Graphe est un sur-graphe du Graphe fourni en argument (ie: le Graphe fourni en argument est un sous-graphe du Graphe).
        """
        return graphe.est_sous_graphe(self)
    
    
    
    ### Cardinaux
    
    
    
    def nombre_sommets (self) :
        """
        Renvoie le nombre de Sommets du Graphe.
        """
        return len(self.som)
    
    
    
    def nombre_aretes (self) :
        """
        Renvoie le nombre d'Aretes du Graphe.
        """
        return len(self.are)
    
    
    
    def nombre_boucles (self) :
        """
        Renvoie le nombre de boucles du Graphe.
        """
        cpt = 0
        for a in self.are :
            if a.est_boucle() :
                cpt += 1
        return cpt
    
    
    
    def nombre_aretes_multiples (self) :
        """
        Renvoie le nombre d'Aretes qui admettent des Aretes parallèles.
        """
        return len(self.aretes_multiples())
    
    
    
    ### Eléments
    
    
    
    def sommet (self, val) :
        """
        Renvoie le Sommet du Graphe qui a la valeur demandée.
        Renvoie None si le Sommet n'est pas trouvé.
        """
        for s in self.som :
            if s == Sommet(val) :
                return s
        return None
    
    
    
    def sommets (self) :
        """
        Renvoie la liste des Sommets.
        """
        return self.som
    
    
    
    def sommets_isoles (self) :
        """
        Renvoie la liste des Sommets qui sont isolés.
        """
        ret = []
        for s in self.som :
            if self.degre(s) == 0 :
                ret.append(s)
        return ret
    
    
    
    def arete (self, val1, val2) :
        """
        Renvoie la première Arete du Graphe dont les extrémités ont les valeurs fournies.
        Renvoie None si l'Arete n'a pas été trouvée.
        Lève une exception si les Sommets correspondant aux valeurs n'ont pas été trouvés.
        """
        s1 = self.sommet(val1)
        s2 = self.sommet(val2)
        if s1 != None and s2 != None :
            are = Arete(s1, s2)
            for a in self.are :
                if a == are :
                    return a
            return None
        raise ValueError("Les valeurs fournies ne correspondent pas à des Sommets du Graphe.")
    
    
    
    def aretes (self) :
        """
        Renvoie la liste des Aretes.
        """
        return self.are
    
    
    
    def aretes_incidentes (self, val) :
        """
        Renvoie la liste des Aretes incidentes à un Sommet de Graphe.
        Le Sommet doit exister et être dans le Graphe.
        """
        ret = []
        s = self.sommet(val)
        if s == None :
            raise ValueError("La valeur " + str(val) + " ne correspond à aucun Sommet du Graphe.")
        for a in self.are :
            if a.a_extremite(s) :
                ret.append(a)
        return ret
    
    
    
    def aretes_occurences (self) :
        """
        Renvoie un dictionnaire d'occurences des Aretes.
        Pour chaque Arete, le dictionnaire associe le nombre d'Aretes (éventuellement multiples) qui relient les deux Sommmets.
        """
        ret = dict()
        for a in self.are :
            ret[a] = ret.setdefault(a, 0) + 1
        return ret
    
    
    
    def aretes_multiples (self) :
        """
        Renvoie un dictionnaire d'occurences des Aretes multiples.
        Pour chaque Arete, le dictionnaire associe le nombre d'Aretes multiples qui relient les deux Sommets.
        """
        occ = self.aretes_occurences()
        ret = dict()
        for k in occ.keys() :
            if occ[k] > 1 :
                ret[k] = occ[k]
        return ret
    
    
    
    def boucles (self) :
        """
        Renvoie la liste des Aretes qui sont des boucles.
        """
        ret = []
        for a in self.are :
            if a.est_boucle() :
                ret.append(a)
        return ret
    
    
    
    def boucles_multiples (self) :
        """
        Renvoie un dictionnaire d'occurences des boucles multiples.
        Pour chaque Arete, le dictionnairee associe le nombre d'Aretes multiples qui sont des boucles qui relient le Sommet à lui-même.
        """
        occ = self.aretes_occurences()
        ret = dict()
        for k in occ.keys() :
            if occ[k] > 1 and k.est_boucle() :
                ret[k] = occ[k]
        return ret
    
    
    
    def extraire_sommets (self, *seq_num) :
        """
        Renvoie la liste des Sommets du Graphe dont on a fournit les indices en argument.
        """
        ret = []
        for i in seq_num :
            if type(i) != int :
                raise TypeError(str(i) + " de type " + str(type(i)) + " n'est pas un " + str(int) + ".")
            ret.append(self.som[i])
        return ret
    
    
    
    def extraire_aretes (self, *seq_num) :
        """
        Renvoie la liste des Aretes du Graphe dont on a fournit les indices en argument.
        """
        ret = []
        for i in seq_num :
            if type(i) != int :
                raise TypeError(str(i) + " de type " + str(type(i)) + " n'est pas un " + str(int) + ".")
            ret.append(self.are[i])
        return ret
    
    
    
    ### Tests de contenance
    
    
    
    def contient_sommet (self, val) :
        """
        Teste si une valeur est un sommet qui apppartient au Graphe.
        """
        s = Sommet(val)
        return s in self.sommets()
    
    
    
    def contient_sommets (self, *seq_s) :
        """
        Teste si tous les Sommets d'une séquence appartienne au Graphe.
        """
        boo = True
        for s in seq_s :
            boo = boo and self.contient_sommet(s)
        return boo
    
    
    
    def contient_arete (self, val1, val2) :
        """
        Teste si deux valeurs données sont des extrémités d'une Arete qui appartient au Graphe.
        Les valeurs doivent être des Sommets valides.
        """
        if not self.contient_sommet(val1) :
            raise ValueError("La valeur " + str(val1) + " ne correspond à aucun Sommet du Graphe.")
        if not self.contient_sommet(val2) :
            raise ValueError("La valeur " + str(val2) + " ne correspond à aucun Sommet du Graphe.")
        s1 = self.sommet(val1)
        s2 = self.sommet(val2)
        a = Arete(s1, s2)
        return a in self.aretes()
    
    
    
    def contient_aretes (self, *seq_cpl) :
        """
        Test si toutes les Aretes d'une séquence appartiennent au Graphe.
        Les Aretes doivent être passées sous forme de couples de valeurs correspondant aux valeurs des extrémités.
        """
        boo = True
        for vals in seq_cpl :
            boo = boo and self.contient_arete(*vals)
        return boo
    
    
    
    def indice_sommet (self, val) :
        """
        Renvoie l'indice d'un Sommet du Graphe.
        Renvoie -1 si la valeur ne correspond à aucun Sommet.
        """
        s = Sommet(val)
        for i in range(len(self.som)) :
            if self.som[i] == s :
                return i
        return -1
    
    
    
    def indice_arete (self, val1, val2) :
        """
        Renvoie l'indice d'une Arete du Graphe (de la première Arete parallèle trouvée).
        Renvoie -1 si les valeurs ne corespondent à aucune Arete.
        Lève une exception si les valeurs ne correspondent à aucun Sommet. 
        """
        s1 = self.sommet(val1)
        s2 = self.sommet(val2)
        if s1 == None :
            raise ValueError("La valeur " + str(val1) + " ne correspond à aucun Sommet du Graphe.")
        if s2 == None :
            raise ValueError("La valeur " + str(val2) + " ne correspond à aucun Sommet du Graphe.")
        a = Arete(s1, s2)
        for i in range(len(self.are)) :
            if self.are[i] == a :
                return i
        return -1
    
    
    
    ### Voisinage
    
    
    
    def degre (self, val) :
        """
        Renvoie le degré d'un Sommet du Graphe.
        """
        d = 0
        if val in self.som :
            s = val
        else :
            s = self.sommet(val)
            if s == None :
                raise ValueError("La valeur " + str(val) + " ne correspond à aucun Sommet du Graphe.")
        for a in self.are :
            if a.a_extremite(s) :
                d += 1
                if a.est_boucle() :
                    d += 1
        return d
    
    
    
    def voisins (self, val) :
        """
        Renvoie la liste des voisins du Sommet dont la valeur est fournie.
        NB : le sommet peut être son propre voisin s'il est extrémité d'une boucle.
        """
        v = set()
        if val in self.som :
            s = val
        else :
            s = self.sommet(val)
            if s == None :
                raise ValueError("La valeur " + str(val) + " ne correspond à aucun Sommet du Graphe.")
        for a in self.are :
            if a.a_extremite(s) :
                v.add(a.autre_extremite(s))
        return list(v)
    
    
    
    ### Suppression d'élement
    
    
    
    def retirer_arete (self, val1, val2) :
        """
        Retire l'Arete dont on fournit les valeurs des extrémités du Graphe.
        Les Sommets et l'Arete doivent exister et être dans le Graphe.
        """
        s1 = self.sommet(val1)
        s2 = self.sommet(val2)
        if s1 == None :
            raise ValueError("La valeur " + str(val1) + " ne correspond à aucun Sommet du Graphe.")
        if s2 == None :
            raise ValueError("La valeur " + str(val2) + " ne correspond à aucun Sommet du Graphe.")
        a = Arete(s1, s2)
        for i in range(len(self.are)) :
            if a == self.are[i] :
                return self.are.pop(i)
        raise ValueError("Les sommets de valeurs " + str(val1) + " et " + str(val2) + " ne sont pas reliés.")
    
    
    
    def retirer_multiarete (self, val1, val2, keepone = True) :
        """
        Retire les Aretes multiples présentes entre deux sommets dont on fournit les valeurs.
        Les Sommets doivent exister mais pas forcément les Aretes.
        Si le paramètre optionnel keepone vaut True (valeur par défaut) : il restera une Arete, qui ne sera donc plus multiple.
        Si keepone vaut False : toutes les Aretes entre les deux Sommets seront supprimmées.
        Le cas échéant, renvoie l'Arete encore présente et None dans tous les autres cas.
        """
        s1 = self.sommet(val1)
        s2 = self.sommet(val2)
        ret = None
        if s1 == None :
            raise ValueError("La valeur " + str(val1) + " ne correspond à aucun Sommet du Graphe.")
        if s2 == None :
            raise ValueError("La valeur " + str(val2) + " ne correspond à aucun Sommet du Graphe.")
        a = Arete(s1, s2)
        i = 0
        while i < len(self.are) :
            if a == self.are[i] and keepone:
                keepone = False
                ret = self.are[i]
                i += 1
            elif a == self.are[i] :
                self.are.pop(i)
            else :
                i += 1
        return ret
    
    
    
    def retirer_aretes (self, *seq_cpl) :
        """
        Retire toutes les Aretes fournies en argument du Graphe.
        Les Aretes doivent être fournies sous la forme de couples de valeurs, correspondant aux extrémités.
        Lève une exception si l'un des Sommet ou l'une des Aretes n'existe pas ou n'est pas dans le Graphe.
        """
        for val1, val2 in seq_cpl :
            self.retirer_arete(val1, val2)
    
    
    
    def retirer_sommet (self, val) :
        """
        Retire le Sommet dont on fournit la valeur du Graphe, ainsi que toutes ses Aretes incidentes.
        Le Sommet doit exister et être dans le Graphe.
        """
        i = self.indice_sommet(val)
        if i == -1 :
            raise ValueError("Le Sommet de valeur " + str(val) + " n'est pas dans le Graphe.")
        s = self.sommet(val)
        inc = self.aretes_incidentes(val)
        for a in inc :
            vois = a.autre_extremite(s).val
            self.retirer_arete(val, vois)
        return self.som.pop(i)
    
    
    
    def retirer_sommets (self, *seq_s) :
        """
        Retire du Graphe tous les Sommets de la séquence, ainsi que leurs Aretes incidentes.
        Les Sommets doivent tous exister et être dans le Graphe.
        """
        for val in seq_s :
            self.retirer_sommet(val)
    
    
    
    def retirer_aretes_multiples (self) :
        """
        Pour toutes les Aretes, retire les Aretes qui lui sont parallèles de telle sorte que le Graphe ne contienne que des Aretes simples.
        L'implémentation des classes Sommet et Arete est à revoir pour un code plus propre.
        """
        arr = self.aretes_multiples()
        for a in arr.keys() :
            val1 = a.valeur()
            val2 = a.autre_extremite(self.sommet(val1)).val
            self.retirer_multiarete(val1, val2)
    
    
    
    def retirer_boucles (self) :
        """
        Retire toutes les boucles du Graphe.
        """
        i = 0
        while i < len(self.are) :
            if self.are[i].est_boucle() :
                self.are.pop(i)
            else :
                i += 1
    
    
    
    def retirer_sommets_isoles (self) :
        """
        Retire tous les Sommets qui sont isolés du Graphe.
        """
        isol = self.sommets_isoles()
        for s in isol :
            self.som.remove(s)
    
    
    
    def vider_aretes (self) :
        """
        Retire toutes les Aretes du Graphe.
        """
        while self.nombre_aretes() > 0 :
            a = self.are[0]
            val1 = a.valeur()
            val2 = a.autre_extremite(self.sommet(val1)).val
            self.retirer_arete(val1, val2)
    
    
    
    def vider_sommets (self) :
        """
        Retire tous les Sommets du Graphe (en ayant au préalable retiré toutes les Aretes).
        """
        self.vider_aretes()
        while self.nombre_sommets() > 0 :
            val = self.som[0].val
            self.retirer_sommet(val)
    
    
    
    def est_simple (self) :
        """
        Renvoie True si le Graphe est simple, False sinon.
        Le Graphe est simple s'il n'a ni boucle, ni arêtes multiples.
        """
        if self.nombre_boucles() > 0 :
            return False
        if len(self.aretes_multiples()) > 0 :
            return False
        return True
    
    
    
    def simplifier (self) :
        """
        Simplifie le Graphe : retire toutes les boucles du Graphe ainsi que les Aretes multiples (mais pas les Sommets isolés).
        """
        self.retirer_aretes_multiples()
        self.retirer_boucles()





class GrapheOriente :
    
    """
    Cette classe définit une implémentation de graphes orientés.
    Elle utilise une liste de sommets et une liste d'arcs.
    Cette implémentation correspond à la définition mathématique d'un graphe orienté mais est à priori assez naïve et donc n'est pas optimale.
    
    Méthodes :
        ¤ Edition de l'objet :
            __init__()                                      (ok)
            __repr__()                                      (ok)
        ¤ Méthodes de conteneur ?
        ¤ Opérateurs mathématiques ?
        ¤ Opérateurs de comparaison ?
        ¤ Autre :
        -> Ajout d'élément :
            ajouter_sommet                                  (tmp) -contient sommet
            ajouter_sommets                                 (ok)
            ajouter_arc                                     (tmp) -sommet
            ajouter_arc_oppose                              (ok)
            ajouter_arcs                                    (ok)
            ajouter_arcs_opposes                            (ok)
        -> Sous-graphes :
            sous_graphe_engendre
            sous_graphe
            est_sous_graphe
            est_super_graphe
        -> Cardinaux :
            nombre_sommets                                  ()
            nombre_arcs                                     ()
            nombre_boucles                                  ()
            nombre_arcs_multiples
            nombre_aretes_multiples ? (arcs et opposés ?)
        -> Eléments :
            sommet                                          ()
            sommets                                         ()
            sommets_isoles
            arc                                             ()
            arcs                                            ()
            arcs_incidents                                  ()
            arcs_entrant                                    ()
            arcs_sortant                                    ()
            arcs_occurences
            arcs_multiples
            boucles                                         ()
            boucles_multiples
            extraire_sommets                                ()
            extraire_arcs                                   ()
        -> Tests de contenance :
            contient_arc                                    ()
            contient_arcs                                   ()
            contient_sommet                                 ()
            contient_sommets                                ()
            indice_sommet                                   ()
            indice_arc                                      ()
        -> Voisinage :
            degre
            degre_entrant
            degre_sortant
            voisins
            successeurs
            predecesseurs
        -> Suppression d'élément :
            retirer_arc
            retirer_multiarc
            retirer_arcs
            retirer_sommet
            retirer_sommets
            retirer_arcs_multiples
            retirer_boucles
            retirer_sommets_isoles
            vider_sommets
            vider_arcs
            est_simple
            simplifier
    Fonctions :
    Idées :
        _ Graphe non-orienté associé
    Remarques :
    """
    
    
    
    ## Edition de l'objet
    
    
    
    def __init__ (self) :
        """
        Construit un GrapheOriente. Celui-ci contient une liste de Sommets et une liste d'Arcs.
        """
        self.s = []
        self.a = []
    
    
    
    def __repr__ (self) :
        """
        """
        s = [som.__repr__() for som in self.s]
        a = [arc.__repr__() for arc in self.a]
        return "graphe orienté :\n" + "|-sommets : " + ", ".join(s) + "\n" + "|-arcs : " + ", ".join(a) + "\n"
    
    
    
    ## Autres
    
    
    
    ### Ajout d'élément
    
    
    
    def ajouter_sommet (self, val) :
        """
        Ajoute un Sommet dont on fourni la valeur au GrapheOriente.
        Si le Sommet est déjà présent, il n'est pas ajouté.
        """
        s = Sommet(val)
        if s not in self.s :
            self.s.append(s)
    
    
    
    def ajouter_sommets (self, *seq_vs) :
        """
        Ajoute au GrapheOriente tous les Sommets de la séquence de valeurs seq_vs.
        Les Sommets déjà présents ne sont pas ajoutés.
        """
        for v in seq_vs :
            self.ajouter_sommet(v)
    
    
    
    def ajouter_arc (self, val1, val2) :
        """
        Ajoute un Arc, dont on fournit les valeurs de l'origine et de la destination, au GrapheOriente.
        Les Arcs multiples sont autorisés.
        """
        s1 = Sommet(val1)
        s2 = Sommet(val2)
        self.a.append(Arc(s1, s2))
    
    
    
    def ajouter_arc_oppose (self, val1, val2) :
        """
        Ajoute l'Arc opposé à celui dont on fournit les valeurs de l'origine et de la destination au GrapheOriente.
        (il s'agit donc de l'arc dont on fourni d'abord la valeur de destination puis d'origine)
        """
        self.ajouter_arc(val2, val1)
    
    
    
    def ajouter_arcs (self, *seq_va) :
        """
        Ajoute au GrapheOriente tous les Arcs fournis en argument.
        Les Arcs doivent être sous la forme de couples de valeurs, correspondant aux extrémités.
        """
        for val1, val2 in seq_va :
            self.ajouter_arc(val1, val2)
    
    
    
    def ajouter_arcs_opposes (self, *seq_va) :
        """
        Ajoute au GrapheOriente tous les Arcs opposés aux Arcs fournis en argument.
        Les Arcs doivent être sous la forme de couples de valeurs, correspondant aux extrémités.
        """
        for val1, val2 in seq_va :
            self.ajouter_arc_oppose(val1, val2)
    
    
    
    ### Sous-graphes
    
    
    
    def sous_graphe_engendre (self, *seq_vals) :
        """
        Renvoie le sous-graphe orienté engendré par la séquence de sommets.
        Peut recevoir 0, 1 ou plusieurs sommet(s) mais les sommets doivent être transmis par valeur valide.
        """
        pass
    
    
    
    def sous_graphe (self, seqs = None, seqa = None) :
        """
        Renvoie le sous-graphe dont on spécifie les valeurs des sommets et des arcs à conserver.
        seqs est une séquence de valeurs de sommets valides et seqa est une séquence de couples (valeur d'origine; valeur de destination) valides.
        """
        pass
    
    
    
    def est_sous_graphe (self, graphe) :
        """
        Teste si le GrapheOriente est un sous-graphe du GrapheOriente fourni.
        """
        pass
    
    
    
    def est_sur_graphe (self, graphe) :
        """
        Teste si le GrapheOriente est un sur-graphe du GrapheOriente fourni en argument (ie: le GrapheOriente fourni en argument est un sous-graphe du GrapheOriente).
        """
        pass
    
    
    
    ### Cardinaux
    
    
    
    def nombre_sommets (self) :
        """
        Renvoie le nombre de Sommets du GrapheOriente.
        """
        return len(self.s)
    
    
    
    def nombre_arcs (self) :
        """
        Renvoie le nombre d'Arcs du GrapheOriente.
        """
        return len(self.a)
    
    
    
    def nombre_boucles (self) :
        """
        Renvoie le nombre d'Arcs du GrapheOriente qui sont des boucles.
        """
        cpt = 0
        for a in self.a :
            if a.est_boucle() :
                cpt +=1
        return cpt
    
    
    
    def nombre_arcs_multiples (self) :
        """
        Renvoie le nombre d'Arcs du GrapheOriente qui ont des Arcs parallèles.
        """
        pass
    
    
    
    def nombre_aretes_multiples (self) :
        """
        /?\ Renvoie le nombre d'Arcs du GrapheOriente dont l'Arete du Graphe associé a des Aretes paralleles. /?\
        /?\ Renvoie le nombre d'Arcs du GrapheOriente qui ont des Arcs parallèles de même sens. /?\
        ??? Intérêt ???
        """
        pass
    
    
    
    ### Elements
    
    
    
    def sommet (self, val) :
        """
        Renvoie le Sommet du GrapheOriente dont la valeur est fournie (None si aucun sommet ne correspond à la valeur).
        """
        for som in self.s :
            if som.val == val :
                return som
        return None
    
    
    
    def sommets (self) :
        """
        Renvoie la liste des Sommets du GrapheOriente.
        """
        return self.s
    
    
    
    def sommets_isoles (self) :
        """
        Renvoie la liste des Sommets isolés (de degré 0) du GrapheOriente.
        """
        pass
    
    
    
    def arc (self, orig, dest) :
        """
        Renvoie le premier Arc du GrapheOriente dont les extrémités ont les valeurs fournies (origine puis destination).
        Renvoie None si l'Arc n'a pas été trouvé.
        Lève une exception si les Sommets correspondant aux valeurs n'ont pas été trouvés.
        /!\ A finir (excep)
        """
        sorig = self.sommet(orig)
        sdest = self.sommet(dest)
        if sorig == None or sdest == None :
            raise ValueError()
        for a in self.a :
            if a.origine() == sorig and a.destination == sdest :
                return a
        return None
    
    
    
    def arcs (self) :
        """
        Renvoie la liste des Arcs du GrapheOriente.
        """
        return self.a
    
    
    
    def arcs_incidents (self, val) :
        """
        Renvoie la liste des Arcs incidents à un Sommet du GrapheOriente.
        Le Sommet doit exister et être dans le GrapheOriente.
        """
        ret = []
        s = self.sommet(val)
        if s == None :
            raise ValueError("La valeur " + str(val) + " ne correspond à aucun Sommet du Graphe.")
        for a in self.a :
            if a.a_extremite(s) :
                ret.append(a)
        return ret
    
    
    
    def arcs_entrant (self, val) :
        """
        Renvoie la liste des Arcs entrant dans un Sommet du GrapheOriente.
        Le Sommet doit exister et être dans le GrapheOriente.
        """
        ret = []
        s = self.sommet(val)
        if s == None :
            raise ValueError("La valeur " + str(val) + " ne correspond à aucun Sommet du Graphe.")
        for a in self.a :
            if a.destination() == s :
                ret.append(a)
        return ret
    
    
    
    def arcs_sortant (self, val) :
        """
        Renvoie la liste des Arcs sortant d'un Sommet du GrapheOriente.
        Le Sommet doit exister et être dans le GrapheOriente.
        """
        ret = []
        s = self.sommet(val)
        if s == None :
            raise ValueError("La valeur " + str(val) + " ne correspond à aucun Sommet du Graphe.")
        for a in self.a :
            if a.origine() == s :
                ret.append(a)
        return ret
    
    
    
    def arcs_occurences (self) :
        """
        Renvoie un dictionnaire d'occurences des Arcs.
        Pour chaque Arc, le dictionnaire associe le nombre d'Arcs (éventuellement multiples) qui relient les deux Sommets.
        """
        pass
    
    
    
    def arcs_multiples (self) :
        """
        Renvoie un dictionnaire d'occurences des Arcs multiples.
        Pour chaque Arc, le dictionnaire associe le nombre d'Arcs multiples qui relient les deux Sommets.
        """
        pass
    
    
    
    def boucles (self) :
        """
        Renvoie la liste des Arcs qui sont des boucles.
        """
        ret = []
        for a in self.a :
            if a.est_boucle() :
                ret.append(a)
        return ret
    
    
    
    def boucles_multiples (self) :
        """
        """
        pass
    
    
    
    def extraire_sommets (self, *seq_num) :
        """
        Renvoie la liste des Sommets du GrapheOriente dont on a fournit les indices en argument.
        """
        ret = []
        for i in seq_num :
            if type(i) != int :
                raise TypeError(str(i) + " de type " + str(type(i)) + " n'est pas un " + str(int) + ".")
            ret.append(self.s[i])
        return ret
    
    
    
    def extraire_arcs (self, *seq_num) :
        """
        Renvoie la liste des Arcs du GrapheOriente dont on a fournit les indices en arguments.
        """
        ret = []
        for i in seq_num :
            if type(i) != int :
                raise TypeError(str(i) + " de type " + str(type(i)) + " n'est pas un " + str(int) + ".")
            ret.append(self.a[i])
        return ret
    
    
    
    ### Tests de contenance
    
    
    
    def contient_sommet (self, val) :
        """
        Teste si une valeur est un sommet qui apppartient au GrapheOriente.
        """
        s = Sommet(val)
        return s in self.sommets()
    
    
    
    def contient_sommets (self, *seq_s) :
        """
        Teste si tous les Sommets d'une séquence appartienne au GrapheOriente.
        """
        boo = True
        for s in seq_s :
            boo = boo and self.contient_sommet(s)
        return boo
    
    
    
    def contient_arc (self, val1, val2) :
        """
        Teste si deux valeurs données sont des extrémités d'un Arc qui appartient au GrapheOriente.
        Les valeurs doivent être des Sommets valides.
        """
        if not self.contient_sommet(val1) :
            raise ValueError("La valeur " + str(val1) + " ne correspond à aucun Sommet du Graphe.")
        if not self.contient_sommet(val2) :
            raise ValueError("La valeur " + str(val2) + " ne correspond à aucun Sommet du Graphe.")
        s1 = self.sommet(val1)
        s2 = self.sommet(val2)
        a = Arc(s1, s2)
        return a in self.arcs()
    
    
    
    def contient_arcs (self, *seq_cpl) :
        """
        Test si tous les Arcs d'une séquence appartiennent au GrapheOriente.
        Les Arcs doivent être passés sous forme de couples de valeurs correspondant aux valeurs des extrémités.
        """
        boo = True
        for vals in seq_cpl :
            boo = boo and self.contient_arc(*vals)
        return boo
    
    
    
    def indice_sommet (self, val) :
        """
        Renvoie l'indice d'un Sommet du GrapheOriente.
        Renvoie -1 si la valeur ne correspond à aucun Sommet.
        """
        s = Sommet(val)
        for i in range(len(self.sommets())) :
            if self.sommets()[i] == s :
                return i
        return -1
    
    
    
    def indice_arc (self, val1, val2) :
        """
        Renvoie l'indice d'un Arc du GrapheOriente (du premier Arc parallèle trouvé).
        Renvoie -1 si les valeurs ne corespondent à aucun Arc.
        Lève une exception si les valeurs ne correspondent à aucun Sommet. 
        """
        s1 = self.sommet(val1)
        s2 = self.sommet(val2)
        if s1 == None :
            raise ValueError("La valeur " + str(val1) + " ne correspond à aucun Sommet du GrapheOriente.")
        if s2 == None :
            raise ValueError("La valeur " + str(val2) + " ne correspond à aucun Sommet du GrapheOriente.")
        a = Arc(s1, s2)
        for i in range(len(self.a)) :
            if self.a[i] == a :
                return i
        return -1
    
    
    
    ### Voisinage
    
    
    
    def degre_entrant (self, val_s) :
        """
        """
        pass
    
    
    
    def degre_sortant (self, val_s) :
        """
        """
        pass
    
    
    
    def degre (self, val_s) :
        """
        """
        pass
    
    
    
    def predecesseurs (self, val_s) :
        """
        """
        pass
    
    
    
    def successeurs (self, val_s) :
        """
        """
        pass
    
    
    
    def voisins (self, val_s) :
        """
        """
        pass
    
    
    
    ### Suppression d'élément
    
    
    
    def retirer_sommet (self, val_s) :
        """
        """
        pass
    
    
    
    def retirer_sommets (self, seq_s) :
        """
        """
        pass
    
    
    
    def retirer_arc (self, val_a) :
        """
        """
        pass
    
    
    
    def retirer_arcs (self, seq_a) :
        """
        """
        pass
    
    
    
    def retirer_multiarc (self, val_a) :
        """
        """
        pass
    
    
    
    def retirer_arcs_multiples (self) :
        """
        """
        pass
    
    
    
    def retirer_boucles (self) :
        """
        """
        pass
    
    
    
    def retirer_sommets_isoles (self) :
        """
        """
        pass
    
    
    
    def vider_sommets (self) :
        """
        """
        pass
    
    
    
    def vider_arcs (self) :
        """
        """
        pass
    
    
    
    def est_simple (self) :
        """
        """
        pass
    
    
    
    def simplifier (self) :
        """
        """
        pass




g=Graphe()
g.ajouter_sommets(0,1,2,3,4,5,7,9,10)
g.ajouter_aretes((0,1),(1,2),(2,3),(3,4),(0,0),(2,2),(2,3),(3,4),(4,3),(2,2))

h = g.sous_graphe([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (0, 0), (2, 2)])

go = GrapheOriente()
go.ajouter_sommets(0,1,2,3,4,5,7,9,10)