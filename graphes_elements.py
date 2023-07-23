"""
Créé le : Ve 17/02/2023 à 02h28
Auteur : Nate
graphes_elements.py
"""

"""
Classes à gérer :
_ Sommet (valeur)
_ Arete (sommet1, sommet2)
_ Arc (sommet1, sommet2)
_ AretePonderee (sommet1, sommet2, poids) ? ou poids = dict{arete : int} ?
_ ArcPondere (sommet1, sommet2, poids) ? ou poids = dict{arc : int} ?
... ? (sommet_pondere ?, chemin ?, flot ?)
"""

class Sommet :
    
    """
    Cette classe définit un sommet d'un graphe.
    On peut attribuer une valeur à un sommet, quelle qu'elle soit (usuellement un compteur entier positif ou une lettre de l'alphabet).
    
    Méthodes :
        ¤ Edition de l'objet :
            __init__                                        (ok) pas 2 somm id ?
            __repr__                                        (ok) = str : plus simple
            __str__                                         (ok)
        ¤ Méthodes de comparaison :
            (__eq__)                                        (ok : non surchargé)
            __gt__                                          (ok)
            __ge__                                          (ok)
        ¤ Autres :
            changer_valeur (__call__ ?) ? pas pour l'instant
    Fonctions ?
    
    idée :
    _ champ de classe compteur de sommets ?
    _ remettre __eq__ et def __hash__ ?
    _ méthode valeur
    
    Remarque :
    _ peu d'exceptions sont levées pour la comparaison pour éviter un filtrage excessif (par ex 1 > 0.5 permis)
    _ le champ val reste public (il n'y a de toutes façons pas de privé strict !) donc attention au hash : si val change, le hash ne change pas. Et deux sommets avec les mêmes valeurs auront possiblement des hashs différents. Deux sommets restent différents tant qu'il ne s'agit pas du même objet. Il faut voir le champ val comme un poids ou une étiquette qui n'affecte en rien l'identité du sommet.
    _ Il faut bien faire attention à éviter de manipuler des copies de sommet pour ne pas déteriorer l'égalité (identité).
    """
    
    
    
    ## Edition de l'objet
    
    
    
    def __init__ (self, val) :
        """
        Construit un Sommet associé à la valeur fournie.
        """
        self.val = val
    
    
    
    def __repr__ (self) :
        """
        Affiche un Sommet dans la console de code.
        """
        return self.__str__()#"Sommet de valeur " + str(self.val)
    
    
    
    def __str__ (self) :
        """
        Affiche un Sommet.
        """
        return "S(" + str(self.val) + ")"
    
    
    
    ## Méthodes de comparaison
    
    
    
    def __eq__ (self, autre) :
        """pas de surcharge permet d'avoir la hashabilité automatique.
        Teste l'égalité de Sommets : self == autre
        """
        return type(autre) == Sommet and self.val == autre.val
    
    
    
    def __hash__ (self) :
        """
        Définit le hashage d'un Sommet.
        """
        return hash(self.val)
    
    
    
    def __gt__ (self, autre) :
        """
        Teste la supériorité stricte d'un Sommet par rapport à un autre.
        """
        if type(autre) != Sommet :
            raise TypeError("Comparaison stricte d'un Sommet avec un type " + str(type(autre)) + ".")
        return self.val > autre.val
    
    
    
    def __ge__ (self, autre) :
        """
        Teste la supériorité large d'un Sommet par rapport à un autre.
        """
        if type(autre) != Sommet :
            raise TypeError("Comparaison large d'un Sommet avec un type " + str(type(autre)) + ".")
        return self.val >= autre.val
    
    
    
    ## Méthodes de classe
    
    
    
    def test_type (obj) :
        """
        Test si l'objet est un sommet et lève une exception sinon.
        """
        if type(obj) != Sommet :
            raise TypeError(str(obj) + " n'est pas de type " + str(Sommet) + " (type : " + str(type(obj)) + ").")





