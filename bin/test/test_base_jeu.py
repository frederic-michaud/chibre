#coding: utf-8
import unittest
import numpy as np
import bin.base_jeu as base_jeu

class BaseJeuTest(unittest.TestCase):

	"""Test case utilisé pour tester les fonctions du module 'base jeu'."""

	def setUp(self):
		"""Initialisation des tests."""
		pass
		

	def test_choice(self):
		"""test le foncionnement de la fonction pour définir une carte a partir d'un numéro"""
		self.ma_carte = base_jeu.carte(Ide=5)
		self.assertEqual("carreau",self.ma_carte.couleur.nom)
		self.assertEqual("10",self.ma_carte.rang.nom)
	
	def test_build_carde(self):
		"""test la fonction qui retrouve le ide en fonction de son rang et de sa couleur"""
		self.ma_carte2 = base_jeu.carte(Rang="10", Couleur="carreau")
		self.ma_carte3 = base_jeu.carte(Rang="valet", Couleur="trefle")
		self.assertEqual(5,self.ma_carte2.ide)
		self.assertEqual(33,self.ma_carte3.ide)

	def test_init_rang(self):
		"""test le constructeur de rang"""
		self.mon_rang1 = base_jeu.rang(Nom="10")
		self.mon_rang2 = base_jeu.rang(Ide=4)
		self.assertEqual(5,self.mon_rang1.ide)
		self.assertEqual("9",self.mon_rang2.nom)   

	def test_init_hand(self):
		"""test le constructeur d'une main (hand) à l'aide de 9 carte"""
		ma_hand = base_jeu.hand(range(3,13))
		ma_carte = base_jeu.carte(Ide = 5)
		self.assertIn(ma_carte,ma_hand.cartes)

	def test_init_jeu(self):
		"""test le constructeur de la classe jeu"""
		mon_jeu = base_jeu.jeu()
		ma_carte = base_jeu.carte(Ide = 33)
		cartes = np.array([mon_jeu.hands[i].cartes for i in range(len(mon_jeu.hands))]).flatten(36)
		self.assertIn(ma_carte, cartes)
		
	def test_compatibilise_jeu(self):
		"""test sur différent scénario la méthode pour compter les points"""
		mon_jeu = base_jeu.jeu(Atout = 1)
		mes_cartes = [base_jeu.carte(Ide = i) for i in range(3,7)]
		mon_jeu.compatibilise(1,mes_cartes)
		self.assertEqual(mon_jeu.equipe_1_points,44)
		
		mon_jeu = base_jeu.jeu(Atout = 2)
		mes_cartes = [base_jeu.carte(Ide = i) for i in range(3,7)]
		mon_jeu.compatibilise(1,mes_cartes)
		self.assertEqual(mon_jeu.equipe_1_points,12)
		
		mon_jeu = base_jeu.jeu(Atout = 2)
		mes_cartes = [base_jeu.carte(Ide = i) for i in [13,14,19,20]]
		mon_jeu.compatibilise(2,mes_cartes)
		self.assertEqual(mon_jeu.equipe_2_points,24)
		
		mon_jeu = base_jeu.jeu(Atout = 2)
		mes_cartes = [base_jeu.carte(Ide = i) for i in [2,4,6,8]]
		mon_jeu.compatibilise(1,mes_cartes)
		self.assertEqual(mon_jeu.equipe_2_points,0)
		

