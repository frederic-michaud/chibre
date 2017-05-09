# coding: utf8

from carte import *
from couleur import *


class hand:
	def __init__(self,perm = None):
		"""fonction pour construire une main """
		if perm is not None:
			self.cartes = [carte(Ide = i) for i in sorted(perm)]
		else:
			self.cartes = []

	def __repr__(self):
		if len(self.cartes)>0:
			return "\n".join([carte.__repr__() for carte in self.cartes])
		else:
			return "Il n'y a pas de carte dans ce jeu"
	
	def __getitem__(self,key):
		return self.cartes[key-1]
		
	def __setitem__(self,key,value):
		self.cartes[key-1] = carte(Ide = value)

	def joue(self,donne,cartes_jouees):
		"""fonction qui définit comment on joue une carte"""
		if len(cartes_jouees) == 0:
			couleur_plie = None
		else:
			couleur_plie = cartes_jouees[0].couleur	
		cartes_jouable = self.get_cartes_jouable(donne.atout, couleur_plie)
		carte_a_jouer = self.get_carte_forte(cartes_jouable, donne.atout, couleur_plie)
		self.cartes.remove(carte_a_jouer)
		return carte_a_jouer
			
	def get_cartes_couleur(self,couleur):
		""" fonction qui retourne toutes les cartes d'une certaines couleur de la main donnée"""
		cartes = [carte for carte in self.cartes if carte.couleur == couleur]
		return cartes
		
	def get_carte_forte(self,cartes,couleur_atout, couleur_plie):
		"""fonction qui retourne la carte la plus forte d'en ensemble de carte"""
		forces = [carte.valeur_force(couleur_atout, couleur_plie) for carte in cartes]
		index_max = forces.index(max(forces))
		return cartes[index_max]
		
	def get_cartes_jouable(self, couleur_atout, couleur_plie):
		"""fonction qui retourne l'ensemble des cartes que j'ai le droit de jouer dans ma main"""
		if couleur_plie == None:
			cartes_jouable = self.cartes
		else:
			cartes_couleur = self.get_cartes_couleur(couleur_plie)	
			cartes_atout = self.get_cartes_couleur(couleur_atout)
			if couleur_plie != couleur_atout:			
				if len(cartes_couleur) == 0:
					cartes_jouable = self.cartes
				else:
					cartes_jouable = cartes_couleur + cartes_atout
			else:
				valet_atout = carte(Rang = "valet", Couleur = couleur_atout.nom)
				if len(cartes_couleur) == 0 or cartes_couleur == [valet_atout]:
					cartes_jouable = self.cartes
				else:
					cartes_jouable = cartes_couleur
		return cartes_jouable
		
	def evalue_atout(self,couleur):
		"""fonction qui associe une force à chaque couleur d'atout"""
		cartes = self.get_cartes_couleur(couleur)
		return sum([carte.rang.valeur_atout() for carte in cartes])
			
