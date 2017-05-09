#coding: utf-8
import unittest
import numpy as np
import bin.base_jeu as base_jeu

class BaseJeuTest(unittest.TestCase):

	"""Test case utilisé pour tester les fonctions du module 'base partie'."""

	def setUp(self):
		"""Initialisation des tests."""
		self.carreau = base_jeu.couleur(Nom = "carreau")
		self.coeur = base_jeu.couleur(Nom = "coeur")
		self.pique = base_jeu.couleur(Nom = "pique")
		self.trefle = base_jeu.couleur(Nom = "trefle")
		self.ma_partie = base_jeu.partie()
		self.ma_partie.joueur_atout = self.ma_partie.get_joueur(2)
		self.ma_donne = base_jeu.donne(self.ma_partie)
		self.ma_donne.distribue()
		self.ma_donne.atout = self.ma_donne.partie.joueur_atout.decide_atout()
		

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

	def test_init_partie(self):
		"""test le constructeur de la classe partie"""

		ma_carte = base_jeu.carte(Ide = 33)
		cartes = np.array([self.ma_partie.get_joueur(i).hand.cartes for i in range(1,5)]).flatten(36)
		self.assertIn(ma_carte, cartes)
		
	def test_compatibilise_partie(self):
		"""test sur différent scénario la méthode pour compter les points"""
		mes_cartes = [base_jeu.carte(Ide = i) for i in range(3,7)]
		self.ma_donne.atout = self.carreau
		self.ma_donne.compatibilise(self.ma_partie.get_equipe(1),mes_cartes)
		self.assertEqual(self.ma_partie.get_equipe(1).points,44)
		
		self.ma_donne.atout = base_jeu.couleur(Ide = 2)
 		mes_cartes = [base_jeu.carte(Ide = i) for i in range(3,7)]
		self.ma_donne.compatibilise(self.ma_partie.get_equipe(1),mes_cartes)
		self.assertEqual(self.ma_partie.get_equipe(1).points,12 + 44)
		

		mes_cartes = [base_jeu.carte(Ide = i) for i in [13,14,19,20]]
		self.ma_donne.compatibilise(self.ma_partie.get_equipe(2),mes_cartes)

		self.assertEqual(self.ma_partie.get_equipe(2).points,24)
		
		mes_cartes = [base_jeu.carte(Ide = i) for i in [2,4,6,8]]
		self.ma_donne.compatibilise(self.ma_partie.get_equipe(1),mes_cartes)
		self.assertEqual(self.ma_partie.get_equipe(2).points,0 + 24)
		
	def test_joueur(self):
		"""test la construction d'un joueur """
		my_hand = base_jeu.hand([1,2,3,4]) 
		mon_joueur = base_jeu.joueur(Hand = my_hand)
		ma_carte = base_jeu.carte(Ide = 2)
		self.assertIn(ma_carte, mon_joueur.hand.cartes)


	def test_joue(self):
		"""test la fonction joue d'un joueur ainsi que sa fonction jouer"""
		my_hand = base_jeu.hand(perm =[1,2,3])
		mon_joueur = base_jeu.joueur(Hand = my_hand)
		cartes_jouees = [base_jeu.carte(Ide = i) for i in [1,2]]
		mon_joueur.joue(self.ma_donne,cartes_jouees)
		self.assertNotIn(base_jeu.carte(Ide = 3),mon_joueur.hand.cartes)	
		
	def test_force_carte(self):
		""" test la force de certaines carte dans différent scénario"""
		six = base_jeu.carte(Rang = "6",Couleur = "carreau")
		neuf = base_jeu.carte(Rang = "9",Couleur = "carreau")
		dix = base_jeu.carte(Rang = "10",Couleur = "carreau")
		valet = base_jeu.carte(Rang = "valet",Couleur = "carreau")
		roi = base_jeu.carte(Rang = "roi",Couleur = "carreau")	

		#couleur atout, couleur plie
		self.assertEqual(six.valeur_force(self.carreau,self.coeur),10)
		self.assertEqual(neuf.valeur_force(self.carreau,self.coeur),19)
		self.assertEqual(dix.valeur_force(self.pique,self.coeur),0)
		self.assertEqual(valet.valeur_force(self.coeur,self.carreau),6)
		self.assertEqual(valet.valeur_force(self.carreau,self.coeur),20)
		self.assertEqual(roi.valeur_force(self.coeur,self.coeur),0)
		
	def test_joueur_gagnant(self):
		""" test quel joueur gagne pour une plie donnée"""
		p1 = [1,5,7,14]
		plie1 = [base_jeu.carte(Ide = i) for i in p1]
		j1 = self.ma_donne.determine_gagnant(plie1)
		self.assertEqual(j1.ide,3)
		
		p2 = [10,11,15,22]
		plie2 = [base_jeu.carte(Ide = i) for i in p2]
		ma_donne = base_jeu.donne(self.ma_partie)
		j2 = self.ma_donne.determine_gagnant(plie2)
		self.assertEqual(j2.ide,3)

	def test_joue_plie(self):
		"""test la fonction qui joue une seule plie"""
		mes_cartes_avant1 = list(self.ma_partie.get_joueur(1).hand.cartes)
		mes_cartes_avant2 = list(self.ma_partie.get_joueur(3).hand.cartes)
		joueur_gagnant, carte_jouees = self.ma_donne.joue_plie(self.ma_partie.get_joueur(1))
		self.assertIn(carte_jouees[0],mes_cartes_avant1)
		self.assertIn(carte_jouees[2],mes_cartes_avant2)
		self.assertNotIn(carte_jouees[0],self.ma_partie.get_joueur(1).hand.cartes)
		self.assertNotIn(carte_jouees[1],self.ma_partie.get_joueur(3).hand.cartes)	
		
	def test_joue_donne(self):
		self.ma_donne.joue_donne()
		self.assertEqual(0,len(self.ma_partie.get_joueur(1).hand.cartes))
		self.assertEqual(157,self.ma_partie.get_equipe(1).points + self.ma_partie.get_equipe(2).points)


	def test_joue_partie(self):
		self.ma_partie.joue()
		self.assertEqual(0,0)
