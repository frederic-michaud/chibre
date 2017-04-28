#coding: utf-8
import unittest
import bin.base_jeu as base_jeu

class BaseJeuTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'base jeu'."""

    def setUp(self):
        """Initialisation des tests."""
        self.ma_carte = base_jeu.carte(ide=5)
		

    def test_choice(self):
        """test le foncionnement de la fonction pour définir une carte a partir d'un numéro"""
        self.assertEqual("carreau",self.ma_carte.couleur.nom)
        self.assertEqual("10",self.ma_carte.rang.nom)

   
