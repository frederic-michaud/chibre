# coding: utf8

import numpy as np
from hand import *
class jeu:
	"""classe qui définit comment se déroule une partie"""
	def __init__(self, Joueur_atout = 1, Atout = 1):
		"""constructeur qui prend en argument le Joueur_atout, l'Atout et d'autres paramètres"""
		donne = (np.random.permutation(36) +1).reshape(4,9)
		self.hands = [hand(perm = i) for i in donne]
		self.joueur_atout = Joueur_atout
		self.atout = couleur(Ide = Atout)
		self.equipe_1_points = 0
		self.equipe_2_points = 0
	
	def joue_donne(self):
		"""fonction qui définit comment on joue chaque donne"""
		joueur_commence = self.joueur_atout
		for i in range (1,10):
			(joueur_gagnant, cartes_jouee) = self.joue_plie(joueur_commence)
			self.compatibilise(joueur_gagant, cartes_jouee)
			joueur_commence = joueur_gagnant
			
	def compatibilise(self,joueur_gagnant,cartes):
		score = sum([carte.valeur_point(self) for carte in cartes])
		if joueur_gagnant in [1,3]:
			self.equipe_1_points +=score
		else:
			self.equipe_2_points +=score

		
	def joue_plie():
		"""fonction qui définit comment on joue chaque plie"""
		for i in range(4):
			joueur_joue()
			
			