class Arete :
    
    """
    Cette classe définit une arête d'un graphe.
    Une arête est une paire de sommets. Une arête étant non-orientée, l'ordre n'importe pas.
    
    Méthodes :
        ¤ Edition de l'objet :
            __init__                                        (ok)
            __repr__                                        (ok)
            (__str__ ?)
        ¤ Méthodes de conteneur :
            (__getitem__ ?)
            __len__                                         (ok)
        ¤ Opérateurs mathématiques (plus tard : chemin...)
        ¤ Méthodes de comparaison
            __eq__                                          (ok) test de parallélisme
            __hash__                                        (ok)
            __gt__                                          (ok)
            __ge__                                          (ok)
        ¤ Autres :
            valeur                                          (ok)
            est_boucle                                      (ok)
            extremites                                      (ok) -> liste des extr.
            extremites_triees                               (ok) -> liste des extr. triées (tri sur sommets) pour faire des chem ???
            a_extremite                                     (ok) -> test si un somm est dedans
            autre_extremite                                 (ok) -> donne l'autre somm
            est_parallele                                   (ok)
            sont_paralleles                                 (ok) -> seq d'arr
        ¤ Méthode de clase :
            test_type                                       (ok)
    Fonctions :
    Idées :
    _ utilisation de frozenset (non-muttable) ?
    _ init (s2=s1)
    Remarques :
    _ utilisation de set ? oui à priori
    _ indexation impossible mais parcours possible sur les set
    """
    
    
    
    ## Edition de l'objet
    
    
    
    def __init__ (self, extr1, extr2) :
        """
        Construit une Arete à partir des deux Sommets fournits.
        Fournir deux fois le même Sommet dans le cas d'une boucle.
        Les Sommets étant hashable, l'utilisation de set est possible.
        """
        if type(extr1) != Sommet :
            raise TypeError("Le sommet " + str(extr1) + " de l'arrête n'est pas de type Sommet (type : " + str(type(extr1)) + ").")
        if type(extr2) != Sommet :
            raise TypeError("Le sommet " + str(extr2) + " de l'arrête n'est pas de type Sommet (type : " + str(type(extr2)) + ").")
        self.extr = set()
        self.extr.add(extr1)
        self.extr.add(extr2)
    
    
    
    def __repr__ (self) :
        """
        Affiche l'Arete (dans la console?).
        """
        return self.extr.__repr__()
    
    
    
    ## Méthodes de conteneur
    
    
    
    def __len__ (self) :
        """
        Renvoie le nombre d'extrémités distinctes de l'Arete.
        """
        return len(self.extr)
    
    
    
    ## Méthodes de comparaison
    
    
    
    def __eq__ (self, obj) :
        """
        Teste si l'Arete a les mêmes extrémités qu'une autre. Il s'agit donc en toute rigueur d'un test de parallélisme.
        Pour tester l'égalité au sens strict, on utilisera le mot-clé "is" car il s'agit alors de l'identité.
        """
        return self.est_parallele(obj)
    
    
    
    def __hash__ (self) :
        """
        Définit le hashage d'une Arete.
        """
        return hash(tuple(self.extremites_triees()))
    
    
    
    def __gt__ (self, obj) :
        """
        Teste si l'Arete est strictement supérieure à une autre.
        Utilise l'ordre "lexicographique" sur les Sommets.
        """
        if type(obj) != Arete :
            raise TypeError(str(type(self)) + " n'est pas comparable à " + str(type(obj)) + ".")
        li_sel = self.extremites_triees()
        li_obj = obj.extremites_triees()
        if li_sel[0] == li_obj[0] :
            return li_sel[-1] > li_obj[-1]
        return li_sel[0] > li_obj[0]
    
    
    
    def __ge__ (self, obj) :
        """
        Teste si l'Arete est supérieure ou égale à une autre.
        Utilise l'ordre "lexicographique" sur les Sommets.
        """
        if type(obj) != Arete :
            raise TypeError(str(type(self)) + " n'est pas comparable à " + str(type(obj)) + ".")
        li_sel = self.extremites_triees()
        li_obj = obj.extremites_triees()
        if li_sel[0] == li_obj[0] :
            return li_sel[-1] >= li_obj[-1]
        return li_sel[0] > li_obj[0]
    
    
    
    ## Autres
    
    
    
    def valeur (self) :
        """
        Renvoie une extrémité de l'Arete de manière arbitraire.
        """
        cop = self.extr.copy()
        return cop.pop().val
    
    
    
    def est_boucle (self) :
        """
        Teste si l'Arete est une boucle (True) ou non (False).
        """
        return len(self) == 1
    
    
    
    def extremites (self) :
        """
        Renvoie la liste des extremités de l'Arete.
        L'ordre n'est pas considéré dans cette méthode : l'ordre dans lequel les Sommets sont listés n'est donc pas prévisible.
        """
        return list(self.extr)
    
    
    
    def extremites_triees (self) :
        """
        Renvoie la liste des extremités de l'Arete triée. Le tri utilise l'ordre définit sur les Sommets.
        """
        l = self.extremites()
        if len(l) == 2 and l[0] > l[1] :
            l.reverse()
        return l
    
    
    
    def a_extremite (self, s) :
        """
        Teste si un sommet est une extrémité de l'Arete (True) ou non (False).
        """
        if type(s) != Sommet :
            raise TypeError("Le type de " + str(s) + " est " +str(type(s)) + ".")
        return s in self.extr
    
    
    
    def autre_extremite (self, s) :
        """
        Prend un Sommet extrémité de l'Arete en argument et renvoie l'autre extrémité.
        Si l'Arete est une boucle, renvoie le Sommet fournit.
        """
        if len(self) == 1 and self.a_extremite(s) :
            return s
        cop = self.extr.copy()
        cop.remove(s)
        return cop.pop()
    
    
    
    def est_parallele (self, obj) :
        """
        Test si l'Arete est parallèle à une autre (True) ou non (False).
        Deux Aretes parallèles sont des Aretes qui ont les mêmes extrémités.
        """
        if type(obj) != Arete :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        if self.extr == obj.extr :
            return True
        return False
    
    
    
    def sont_paralleles (self, iterable) :
        """
        Teste si toutes les Aretes fournies sont parallèles entre elles.
        """
        para = True
        for arr in iterable :
            if not self.est_parallele(arr) :
                para = False
        return para
    
    
    
    ## Méthodes de classe
    
    
    
    def test_type (obj) :
        """
        Test si l'objet est une Arete et lève une exception sinon.
        """
        if type(obj) != Arete :
            raise TypeError(str(obj) + " n'est pas de type " + str(Arete) + " (type : " + str(type(obj)) + ").")





