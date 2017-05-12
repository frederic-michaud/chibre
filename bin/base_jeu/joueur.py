# coding: utf8
from hand import * 
from couleur import *

class joueur:
	"""classe qui définit ce qu'est un joueur. Les joueurs sont définis de 1 à 4. le premier et le troisième joueur sont dans l'équipe 1 alors que le 2eme et le 4eme joueurs sont dans l'équipe 2"""
	def __init__(self, Ide = 1, Equipe = 0,Hand = None):
		"""constructeur qui prend en argument une équipe 'Equipe' et un jeu 'Hand' """
		#self.n_equipe = Equipe
		self.hand = Hand
		self.ide = Ide
	
	def joue(self,donne,cartes_jouees):
		"""fonction qui définit comment on joue une carte"""
		ma_carte = self.hand.joue(donne,cartes_jouees)
		return ma_carte

	def decide_atout(self):
		"""fonction qui décide de l'atout en fonction de la main du joueur"""
		couleurs = [couleur(Ide = i) for i in range(1,5)]
		forces = [self.hand.evalue_atout(c) for c in couleurs]
		index_couleur = forces.index(max(forces))
		return couleurs[index_couleur]		
		
	def get_carte(self,i):
		return self.hand.cartes[i-1]
		
	def __repr__(self):
		return "joueur N°"+str(self.ide)
		
	
			
