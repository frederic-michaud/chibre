# coding: utf8

import numpy as np
from hand import *
from equipe import *
from joueur import *
from donne import *
class partie:
	"""classe qui définit comment se déroule une partie"""
	def __init__(self):
		"""constructeur qui prend en argument le Joueur_atout, l'Atout et d'autres paramètres"""
		joueurs = [joueur(Ide = i) for i in range(1,5)]
		self.equipes = [equipe(J1 = joueurs[0], J2 = joueurs[1], Ide = 1),equipe(J1 = joueurs[2], J2 = joueurs[3], Ide = 2)]

	
	def joue(self):
		"""fonction qui définit comment se joue une partie jusqu'à 1000"""
		self.joueur_atout = self.get_joueur(2)
		while self.get_equipe(1).points < 1000 and self.get_equipe(2).points < 1000:			
			ma_donne = donne(self)
			ma_donne.distribue()
			ma_donne.joue_donne()
			self.joueur_atout = self.get_joueur(self.joueur_atout.ide+1)
		if self.equipes[0].points < self.equipes[1].points :
			print ("l'équipe N° 2 a gagné {score2} à {score1}, et Freddou c'est le meilleur. Vive l'équipe 2 !".format(score1 = self.get_equipe(1).points, score2 = self.get_equipe(2).points))

		else:
			print "l'équipe N° 1 a gagné {score1} à {score2}. Franchement, c'est abusé seulement {score2} points?".format(score1 = self.get_equipe(1).points, score2 = self.get_equipe(2).points)

		
	def get_equipe(self,i = 1, joueur = None):
		"""fonction qui retourne une équipe du jeu, indexé entre 1 et 2"""
		if joueur == None:
			return self.equipes[i-1]
		else:
			return self.equipes[(joueur.ide+1)%2]
		
	def get_joueur(self,i):
		"""fonction qui retourne un joueur, indexé de 1 à 4"""
		while i > 4:
			i -= 4
		i-=1
		return self.equipes[int(i/2)].joueurs[i%2]
		
		
			
			