class Arc :
    
    """
    Cette classe définit un arc d'un graphe orienté.
    Un arc est un couple de sommets. Un arc étant orienté, il est ordonné.
    
    Méthodes :
        ¤ Edition de l'objet :
            __init__                                        (ok)
            __repr__                                        (ok)
        ¤ Méthodes de conteneur :
            (__getitem__ ?)
            __len__                                         (ok)
        ¤ Opérateurs mathématiques (plus tard : chemin...)
        ¤ Méthodes de comparaison :
            __eq__                                          (ok)
            __hash__                                        (ok)
            __gt__                                          (ok)
            __ge__                                          (ok)
        ¤ Autres :
            valeur ?                                        ----
            est_boucle                                      (ok)
            extremites                                      (ok)
            a_extremite                                     (ok)
            autre_extremite ?                               ----
            origine                                         (ok)
            destination                                     (ok)
            est_parallele                                   (ok)
            sont_paralleles                                 (ok)
            est_oppose                                      (ok)
            arc_retour                                      (ok)
        ¤ Méthode de classe :
            test_type                                       (ok)
    Fonctions :
    Idées :
    Remarques :
    """
    
    
    
    ## Edition de l'objet
    
    
    
    def __init__ (self, extr1, extr2) :
        """
        Construit un Arc à partir de deux Sommets fournis.
        """
        if type(extr1) != Sommet :
            raise TypeError("Le sommet " + str(extr1) + " de l'arrête n'est pas de type Sommet (type : " + str(type(extr1)) + ").")
        if type(extr2) != Sommet :
            raise TypeError("Le sommet " + str(extr2) + " de l'arrête n'est pas de type Sommet (type : " + str(type(extr2)) + ").")
        self.extr = (extr1, extr2)
    
    
    
    def __repr__ (self) :
        """
        Affiche un Arc.
        """
        return self.extr.__repr__()
    
    
    
    ## Méthodes de conteneur
    
    
    
    def __len__ (self) :
        """
        Renvoie le nombre d'extrémités distinctes de l'Arc.
        """
        if self.extr[0] == self.extr[1] :
            return 1
        else :
            return 2
    
    
    
    ## Méthodes de comparaison
    
    
    
    def __eq__ (self, obj) :
        """
        Teste l'égalité de deux Arcs. Il s'agit de tester les extrémités (c'est donc plus un test de parallélisme).
        Pour tester l'égalité au sens strict, il faudra utiliser le mot-clé "is".
        """
        return self.est_parallele(obj)
    
    
    
    def __hash__ (self) :
        """
        Définit le hashage d'un Arc.
        """
        return hash(self.extr)
    
    
    
    def __gt__ (self, obj) :
        """
        Teste si l'Arc est strictement supérieur à un autre.
        Utilise l'odre lexicographique sur les Sommets.
        """
        if type(obj) != Arc :
            raise TypeError(str(type(obj)) + " n'est pas comparable avec " + str(type(self)) + ".")
        if self.extr[0] == obj.extr[0] :
            return self.extr[1] > obj.extr[1]
        return self.extr[0] > obj.extr[0]
    
    
    
    def __ge__ (self, obj) :
        """
        Teste si l'Arc est supérieur ou égal à un autre.
        Utilise l'ordre lexicographique sur les Sommets.
        """
        if type(obj) != Arc :
            raise TypeError(str(type(obj)) + "n'est pas comparable avec " + str(type(self)) + ".")
        if self.extr[0] == obj.extr[0] :
            return self.extr[1] >= obj.extr[1]
        return self.extr[0] > obj.extr[0]
    
    
    
    ## Autres
    
    
    
    def est_boucle (self) :
        """
        Teste si l'Arc est une boucle (True) ou non (False).
        """
        return self.extr[0] == self.extr[1]
    
    
    
    def extremites (self) :
        """
        Renvoie le tuple des extrémités de l'Arc.
        """
        return self.extr
    
    
    
    def a_extremite (self, s) :
        """
        Teste si un Sommet est une extrémité de l'Arc ou non.
        """
        if type(s) != Sommet :
            raise TypeError("Le type de " + str(s) + " est " + str(type(s)) + ".")
        return s in self.extr
    
    
    
    def origine (self) :
        """
        Renvoie l'origine de l'Arc.
        """
        return self.extr[0]
    
    
    
    def destination (self) :
        """
        Renvoie la destination de l'Arc.
        """
        return self.extr[1]
    
    
    
    def est_parallele (self, obj) :
        """
        Teste si deux Arcs sont parallèles (ont les mêmes extrémités).
        """
        if type(obj) != Arc :
            raise TypeError("L'objet " + str(obj) + " n'est pas de type " + str(Arc) + ".")
        return self.extr == obj.extr
    
    
    
    def sont_paralleles (self, iterable) :
        """
        Teste si une liste d'arcs sont parallèles entre eux.
        """
        para = True
        for a in iterable :
            para = para and self.est_parallele(a)
        return para
    
    
    
    def est_oppose (self, obj) :
        """
        Teste si un objet est l'Arc opposé.
        """
        if type(obj) != Arc :
            raise TypeError(str(obj) + " n'est pas du type " + str(Arc) + " (type : " + str(type(obj)) + ").")
        return self.origine() == obj.destination() and self.destination() == obj.origine()
    
    
    
    def arc_retour (self) :
        """
        Renvoie l'Arc retour (dont l'origine et la destination sont inversés).
        """
        return Arc(self.destination(), self.origine())
    
    
    
    ## Méthode de classe
    
    
    
    def test_type (obj) :
        """
        Teste si l'objet est un Arc et lève une exception sinon.
        """
        if type(obj) != Arc :
            raise TypeError(str(obj) + " n'est pas du type " + str(Arc) + " (type : " + str(type(obj)) + ").")





