# coding: utf8

import bin.base_jeu as base_jeu
#from base_jeu.hand import *
#from base_jeu.couleur import *


class joueur_physique(base_jeu.joueur):
	"""joueur qui a un accès à un ordi et un cerveau"""

	def joue(self,donne,cartes_jouees):
		"""fonction qui définit comment on joue une carte"""
		print "\n\n"
		print self.hand
		if len(cartes_jouees) ==0:
			print "vous êtes le premier à jouer"
			couleur_plie = None
		else:
			print "carte jouee: ",
			for carte in cartes_jouees:
				print str(carte) + " - ",
			print " "
			couleur_plie =cartes_jouees[0].couleur
		carte_a_jouer = self.get_entree(self.hand.get_cartes_jouable(donne.atout,couleur_plie))
		self.hand.cartes.remove(carte_a_jouer)
		return carte_a_jouer

	def get_entree(self,cartes_jouable):
		"""fonction pour vérifier que l'entrée est bien"""
		good = 0
		while good ==0:
			a = raw_input("Entrez la carte que vous voulez jouer: ")
			try:
				n = int(a)
				if n in [self.hand.get_position(carte) for carte in cartes_jouable]:
					carte = n
					good = 1
				else:
					print "vous n'avez pas le droit de jouer cette carte"
				
			except:
				print "SVP entrez un nombre"
		return self.get_carte(carte)		
				
		
	
			
