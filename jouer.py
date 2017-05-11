# coding: utf8

import bin.base_jeu as base_jeu
import bin.interface as interface

joueur1 = interface.joueur_physique(Ide = 1)
joueur2 = base_jeu.joueur(Ide = 2)
joueur3 = base_jeu.joueur(Ide = 3)
joueur4 = base_jeu.joueur(Ide = 4)
ma_partie = base_jeu.partie([joueur1, joueur2, joueur3, joueur4])
res = ma_partie.joue()