class AretePondere :
    
    """
    Cette classe définit une arête pondérée d'un graphe pondéré.
    Une arête pondérée est un objet contenant une arête classique et un poids.
    
    Méthodes :
        ¤ Edition de l'objet :
            __init__                                        (ok)
            __repr__                                        (ok)
        ¤ Méthode de conteneur :
            __len__                                         (ok)
        ¤ Opérateurs mathématiques (?)
        ¤ Méthodes de comparaisons :
            __eq__                                          (ok) -- égalité des Aretes ET des poids
            __hash__                                        (ok)
            __ge__                                          (ok) -- ordre lexico des Aretes
            __gt__                                          (ok) -- ordre lexico des Aretes
            eq_poids                                        (ok)
            ne_poids                                        (ok)
            ge_poids                                        (ok)
            gt_poids                                        (ok)
            le_poids                                        (ok)
            lt_poids                                        (ok)
        ¤ Autres :
            valeur                                          (ok)
            est_boucle                                      (ok)
            extremites                                      (ok)
            extremites_triees                               (ok)
            a_exremite                                      (ok)
            autre_extremite                                 (ok)
            est_parallele                                   (ok)
            sont_paralleles                                 (ok)
            poids                                           (ok)
            arete                                           (ok)
        ¤ Méthode de classe :
            test_type                                       (ok)
    Fonctions :
    Idées :
        _ choisir la comparaison adéquate
    Remarques :
    """
    
    ## Edition de l'objet
    
    
    
    def  __init__ (self, s1, s2, p) :
        """
        Construit une AretePondere à partir de deux sommets et d'un poids fournis.
        """
        self.a = Arete(s1, s2)
        self.p = p
    
    
    
    def __repr__ (self) :
        """
        Affiche une AretePondere.
        """
        return str((self.a, self.p))
    
    
    
    ## Méthode de conteneur
    
    
    
    def __len__ (self) :
        """
        Renvoie la longueur de l'AretePondere (en tant qu'Arete).
        """
        return len(self.a)
    
    
    
    ## Méthodes de comparaison
    
    
    
    def __eq__ (self, obj) :
        """
        Teste l'égalité de deux AretePonderes (parallélisme des Aretes et égalité des poids).
        """
        if type(obj) != AretePondere :
            return False
        return self.a == obj.a and self.p == obj.p
    
    
    
    def __hash__ (self) :
        """
        Définit le hashage d'une AretePondere.
        """
        return hash((hash(self.a), self.p))
    
    
    
    def __ge__ (self, obj) :
        """
        Teste si l'AretePondere est supérieure ou égale à une autre.
        Utilise l'ordre lexicographique sur les Aretes.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        return self.a >= obj.a
    
    
    
    def __gt__ (self, obj) :
        """
        Teste si l'AretePondere est strictement supérieure à une autre.
        Utilise l'ordre lexicographique sur les Aretes.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        return self.a > obj.a
    
    
    
    def eq_poids (self, obj) :
        """
        Teste l'égalité des poids de deux AretePonderes.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        return self.poids() == obj.poids()
    
    
    
    def ne_poids (self, obj) :
        """
        Teste la différence des poids de deux AretePonderes.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        return self.poids() != obj.poids()
    
    
    
    def ge_poids (self, obj) :
        """
        Teste la supériorité large des poids de deux AretePonderes.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        return self.poids() >= obj.poids()
    
    
    
    def gt_poids (self, obj) :
        """
        Teste la supériorité stricte des poids de deux AretePonderes.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        return self.poids() > obj.poids()
    
    
    
    def le_poids (self, obj) :
        """
        Teste l'infériorité large des poids de deux AretePonderes.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        return self.poids() <= obj.poids()
    
    
    
    def lt_poids (self, obj) :
        """
        Teste l'infériorité stricte des poids de deux AretePonderes.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        return self.poids() < obj.poids()
    
    
    
    ## Autres
    
    
    
    def valeur (self) :
        """
        Renvoie une extrémité de l'AretePondere de manière arbitraire.
        """
        return self.a.valeur()
    
    
    
    def est_boucle (self) :
        """
        Teste si l'AretePondere est une boucle (True) ou non (False).
        """
        return self.a.est_boucle()
    
    
    
    def extremites (self) :
        """
        Renvoie la liste des extremités de l'AretePondere.
        L'ordre n'est pas considéré dans cette méthode : l'ordre dans lequel les Sommets sont listés n'est donc pas prévisible.
        """
        return self.a.extremites()
    
    
    
    def extremites_triees (self) :
        """
        Renvoie la liste des extremités de l'AretePondere triée. Le tri utilise l'ordre définit sur les Sommets.
        """
        return self.a.extremites_triees()



    def a_extremite (self, s) :
        """
        Teste si un sommet est une extrémité de l'AretePondere (True) ou non (False).
        """
        return self.a.a_extremite(s)
    
    
    
    def autre_extremite (self, s) :
        """
        Prend un Sommet extrémité de l'Arete en argument et renvoie l'autre extrémité.
        Si l'Arete est une boucle, renvoie le Sommet fournit.
        """
        return self.a.autre_extremite(s)
    
    
    
    def est_parallele (self, obj) :
        """
        Test si l'AretePondere est parallèle à une autre (True) ou non (False).
        Deux AretePonderes parallèles sont des AretePonderes qui ont les mêmes extrémités.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(type(self)) + " n'est pas comparable avec " + str(type(obj)) + ".")
        return self.a.est_parallele(obj.a)
    
    
    
    def sont_paralleles (self, iterable) :
        """
        Teste si toutes les AretePonderes fournies sont parallèles entre elles.
        """
        para = True
        for arp in iterable :
            if not self.est_parallele(arp) :
                para = False
        return para
    
    
    
    def poids (self) :
        """
        Renvoie le poids de l'AretePondere.
        """
        return self.p
    
    
    
    def arete (self) :
        """
        Renvoie l'Arete de l'AretePondere.
        """
        return self.a
    
    
    
    ## Méthode de classe
    
    
    
    def test_type (obj) :
        """
        Teste si l'objet est une AretePondere et lève une exception sinon.
        """
        if type(obj) != AretePondere :
            raise TypeError(str(obj) + " n'est pas du type " + str(AretePondere) + " (type : " + str(type(obj)) + ").")





class ArcPondere :
    
    """
    Cette classe définit un arc pondéré d'un graphe orienté pondéré.
    Un arc pondéré est un objet contenant un arc classique et un poids.
    
    Méthodes :
        ¤ Edition de l'objet :
            __init__
            __repr__
        ¤ Méthode de conteneur :
            __len__
        ¤ Opérateurs mathématiques (?)
        ¤ Méthodes de comparaison :
            __eq__
            __hash__
            __ge__
            __gt__
            eq_poids
            ne_poids
            ge_poids
            gt_poids
            le_poids
            lt_poids
        ¤ Autres :
            est_boucle
            extremites
            a_extremite
            (autre_extremite ?)
            est_parallele
            sont_paralleles
            est_oppose
            arc_retour
            poids
            arc
        ¤ Méthode de classe :
            test_type
    Fonctions :
    Idées :
    Remarques :
    """



s1 = Sommet(1)
s2 = Sommet(2)
s3 = Sommet(3)
a1 = Arc(s1, s2)
a2 = Arc(s2, s3)
a3 = Arc(s3, s2)
a4 = Arc(s2, s1)
a5 = Arc(s1, s2)
a6 = Arc(s1, s2)
a=AretePondere(s1, s2, 5)
b=AretePondere(s2, s3, 3)
c=AretePondere(s1, s1, 0)
d=AretePondere(s2, s1, -1)
e=AretePondere(s3, s2, 5)

# comparaisons
a=AretePondere(s1, s2, 5)
b=AretePondere(s2, s1, -1)
c=AretePondere(s1, s3, 5)
d=AretePondere(s1, s2, 10)
e=AretePondere(s3, s2, 5)
# a = b = d < c < e
A=a.a
B=b.a
C=c.a
D=d.a

