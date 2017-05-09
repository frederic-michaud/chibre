# coding: utf8
from rang import *
from couleur import *
import numpy as np
from hand import *
from joueur import *

class donne:
	def __init__(self,partie):
		"""fonction qui commence une nouvelle donne en distribuant les cartes et en choississant l'atout"""
		carte_jouee = []
		self.partie = partie
		#self.distribue()
		#self.atout = partie.joueur_atout.decide_atout()
		#self.points = [0,0]
		#self.joue_donne()
		#self.fin_donne(partie)
		
		
	def distribue(self):
		"""fonction qui distribue les cartes de manières aléatoires aux quatre joueurs"""
		permutations = (np.random.permutation(36) +1).reshape(4,9)
		hands = [hand(perm = i) for i in permutations]
		for i in range(4):
			self.partie.get_joueur(i+1).hand = hands[i]			
		self.atout = self.partie.joueur_atout.decide_atout()
			
	def compatibilise(self,equipe_gagnant,cartes):
		""" fonction qui détermine le nombre de points gagnés dans une plie"""
		score = sum([carte.valeur_point(self) for carte in cartes])
		equipe_gagnant.points+=score

	def joue_donne(self):
		"""fonction qui définit comment on joue chaque donne"""
		joueur_commence = self.partie.joueur_atout
		for i in range (1,10):
			(joueur_gagnant, cartes_jouees) = self.joue_plie(joueur_commence)
			self.compatibilise(self.partie.get_equipe(joueur = joueur_gagnant), cartes_jouees)
			joueur_commence = joueur_gagnant
		self.partie.get_equipe(joueur = joueur_gagnant).points +=5	
		
	def joue_plie(self,joueur_commence):
		"""fonction qui définit comment on joue chaque plie"""
		cartes_jouees = []
		for i in range(4):
			cartes_jouees.append(self.partie.get_joueur(i + joueur_commence.ide).joue(self,cartes_jouees))
		joueur_gagnant	= self.determine_gagnant(cartes_jouees)
		return (joueur_gagnant, cartes_jouees)
		
	def determine_gagnant(self,cartes_jouees):
		"""fonction qui determine le combientième joueur a gagné la plie"""
		couleur_plie = cartes_jouees[0].couleur
		values = [carte.valeur_force(couleur_plie, self.atout) for carte in cartes_jouees]
		joueur_gagnant = values.index(max(values))+1
		return self.partie.get_joueur(joueur_gagnant)
	
